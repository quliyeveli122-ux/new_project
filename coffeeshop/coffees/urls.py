from django.urls import path
from .views import get_all_coffees, get_iced_coffees


urlpatterns = [
    path(
        "api/v1/coffees",
        get_all_coffees
    ),
    path(
        "api/v1/coffees/iced",
        get_iced_coffees
    )
]