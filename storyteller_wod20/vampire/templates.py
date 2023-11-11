from django.conf import settings
from storyteller_wod20.templates import _WoD20Template


class _V20Template(_WoD20Template):
    pass


class Mortal(_V20Template):
    fields = ["Nature", "Demeanor"]


class Vampire(_V20Template):
    power_stat = "Generation"
    fields = ["Clan", "Path", "Nature", "Demeanor", "Bloodline"]
    field_choices = {
        "Clan": ["Assamite", "Brujah", "Followers of Set", "Gangrel", "Giovanni", "Lasombra", "Malkavian", "Nosferatu",
                 "Ravnos", "Toreador", "Tremere", "Tzimisce", "Ventrue", "Caitiff"],
        "Path": ["Humanity", "Blood", "Bones", "Caine", "Cathari", "Feral Heart", "Honorable Accord", "Lilith",
                 "Metamorphosis", "Night", "Paradox", "Power and the Inner Voice", "Typhon"]
    }
    field_defaults = {
        "Clan": "Brujah",
        "Path": "Humanity"
    }