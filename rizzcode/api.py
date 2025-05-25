import sys


try:
    from ninja import NinjaAPI
except ImportError:
    print("Ninja is required for this project.")
    sys.exit(-1)

api = NinjaAPI()

from zadania.api import router as zadania_router

api.add_router("/", zadania_router)

@api.get("/hello")
def hello(request):
    return "Hello World"
