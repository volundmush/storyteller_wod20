from evennia.utils.utils import lazy_property
from storyteller.base import Game


class WoD20(Game):
    def __init__(self, alias: str, name: str, key: str = None):
        super().__init__(alias, name, key=key)
        self.setup_handlers("storyteller_wod20.handlers")
        self.talents_abilities = list()
        self.skills_abilities = list()
        self.knowledges_abilities = list()
        self.physical_attributes = ["Strength", "Dexterity", "Stamina"]
        self.social_attributes = ["Charisma", "Manipulation", "Appearance"]
        self.mental_attributes = ["Perception", "Intelligence", "Wits"]

    @lazy_property
    def abilities(self):
        return (
            self.talents_abilities + self.skills_abilities + self.knowledges_abilities
        )

    @lazy_property
    def attributes(self):
        return (
            self.physical_attributes + self.social_attributes + self.mental_attributes
        )
