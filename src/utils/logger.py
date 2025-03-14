import logging, os

from src.utils.env import EnvManager

env_manager = EnvManager()
STORAGE, USE_PRINT = env_manager.get_env("STORAGE"), env_manager.get_env("USE_PRINT")

if not os.path.exists(STORAGE): os.makedirs(STORAGE)

logging.basicConfig(filename=f'{STORAGE}/app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s')
LOGGER = (lambda message: print(message + '\n')) if USE_PRINT \
    else (lambda message: logging.getLogger(__name__).info(message + '\n'))
