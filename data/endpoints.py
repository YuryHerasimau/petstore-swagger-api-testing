class Endpoints:

    class CreatePetEndpoints:
        create_pet = "/pet"

        def get_pet_by_id(self, petId: int):
            return f"/pet/{petId}"