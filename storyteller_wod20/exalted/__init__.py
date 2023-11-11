"""
This module contains data for Exalted vs World of Darkness, an unofficial add-on by Holden Shearer which uses
WoD20 as a base.
"""

from storyteller_wod20.base import WoD20


class EXVSWOD(WoD20):

    def __init__(self, alias: str, name: str, key: str = None):
        super().__init__(alias, name, key=key)
        self.setup_templates("storyteller_wod20.exalted.templates")
        self.setup_handlers("storyteller_wod20.exalted.handlers")
        self.talents = ["Alertness", "Athletics", "Awareness", "Brawl", "Empathy", "Expression", "Intimidation", "Leadership",
               "Streetwise", "Subterfuge"]
        self.skills = ["Animal-Ken", "Crafts", "Drive", "Etiquette", "Firearms", "Larceny", "Melee", "Performance", "Stealth",
                "Survival"]
        self.knowledges = ["Academics", "Computer", "Finance", "Investigation", "Law", "Medicine", "Occult", "Politics", "Science",
                  "Technology"]