from data.endpoints import Endpoints


# def get_pet_endpoints():
#     return {
#         "create_pet": Endpoints.CreatePetEndpoints(),
#         "get_pet": Endpoints.GetPetEndpoints()
#     }


def get_pet_endpoints():
    return Endpoints.CreatePetEndpoints()
