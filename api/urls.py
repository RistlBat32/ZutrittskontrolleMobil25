from django.urls import path
from .views import checkin_checkout, all_users, manual_checkout, add_ada, add_nfc_chip, delete_ada, get_ada_list, register_nfc_card, battery_status, import_excel

urlpatterns = [
    path("checkin/", checkin_checkout),
    path("users/", all_users, name="all_users"),
    path("checkout/<int:ada_id>/", manual_checkout, name="manual_checkout"),
    path("add_ada/", add_ada, name="add_ada"),
    path("add_nfc_chip/", add_nfc_chip, name="add_nfc_chip"),
    path("delete_ada/<int:ada_id>/", delete_ada, name="delete_ada"),
    path("get_ada_list/", get_ada_list, name="get_ada_list"),
    path("register_nfc_card/", register_nfc_card, name="register_nfc_card"),
    path("battery/", battery_status, name="battery_status"),
    path("import_excel/", import_excel, name="import_excel"),
]