from api_client.abstract_api_client import AbstractApiClient

from api_client.helper import *


#описуємо клієнта для ендпоінта Alert, також описуємо властиві йому методи згідно документації паблік апі

class AlertPublicAPI(AbstractApiClient):
    endpoint = "api/v1/alerts"
    def __init__(self, env, user=None):
        super().__init__(env, user)

    def create_alert(self, data_payload, param = None):
        return self._post(endpoint=AlertPublicAPI.endpoint, data = data_payload, param=param)

    def query_alerts(self, parameters):
        return self._get(endpoint=AlertPublicAPI.endpoint, param=parameters)

    def get_alert(self, alertId):
        return self._get(endpoint=AlertPublicAPI.endpoint, param=alertId)

    def get_alert_evidence(self, alertId):
        return self._get(endpoint=AlertPublicAPI.endpoint, param = {alertId}+"/evidence")

    def сreate_alert_evidence(self, data_payload, alertId):
        return self._get(endpoint=AlertPublicAPI.endpoint,payload = data_payload, param = {alertId}+"/evidence")
