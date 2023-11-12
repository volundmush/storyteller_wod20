from storyteller_wod20.base import WoD20


class W20(WoD20):
    def __init__(self, alias: str, name: str, key: str = None):
        super().__init__(alias, name, key=key)
        self.setup_templates("storyteller_wod20.werewolf.templates")
        self.setup_handlers("storyteller_wod20.werewolf.handlers")
        self.talents_abilities = [
            "Alertness",
            "Athletics",
            "Brawl",
            "Empathy",
            "Expression",
            "Leadership",
            "Intimidation",
            "Primal-Urge",
            "Streetwise",
            "Subterfuge",
        ]
        self.skills_abilities = [
            "Animal-Ken",
            "Crafts",
            "Drive",
            "Etiquette",
            "Firearms",
            "Larceny",
            "Melee",
            "Performance",
            "Stealth",
            "Survival",
        ]
        self.knowledges_abilities = [
            "Academics",
            "Computer",
            "Enigmas",
            "Investigation",
            "Law",
            "Medicine",
            "Occult",
            "Rituals",
            "Science",
            "Technology",
        ]
