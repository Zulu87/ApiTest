from api_client.abstract_api_client import AbstractApiClient

#описуємо клієнта для ендпоінта Store, також описуємо властиві йому методи згідно свегерфайлу
class StoreClient(AbstractApiClient):
    store_endpoint = "store"

    def add_order_for_pet(self, data_payload, param=None):
        return self._post(endpoint=StoreClient.store_endpoint, payload = data_payload, param=param)

    def find_order_by_id(self, orderID):
        params = f'''order/{orderID}'''
        return self._get(endpoint=StoreClient.store_endpoint, param=params)

    def delete_order_by_id(self, orderID):
        params = f'''order/{orderID}'''
        return self._delete(endpoint=StoreClient.store_endpoint, param=params)

    def get_inventories (self):
        return self._get(endpoint=StoreClient.store_endpoint, param='inventory')