from evennia.utils.utils import callables_from_module
from storyteller_wod20.base import WoD20


class C20(WoD20):

    def __init__(self, alias: str, name: str, key: str = None):
        super().__init__(alias, name, key=key)
        self.setup_templates("storyteller_wod20.changeling.templates")
        self.setup_handlers("storyteller_wod20.changeling.handlers")