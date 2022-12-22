from ninja import NinjaAPI
from Coworking.api import router as coworking_router

api = NinjaAPI()

api.add_router("/api/", coworking_router)
