import pytest
from api_client.alert_client import AlertPublicAPI
from api_client.helper import *


#фікстура викликатиме апіклієнта для Алерта
@pytest.fixture(scope="session")
def alert_client(request):
    api_client = AlertPublicAPI(env=config_json("envs/config.json"))
    yield api_client
    del api_client
