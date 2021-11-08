from api_client.user_client import *
from api_client.pet_client import *
from api_client.store_client import *



class TestStore:

    # тест на додавання одного юзера
    def test_user_is_added(self, current_user_client: UserClient, users_data_provider):
        single_user_request = current_user_client.add_user(data_payload = users_data_provider("single_user_data.csv"))

        assert single_user_request.status_code == 200, f"Request failed with the status code {single_user_request.status_code}"

    # тест на додавання кількох юзерів списком
    def test_few_users_are_added(self, current_user_client: UserClient, users_data_provider):
        few_users_request = current_user_client.add_user(data_payload = users_data_provider("multiple_users_data.csv"), param="createWithList")

        assert few_users_request.status_code == 200, f"Request failed with the status code {few_users_request.status_code}"

    # тест на отримання даних юзера за юзернеймом
    def test_get_users_by_username(self, current_user_client: UserClient, users_data_provider):
        get_user_request = current_user_client.get_user_by_username(username=users_data_provider("single_user_data.csv")['username'])

        assert get_user_request.status_code == 200, f"Request failed with the status code {get_user_request.status_code}"

    # тест на логін юзера
    def test_user_is_logged(self, current_user_client: UserClient, users_data_provider):
        login_user_request = current_user_client.log_user(username=users_data_provider("single_user_data.csv")['username'], password=users_data_provider("single_user_data.csv")['password'])

        assert login_user_request.status_code == 200, f"Request failed with the status code {login_user_request.status_code}"

    # тест на логоут юзера
    def test_user_is_logged_out(self, current_user_client: UserClient,users_data_provider ):
        logout_user_request = current_user_client.logout_user()

        assert logout_user_request.status_code == 200, f"Request failed with the status code {logout_user_request.status_code}"

    # тест на додавання ордера на тваринку
    def test_place_order_for_pet(self, current_store_client: StoreClient, users_data_provider):
        order_for_pet_request = current_store_client.add_order_for_pet(data_payload=users_data_provider("single_pet_data.csv"), param='order')

        assert order_for_pet_request.status_code == 200, f"Request failed with the status code {order_for_pet_request.status_code}"

    # тест на апдейт зображення для тваринки
    def test_pet_image_update(self, current_pet_client: PetClient, users_data_provider):
        image_update_request = current_pet_client.update_pet_image(id =users_data_provider("single_pet_data.csv")["id"], file = 'pokemon_grookey.png', metadata="test")

        assert image_update_request.status_code == 200, f"Request failed with the status code {image_update_request.status_code}"

    # тест на повернення анкет тваринок згідно статусу
    def test_get_pet_inventories_by_status(self, current_store_client: StoreClient):
        get_inventories_request = current_store_client.get_inventories()

        assert get_inventories_request.status_code == 200, f"Request failed with the status code {get_inventories_request.status_code}"