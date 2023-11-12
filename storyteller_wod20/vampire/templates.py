from django.conf import settings
from storyteller_wod20.templates import _WoD20Template


class _V20Template(_WoD20Template):
    pass


class Mortal(_V20Template):
    fields = ["Nature", "Demeanor"]


class Vampire(_V20Template):
    """
    Developer Notes:

    Clan and Path are left open because V20 has a crazy amount of possible Clans/Bloodlines/Legacies which can be written
    in there. I'm not going to try to list them all. Let people write whatever they want in there.
    """

    power_stat = "Generation"
    fields = ["Clan", "Path", "Nature", "Demeanor"]
    field_defaults = {"Path": "Humanity"}
