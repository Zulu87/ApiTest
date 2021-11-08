from api_client.abstract_api_client import AbstractApiClient

#описуємо клієнта для ендпоінта Pet, також описуємо властиві йому методи згідно свегерфайлу

class PetClient(AbstractApiClient):
    pet_endpoint = "pet"

    def add_pet(self, data_payload, param = None):
        return self._post(endpoint=PetClient.pet_endpoint, payload = data_payload, param=param)


    def update_pet(self):
        return self._put(endpoint=UserClient.pet_endpoint, payload = data_payload)

    def get_pet_by_status(self, status):
        params = f'''findByStatus?status={status}'''
        return self._get(endpoint=PetClient.pet_endpoint, param=params)

    def get_pet_by_tags(self, tag):
        params = f'''findByTags?tags={tag}'''
        return self._get(endpoint=PetClient.pet_endpoint, param=params)

    def get_pet_by_id(self, id):
        return self._get(endpoint=PetClient.pet_endpoint, param=id)

    def update_pet_by_id(self, id, name, status):
        params = f'''{id}?name={name}&status={status}'''
        return self._get(endpoint=PetClient.pet_endpoint, param=params)


    def delete_pet_by_Id(self, id):
        return self._delete(endpoint=PetClient.pet_endpoint, param=id)

    def update_pet_image(self, id, file, metadata=None):
        if metadata:
            params = f'''{id}/uploadImage?&additionalMetadata={metadata}'''
        else:
            params = f'''{id}/uploadImage'''
        return self._post_with_files(endpoint=PetClient.pet_endpoint, file_to_open=file, param=params)
