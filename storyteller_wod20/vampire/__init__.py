from evennia.utils.utils import callables_from_module
from storyteller_wod20.base import WoD20


class V20(WoD20):

    def __init__(self, alias: str, name: str, key: str = None):
        super().__init__(alias, name, key=key)
        self.setup_templates("storyteller_wod20.vampire.templates")
        self.setup_handlers("storyteller_wod20.vampire.handlers")
        self.talents = ["Alertness", "Athletics", "Awareness", "Brawl", "Empathy", "Expression", "Intimidation",
                        "Leadership",
                        "Streetwise", "Subterfuge"]
        self.skills = ["Animal Ken", "Crafts", "Drive", "Etiquette", "Firearms", "Larceny", "Melee", "Performance",
                       "Stealth",
                       "Survival"]
        self.knowledges = ["Academics", "Computer", "Finance", "Investigation", "Law", "Medicine", "Occult", "Politics",
                           "Science", "Technology"]
