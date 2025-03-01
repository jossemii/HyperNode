import threading
from concurrent import futures

import grpc, json

from protos import gateway_pb2, gateway_pb2_grpc
from src.gateway.gateway import Gateway
from src.tunneling_system.tunnels import TunnelSystem
from src.manager.maintain_thread import manager_thread
from src.utils import logger as log
from src.utils.env import EnvManager

env_manager = EnvManager()

GATEWAY_PORT = env_manager.get_env("GATEWAY_PORT")
IGNORE_FATHER_NETWORK_ON_SERVICE_BALANCER = env_manager.get_env("IGNORE_FATHER_NETWORK_ON_SERVICE_BALANCER")
SEND_ONLY_HASHES_ASKING_COST = env_manager.get_env("SEND_ONLY_HASHES_ASKING_COST")
DENEGATE_COST_REQUEST_IF_DONT_VE_THE_HASH = env_manager.get_env("DENEGATE_COST_REQUEST_IF_DONT_VE_THE_HASH")
COMPUTE_POWER_RATE = env_manager.get_env("COMPUTE_POWER_RATE")
COST_OF_BUILD = env_manager.get_env("COST_OF_BUILD")
EXECUTION_BENEFIT = env_manager.get_env("EXECUTION_BENEFIT")
MANAGER_ITERATION_TIME = env_manager.get_env("MANAGER_ITERATION_TIME")
COST_AVERAGE_VARIATION = env_manager.get_env("COST_AVERAGE_VARIATION")
GAS_COST_FACTOR = env_manager.get_env("GAS_COST_FACTOR")
MODIFY_SERVICE_SYSTEM_RESOURCES_COST = env_manager.get_env("MODIFY_SERVICE_SYSTEM_RESOURCES_COST")
EXTERNAL_COST_TIMEOUT = env_manager.get_env("EXTERNAL_COST_TIMEOUT")

def serve():

    # Run manager.
    threading.Thread(
        target=manager_thread,
        daemon=True
    ).start()

    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=30))
    gateway_pb2_grpc.add_GatewayServicer_to_server(
        Gateway(), server=server
    )

    SERVICE_NAMES = (
        gateway_pb2.DESCRIPTOR.services_by_name['Gateway'].full_name,
    )

    server.add_insecure_port('[::]:' + str(GATEWAY_PORT))

    log.LOGGER('COMPUTE POWER RATE -> ' + str(COMPUTE_POWER_RATE))
    log.LOGGER('COST OF BUILD -> ' + str(COST_OF_BUILD))
    log.LOGGER('EXECUTION BENEFIT -> ' + str(EXECUTION_BENEFIT))
    log.LOGGER('IGNORE FATHER NETWORK ON SERVICE BALANCER -> ' + str(IGNORE_FATHER_NETWORK_ON_SERVICE_BALANCER))
    log.LOGGER('SEND ONLY HASHES ASKING COST -> ' + str(SEND_ONLY_HASHES_ASKING_COST))
    log.LOGGER('DENEGATE COST REQUEST IF DONT VE THE HASH -> ' + str(DENEGATE_COST_REQUEST_IF_DONT_VE_THE_HASH))
    log.LOGGER('MANAGER ITERATION TIME-> ' + str(MANAGER_ITERATION_TIME))
    log.LOGGER('AVG COST MAX PROXIMITY FACTOR-> ' + str(COST_AVERAGE_VARIATION))
    log.LOGGER('GAS_COST_FACTOR-> ' + str(GAS_COST_FACTOR))
    log.LOGGER('MODIFY_SERVICE_SYSTEM_RESOURCES_COST_FACTOR-> ' + str(MODIFY_SERVICE_SYSTEM_RESOURCES_COST))
    log.LOGGER('EXTERNAL_COST_TIMEOUT -> ' + str(EXTERNAL_COST_TIMEOUT))

    log.LOGGER('Starting gateway at port' + str(GATEWAY_PORT))
    log.LOGGER(f"Available tunnels: {json.dumps(TunnelSystem().get_gateway_urls(), indent=4)}")

    server.start()
    server.wait_for_termination()
