import hashlib
from ipss_pb2 import Service
from compile import LOGGER

# -- HASH FUNCTIONS --
SHAKE_256 = lambda value: "" if value is None else 'shake-256:0x'+hashlib.shake_256(value).hexdigest(32)
SHA3_256 = lambda value: "" if value is None else 'sha3-256:0x'+hashlib.sha3_256(value).hexdigest()

def calculate_hashes(value) -> list:
    return [
        SHA3_256(value),
        SHAKE_256(value)
    ]

def prune_hashes_of_service(service: Service) -> Service:
    s = Service()
    s.CopyFrom(service)
    recursive_prune(field=s)
    return s

    def recursive_prune(field: any) -> any:
        try:
            field.ClearField('hash')
        except ValueError: pass
        try:
            for attribute in field.ListFields():
                if attribute[0].number == 15: # The hash field is always on index 15.
                    s.ClearField(attribute[0].name) # 'name' is the field's name on our serializer.
                else:
                    recursive_prune(field=field)
        except AttributeError: pass

def get_service_hash(service: Service, hash_type: str) -> list:
    if hash_type == "sha3-256":
        return SHA3_256(
            value=prune_hashes_of_service(
                service=Service
            ).SerializeToString()
        )
    else:
        LOGGER(hash_type+' hash function is not implemented on this method.')
        return Service