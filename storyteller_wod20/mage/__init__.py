from storyteller_wod20.base import WoD20


class M20(WoD20):
    def __init__(self, alias: str, name: str, key: str = None):
        super().__init__(alias, name, key=key)
        self.setup_templates("storyteller_wod20.mage.templates")
        self.setup_handlers("storyteller_wod20.mage.handlers")
        self.talents_abilities = [
            "Alertness",
            "Art",
            "Athletics",
            "Awareness",
            "Brawl",
            "Empathy",
            "Expression",
            "Intimidation",
            "Leadership",
            "Streetwise",
            "Subterfuge",
        ]
        self.skills_abilities = [
            "Crafts",
            "Drive",
            "Etiquette",
            "Firearms",
            "Martial Arts",
            "Meditation",
            "Melee",
            "Research",
            "Stealth",
            "Survival",
            "Technology",
        ]
        self.knowledges_abilities = [
            "Academics",
            "Computer",
            "Cosmology",
            "Enigmas",
            "Esoterica",
            "Investigation",
            "Law",
            "Medicine",
            "Occult",
            "Politics",
            "Science",
        ]
