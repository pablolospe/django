from django.contrib import admin
from django.urls import path , include
# from .router import router 


from .views import      UsersListView   \
                    ,   UsersDetailView \
                    ,   UsersCreateView \
                    ,   UsersUpdateView \
                    ,   UsersDeleteView

app_name = "users"

urlpatterns = [
    path("", UsersListView.as_view(), name="all"),
    path("create/", UsersCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", UsersDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", UsersUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", UsersDeleteView.as_view(), name="delete")
]

# urlpatterns += router.urls

# criptoplus---->>>