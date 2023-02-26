import requests
import json



#описуємо абстракну апі з методами які ляжуть в основу для клієнтів відповідних ендпоїнтів
class AbstractApiClient:
    def __init__(self, env, user=None):

        self.base_url = env["envAddress"]
        self.user = env['users']['public_api_user'] if user is None else env['users'][user]
        self.api_key = self.user['public_api_key']
        self.headers = {'Accept': '*/*', 'Content-Type': 'application/json',
                       'x-api-key': self.api_key}
        self.__client = requests.Session()


    # оголошуємо метод який виконуватиме get запити
    def _get(self, endpoint, param):
        url = f"{self.base_url}/{endpoint}/{param}"
        res = self.__client.get(url, headers = self.headers)
        return res


    # оголошуємо метод який виконуватиме post запити
    def _post(self, endpoint, data, param = None ):
        if param:
            url = f"{self.base_url}/{endpoint}/{param}"
        else:
            url = f"{self.base_url}/{endpoint}"
        res = self.__client.post(url, headers = self.headers, data = json.dumps(data))
        return res


    # оголошуємо метод який виконуватиме put запити
    def _patch(self, endpoint, payload, param = None ):
        if param:
            url = f"{self.base_url}/{endpoint}/{param}"
        else:
            url = f"{self.base_url}/{endpoint}"
        res = self.__client.put(url, headers = self.headers, json = payload)
        return res

    def __del__(self):
        self.__client.close()