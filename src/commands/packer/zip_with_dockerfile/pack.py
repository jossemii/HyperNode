import os, sys, time, threading, shutil
from hashlib import sha3_256
from typing import Optional
import grpc
from bee_rpc import client as grpcbb

from protos import celaut_pb2, pack_pb2, gateway_pb2_bee, gateway_pb2_grpc
from src.commands.packer.zip_with_dockerfile.prepare_directory import prepare_directory
from src.commands.packer.zip_with_dockerfile.generate_service_zip import generate_service_zip
from src.database.access_functions.peers import get_peer_ids, get_peer_directions
from src.utils.env import EnvManager

env_manager = EnvManager()

GATEWAY_PORT = env_manager.get_env("GATEWAY_PORT")
METADATA_REGISTRY = env_manager.get_env("METADATA_REGISTRY")
REGISTRY = env_manager.get_env("REGISTRY")

def __spinner(event):
    """Spinner function to show progress while the main task runs."""
    spinner = ['|', '/', '-', '\\']
    messages = [
        "Processing... This might take a while.",
        "Processing... Please wait, the node is working.",
        "Processing... Almost there, please hold on.",
        "Processing... Still working, hang tight."
    ]
    idx = 0
    msg_idx = 0
    start_time = time.time()

    while not event.is_set():
        # Show spinner animation
        sys.stdout.write(f'\r{messages[msg_idx]} {spinner[idx]}')
        sys.stdout.flush()
        idx = (idx + 1) % len(spinner)

        # Update message every minute
        if time.time() - start_time > 60:
            msg_idx = (msg_idx + 1) % len(messages)
            start_time = time.time()

        time.sleep(0.1)  # Adjust speed of spinner

    sys.stdout.write('\rProcess complete!   \n')  # Clear spinner after done
    sys.stdout.flush()



def __pack(zip, node: str):
    yield from grpcbb.client_grpc(
        method=gateway_pb2_grpc.GatewayStub(
            grpc.insecure_channel(node)
        ).Pack,
        input=grpcbb.Dir(dir=zip, _type=bytes),
        indices_serializer={0: bytes},
        indices_parser=gateway_pb2_bee.PackOutput_indices,
        partitions_message_mode_parser={1: True, 2: True, 3: False}
    )


def __on_peer(peer: str, service_zip_dir: str):
    _id: Optional[str] = None
    print(f'Starting compilation on {peer}...')
    
    # Create an event to control the spinner thread
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=__spinner, args=(stop_event,))
    spinner_thread.start()
    
    try:
        for b in __pack(
                zip=service_zip_dir,
                node=peer
        ):
            if type(b) is pack_pb2.PackOutputServiceId:
                if not _id:
                    _id = b.id.hex()
            elif type(b) == celaut_pb2.Metadata and _id:
                with open(f"{METADATA_REGISTRY}{_id}", "wb") as f:
                    f.write(b.SerializeToString())
            elif type(b) == grpcbb.Dir and b.type == pack_pb2.Service and _id:
                # b is ServiceWithMeta grpc-bb cache directory.
                os.system(f"mv {b.dir} {REGISTRY}{_id}")
            elif type(b) == pack_pb2.PackOutputError:
                print(f"\nError in the compilation process: \n{b.message}")
                return
            else:
                raise Exception('\nError with the packer output:' + str(b))

    finally:
        # Stop the spinner when the process completes
        stop_event.set()
        spinner_thread.join()

    print('Compilation complete.')
    print('Service ID -> ', _id)
    print('\nValidating the content...')

    validate_id = sha3_256()

    try:
        for i in grpcbb.read_multiblock_directory(f"{REGISTRY}{_id}/"):
            validate_id.update(i)
        print("validated service id -> ", validate_id.hexdigest())
    except Exception as e:
        print(f"Maybe it doesn't have blocks? validation will occurr into an error due to https://github.com/celaut-project/nodo/issues/38")


def __remove_path(path):
    if os.path.exists(path):
        (os.remove if os.path.isfile(path) else shutil.rmtree)(path)
        print(f"Removed: '{path}'")


def pack_directory(directory: str):
    is_remote, directory = prepare_directory(directory)
    
    service_zip_dir: str = generate_service_zip(
        project_directory=directory
    )

    # TODO check if dependencies has directories, and pack them before.
    try:
        ip, port = None, None
        if False:  # TODO; control exceptions and try others; and enviroment variable COMPILE_LOCAL_FIRST
            for peer_id in list(get_peer_ids()):
                for _ip, _port in get_peer_directions(peer_id=peer_id):
                    ip, port = _ip, _port
        if not ip or not port:
            ip, port = 'localhost', GATEWAY_PORT
        __on_peer(peer=f"{ip}:{port}", service_zip_dir=service_zip_dir)
    finally:
        # __remove_path(service_zip_dir)
        
        if is_remote: 
            __remove_path(directory)
