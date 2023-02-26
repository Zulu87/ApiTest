from api_client.alert_client import *

from api_client.helper import *


class TestAlertApi:

    # тест на створення алерта
    def test_alert_is_added(self, alert_client: AlertPublicAPI):

        alert_create_request = alert_client.create_alert(data_payload=config_json("alert_body.json"))

        assert alert_create_request.status_code == 201, f"Request failed with the status code {alert_create_request}"