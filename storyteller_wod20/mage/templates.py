from django.conf import settings
from storyteller_wod20.templates import _WoD20Template


class _M20Template(_WoD20Template):
    sheet_footer = "Mage: The Ascension"


class Mortal(_M20Template):
    pass


class Mage(_M20Template):
    power_stat = "Arete"
    fields = ["Nature", "Demeanor", "Essence", "Affiliation"]
    advantages = ["Willpower", "Arete"]
