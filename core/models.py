from django.db import models
from django.utils.timezone import now

RANK_CHOICES = [
    ("Sdt", "Soldat (Sdt)"),
    ("Gfr", "Gefreiter (Gfr)"),
    ("Obgfr", "Obergefreiter (Obgfr)"),
    ("Kpl", "Korporal (Kpl)"),
    ("Wm", "Wachtmeister (Wm)"),
    ("Obwm", "Oberwachtmeister (Obwm)"),
    ("Fw", "Feldweibel (Fw)"),
    ("Four", "Fourier (Four)"),
    ("Hptfw", "Hauptfeldweibel (Hptfw)"),
    ("Adj Uof", "Adjutant Unteroffizier (Adj Uof)"),
    ("Stabsadj", "Stabsadjutant (Stabsadj)"),
    ("Hptadj", "Hauptadjutant (Hptadj)"),
    ("Chefadj", "Chefadjutant (Chefadj)"),
    ("Lt", "Leutnant (Lt)"),
    ("Oblt", "Oberleutnant (Oblt)"),
    ("Hptm", "Hauptmann (Hptm)"),
    ("Maj", "Major (Maj)"),
    ("Oberstlt", "Oberstleutnant (Oberstlt)"),
    ("Oberst", "Oberst"),
    ("Fach Of", "Fachoffizier (Fach Of)"),
    ("Br", "Brigadier (Br)"),
    ("Div", "Divisionär (Div)"),
    ("KKdt", "Korpskommandant (KKdt)"),
    ("Gen", "General"),
]

class AdA(models.Model):
    rank = models.CharField(max_length=20, choices=RANK_CHOICES)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    is_checked_in = models.BooleanField(default=False)
    last_checkin_time = models.DateTimeField(null=True, blank=True)
    last_checkout_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.rank} {self.last_name} {self.first_name}"

class NFCChip(models.Model):
    nfc_id = models.CharField(max_length=50, unique=True)
    ada = models.OneToOneField(AdA, on_delete=models.CASCADE, related_name="nfc_chip", null=True, blank=True)

    def __str__(self):
        return f"NFC {self.nfc_id} für {self.ada.last_name}" if self.ada else f"NFC {self.nfc_id} (nicht zugewiesen)"