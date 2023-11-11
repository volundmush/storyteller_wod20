from django.conf import settings
from storyteller_wod20.templates import _WoD20Template


class _W20Template(_WoD20Template):
    pass


class Mortal(_W20Template):
    pass


class _Fera(_W20Template):
    power_stat = "Gnosis"
    advantages = ["Willpower", "Rank", "Rage", "Gnosis"]


class Ajaba(_Fera):
    fields = ["Breed", "Aspect"]
    field_choices = {
        "Breed": ["Homid", "Metis", "Hyaenid"],
        "Aspect": ["Dawn", "Midnight", "Dusk"]
    }
    field_defaults = {
        "Breed": "Homid",
        "Aspect": "Dawn"
    }
    form_choices = ["Homid", "Anthros", "Crinos", "Crocas", "Hyaenid"]
    renown_types = ["Ferocity", "Cunning", "Obligation"]


class Ananasi(_Fera):
    fields = ["Breed", "Aspect"]
    field_choices = {
        "Breed": ["Homid", "Arachnid"],
        "Aspect": ["Tenere", "Hatar", "Kumoti"]
    }
    field_defaults = {
        "Breed": "Homid",
        "Aspect": "Tenere"
    }
    form_choices = ["Homid", "Lilian", "Pithus", "Crawlerling"]
    renown_types = ["Cunning", "Obedience", "Wisdom"]


class Apis(_Fera):
    fields = ["Breed", "Auspice"]
    field_choices = {
        "Breed": ["Homid", "Bos"],
        "Auspice": ["Twilight", "Solar", "Lunar"]
    }
    form_choices = ["Homid", "Minotaur", "Aurochs"]


class Bastet(_Fera):
    fields = ["Breed", "Tribe", "Pyrio"]
    field_choices = {
        "Pyrio": ["Daylight", "Twilight", "Night"],
        "Breed": ["Homid", "Metis", "Feline"],
        "Tribe": ["Bagheera", "Balam", "Bubasti", "Ceilican", "Khan", "Pumonca", "Qualmi", "Simba", "Swara",
                  "Khara"]
    }
    field_defaults = {
        "Pyrio": "Daylight",
        "Breed": "Homid",
        "Tribe": "Bagheera"
    }
    form_choices = ["Homid", "Sokto", "Crinos", "Chatro", "Feline"]
    renown_types = ["Ferocity", "Cunning", "Honor"]


class Camazotz(_Fera):
    fields = ["Breed"]
    field_choices = {
        "Breed": ["Homid", "Chiroptera"]
    }
    form_choices = ["Homid", "Apterous", "Crinos", "Megachiroptera"]


class Corax(_Fera):
    fields = ["Breed", "Tribe"]
    field_choices = {
        "Breed": ["Homid", "Corvid"],
        "Tribe": ["Chasers", "Leshy", "Hermetic Order of Swift Light", "The Gulls of Battle", "The Morrigan",
                  "Murder's Daughters", "The Sun-Lost", "Tulugaq"]
    }
    field_Defaults = {
        "Breed": "Homid",
        "Tribe": "Chasers"
    }
    form_choices = ["Homid", "Crinos", "Corvid"]
    renown_types = ["Glory", "Honor", "Wisdom"]


class Garou(_Fera):
    fields = ["Breed", "Auspice", "Tribe"]
    field_choices = {
        "Breed": ["Homid", "Metis", "Lupus"],
        "Auspice": ["Ragabash", "Theurge", "Philodox", "Galliard", "Ahroun"],
    }
    field_defaults = {
        "Breed": "Homid",
        "Auspice": "Ragabash"
    }
    form_choices = ["Homid", "Glabro", "Crinos", "Hispo", "Lupus"]
    renown_types = ["Glory", "Honor", "Wisdom"]


class Grondr(_Fera):
    fields = ["Breed"]
    field_choices = {
        "Breed": ["Homid", "Metis", "Scrofa"]
    }
    form_choices = ["Homid", "Aperius", "Crinos", "Daeodon", "Scrofa"]


class Gurahl(_Fera):
    fields = ["Breed", "Tribe", "Auspice"]
    field_choices = {
        "Auspice": ["Arcas", "Uzmati", "Kojubat", "Kieh", "Rishi"],
        "Breed": ["Homid", "Ursine"],
        "Tribe": ["Forest Walkers", "Ice Stalkers", "Mountain Guardians", "River Keepers", "Okuma"]
    }
    field_defaults = {
        "Auspice": "Arcas",
        "Breed": "Homid",
        "Tribe": "Forest Walkers"
    }
    renown_types = ["Honor", "Succor", "Wisdom"]
    form_choices = ["Homid", "Arthren", "Crinos", "Bjornen", "Ursus"]


class Kitsune(_Fera):
    renown_types = ["Cunning", "Honor", "Glory"]
    fields = ["Breed", "Path"]
    field_choices = {
        "Breed": ["Kojin", "Roko", "Shinju"],
        "Path": ["Kataribe", "Gukutsushi", "Doshi", "Eji"]
    }
    field_defaults = {
        "Breed": "Kojin",
        "Path": "Kataribe"
    }
    form_choices = ["Hitogata", "Sambuhenge", "Koto", "Juko", "Kyubi"]


class Mokole(_Fera):
    fields = ["Breed", "Stream", "Auspice"]
    field_choices = {
        "Breed": ["Homid", "Suchid"],
        "Stream": ["Mokole-mbembe", "Gumagan", "Makara", "Zhong Lung", "Ao"],
        "Auspice": ["Rising Sun", "Noonday Sun", "Setting Sun", "Shrouded Sun", "Midnight Sun", "Decorated Suns",
                    "Solar Eclipse", "Hemanta", "Zarad", "Grisma", "Vasanta"]
    }
    field_defaults = {
        "Breed": "Homid",
        "Stream": "Mokole-mbembe",
        "Auspice": "Rising Sun"
    }
    form_choices = ["Homid", "Archid", "Suchid"]


class Nagah(_Fera):
    fields = ["Breed", "Auspice"]
    field_choices = {
        "Breed": ["Balaram", "Ahi", "Vasuki"],
        "Auspice": ["Kamakshi", "Kartikeya", "Kamsa", "Kali"]
    }
    field_defaults = {
        "Breed": "Balaram",
        "Auspice": "Kamakshi"
    }
    form_choices = ["Balaram", "Silkaram", "Azhi Dahaka", "Kali Dahaka", "Vasuki"]


class Nuwisha(_Fera):
    fields = ["Breed"]
    field_choices = {
        "Breed": ["Homid", "Latrani"],
    }
    renown_types = ["Glory", "Humor", "Wisdom"]
    form_choices = ["Homid", "Tsitsu", "Manabozho", "Sendeh", "Latrani"]


class Ratkin(_Fera):
    fields = ["Breed", "Aspect"]
    field_choices = {
        "Breed": ["Homid", "Metis", "Rodens"],
        "Aspect": ["Tunnel Runner", "Shadow Seer", "Knife Skulker", "Warrior", "Engineer", "Plague Lords",
                   "Munchmausen", "Twitchers", "Bard"]
    }
    renown_types = ["Infamy", "Cunning", "Obligation"]
    form_choices = ["Homid", "Crinos", "Rodens"]


class Rokea(_Fera):
    fields = ["Breed", "Auspice"]
    field_choices = {
        "Breed": ["Homid", "Squamus"],
        "Auspice": ["Brightwater", "Dimwater", "Darkwater"]
    }
    renown_types = ["Harmony", "Innovation", "Valor"]
    form_choices = ["Homid", "Glabrus", "Gladius", "Chasmus", "Squamus"]

