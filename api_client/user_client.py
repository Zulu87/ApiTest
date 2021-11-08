from api_client.abstract_api_client import AbstractApiClient


#описуємо клієнта для ендпоінта User, також описуємо властиві йому методи згідно свегерфайлу

class UserClient(AbstractApiClient):
    user_endpoint = "user"

    def add_user(self, data_payload, param = None):
        return self._post(endpoint=UserClient.user_endpoint, payload = data_payload, param=param)

    def get_user_by_username(self, username):
        return self._get(endpoint=UserClient.user_endpoint, param=username)

    def update_user(self, username):
        return self._put(endpoint=UserClient.user_endpoint, param=username)

    def delete_user(self, username):
        return self._delete(endpoint=UserClient.user_endpoint, param=username)

    def log_user(self, username, password):
        params = f'''login?username={username}&password={password}'''
        return self._get(endpoint=UserClient.user_endpoint, param=params)

    def logout_user(self):
        params = "logout"
        return self._get(endpoint=UserClient.user_endpoint, param=params)

    def delete_user_by_username(self, username):
        return self._delete(endpoint=UserClient.user_endpoint, param=username)
