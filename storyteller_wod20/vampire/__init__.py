from storyteller_wod20.base import WoD20


class V20(WoD20):
    def __init__(self, alias: str, name: str, key: str = None):
        super().__init__(alias, name, key=key)
        self.setup_templates("storyteller_wod20.vampire.templates")
        self.setup_handlers("storyteller_wod20.vampire.handlers")
        self.talents_abilities = [
            "Alertness",
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
            "Animal Ken",
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
            "Finance",
            "Investigation",
            "Law",
            "Medicine",
            "Occult",
            "Politics",
            "Science",
            "Technology",
        ]

        self.vampire_disciplines = (
            "Animalism",
            "Assamite Sorcery",
            "Auspex",
            "Bardo",
            "Celerity",
            "Chimerstry",
            "Daimoinon",
            "Dementation",
            "Dominate",
            "Flight",
            "Fortitude",
            "Koldunic Sorcery",
            "Melpominee",
            "Mytherceria",
            "Necromancy",
            "Obeah",
            "Obfuscate",
            "Obtenebration",
            "Ogham",
            "Potence",
            "Presence",
            "Protean",
            "Quietus",
            "Sanguinis",
            "Spiritus",
            "Serpentis",
            "Temporis",
            "Thanatosis",
            "Thaumaturgy",
            "Valeren",
            "Vicissitude",
            "Visceratika",
        )
