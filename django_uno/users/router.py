from rest_framework import routers
from .viewsets import UserViewSet

router = routers.SimpleRouter()

# en este caso se le anexa a la ruta de las urls de la app
router.register("api-user",UserViewSet)