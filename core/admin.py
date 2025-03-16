from django.contrib import admin
from .models import AdA, NFCChip

@admin.register(AdA)
class AdAAdmin(admin.ModelAdmin):
    list_display = ("rank", "last_name", "first_name", "get_nfc_id", "last_checkin_time", "last_checkout_time")
    search_fields = ("last_name", "first_name", "rank")
    list_filter = ("rank", "last_checkin_time", "last_checkout_time")  # Filter für Check-in/Check-out

    def get_nfc_id(self, obj):
        """Falls der AdA einen NFC-Chip hat, die ID anzeigen"""
        return obj.nfc_chip.nfc_id if hasattr(obj, "nfc_chip") else "-"

    get_nfc_id.short_description = "NFC-ID"


@admin.register(NFCChip)
class NFCChipAdmin(admin.ModelAdmin):
    list_display = ("nfc_id", "get_ada")  # NFC-ID & zugehöriger AdA anzeigen
    search_fields = ("nfc_id", "ada__last_name")  # Suchoptionen
    list_filter = ("ada",)  # Nach AdA filtern
    
    def get_ada(self, obj):
        """Falls der NFC-Chip einem AdA zugeordnet ist, Name anzeigen"""
        return f"{obj.ada.rank} {obj.ada.last_name}" if obj.ada else "Nicht zugewiesen"
    
    get_ada.short_description = "Zugewiesener AdA"