from django.conf import settings
from storyteller_wod20.templates import _WoD20Template


class _EXVSWODTemplate(_WoD20Template):
    charm_categories = list()


class Mortal(_EXVSWODTemplate):
    advantages = ["Willpower"]


class _Exalt(_EXVSWODTemplate):
    advantages = ["Willpower", "Essence"]
    power_stat = "Essence"


class Solar(_Exalt):
    fields = ["Caste"]
    field_choices = {
        "Caste": ["Dawn", "Zenith", "Twilight", "Night", "Eclipse"]
    }
    field_defaults = {
        "Caste": "Dawn",
    }
    charm_categories = ["Dawn", "Zenith", "Twilight", "Night", "Eclipse", "Special"]


class DragonBlooded(_Exalt):
    name = "Dragon-Blooded"
    fields = ["Aspect"]
    field_choices = {
        "Aspect": ["Air", "Earth", "Fire", "Water", "Wood"]
    }
    field_defaults = {
        "Aspect": "Air",
    }
    charm_categories = ["Air", "Earth", "Fire", "Water", "Wood"]


class Lunar(_Exalt):
    fields = ["Caste", "Totem Animal"]
    field_choices = {
        "Caste": ["Full Moon", "Changing Moon", "No Moon"]
    }
    field_defaults = {
        "Caste": "Full Moon",
    }
    form_choices = ["Human", "Totem", "Animal", "Lord of Fangs", "Farstrider", "Scutterling", "Earthshaker", "Nightstalker",
                    "Beastman"]
    charm_categories = ["Full Moon", "Changing Moon", "No Moon", "Shapeshifting"]


class Sidereal(_Exalt):
    fields = ["Caste"]
    field_choices = {
        "Caste": ["Journeys", "Battles", "Secrets", "Endings", "Serenity"]
    }
    field_defaults = {
        "Caste": "Journeys",
    }
    charm_categories = ["Journeys", "Battles", "Secrets", "Endings", "Serenity"]


class Abyssal(_Exalt):
    fields = ["Caste"]
    field_choices = {
        "Caste": ["Dusk", "Midnight", "Daybreak", "Day", "Moonshadow"]
    }
    field_defaults = {
        "Caste": "Dusk",
    }
    charm_categories = ["Dusk", "Midnight", "Daybreak", "Day", "Moonshadow", "Special"]


class Infernal(_Exalt):
    fields = ["Crown"]
    field_choices = {
        "Crown": ["Eyes", "Flames", "Glory", "Kings", "Night"]
    }
    field_defaults = {
        "Crown": "Slayer",
    }
    charm_categories = ["Kakuri: The Night Realm", "Lanka: Demon City of the Rakshas",
                        "The Hell of Being Skinned Alive", "The Wicked City", "The Hell of Boiling Oil",
                        "The Hell of Burrowing Maggots"]


class Alchemical(_Exalt):
    fields = ["Caste"]
    field_choices = {
        "Caste": ["Orichalcum", "Moonsilver", "Jade", "Starmetal", "Soulsteel", "Adamant"]
    }
    field_defaults = {
        "Caste": "Orichalcum",
    }
    charm_categories = ["General", "Combat", "Physical Enhancement", "Social", "Stealth and Disguise",
                        "Analytic and Cognitive", "Utility", "Spiritual"]


class Liminal(_Exalt):
    fields = ["Aspect"]
    field_choices = ["Blood", "Breath", "Flesh", "Soil", "Marrow"]
    field_defaults = {
        "Aspect": "Blood",
    }
    charm_categories = ["Blood", "Breath", "Flesh", "Soil", "Marrow"]


class DragonKing(_Exalt):
    name = "Dragon King"
    fields = ["Breed"]
    field_choices = {
        "Breed": ["Pterok", "Raptok", "Anklok", "Mosok"]
    }
    charm_categories = ["Celestial Air", "Clear Air", "Solid Earth", "Yielding Earth", "Blazing Fire", "Flickering Fire",
                        "Flowing Water", "Shimmering Water", "Growing Wood", "Shaping Wood"]
