import pytest
import csv
from api_client.user_client import UserClient
from api_client.store_client import StoreClient
from api_client.pet_client import PetClient


#фікстура викликатиме апіклієнта для енпоїнта User
@pytest.fixture(scope="session")
def current_user_client(request):
    api_client = UserClient()
    yield api_client
    del api_client


#фікстура викликатиме апіклієнта для енпоїнта Store
@pytest.fixture(scope="session")
def current_store_client(request):
    api_client = StoreClient()
    yield api_client
    del api_client


#фікстура викликатиме апіклієнта для енпоїнта Pet
@pytest.fixture(scope="session")
def current_pet_client(request):
    api_client = PetClient()
    yield api_client
    del api_client

#фікстура для передавання даних з csv файлу в пейлод реквеста
@pytest.fixture(scope="function")
def users_data_provider():
    def _csv_to_dict(a):
        with open(a, 'r') as read_obj:
            dict_reader = csv.DictReader(read_obj)
            list_of_dict = list(dict_reader)

            #тут запускаємо цикл який пройдеться по ключах для яких значення повинобути числовим і конвертне їх зі стрічкового типу в числовий
            for i in range(len(list_of_dict)):
                for item in ('id','userStatus', 'petId', 'quantity'):
                    if item in list_of_dict[i].keys():
                        list_of_dict[i][item] = int(list_of_dict[i][item])
            if len(list_of_dict)==1:
                return list_of_dict[0]
            else:
                return list_of_dict

    return _csv_to_dict