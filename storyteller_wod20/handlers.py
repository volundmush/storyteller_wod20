from storyteller.handlers import TemplateHandler as _TemplateHandler, FieldHandler as _FieldHandler
from storyteller.handlers import StatHandler as _StatHandler


class TemplateHandler(_TemplateHandler):
    pass


class FieldHandler(_FieldHandler):
    pass


class AttributeHandler(_StatHandler):
    name = "Attributes"
    stat_category = "Attributes"

    def get_choices(self) -> list[str]:
        return self.game.attributes


class AdvantageHandler(_StatHandler):
    name = "Advantages"
    stat_category = "Advantages"

    def get_choices(self) -> list[str]:
        return getattr(self.template(), "advantages", list())


class AbilityHandler(_StatHandler):
    name = "Abilities"
    stat_category = "Abilities"

    def get_choices(self) -> list[str]:
        return self.game.abilities


class BackgroundHandler(_StatHandler):
    name = "Backgrounds"
    stat_category = "Backgrounds"
    dynamic_choices = True
    use_context = True


class MeritHandler(_StatHandler):
    name = "Merits"
    stat_category = "Merits"
    dynamic_choices = True
    use_context = True


class FlawHandler(_StatHandler):
    name = "Flaws"
    stat_category = "Flaws"
    dynamic_choices = True
    use_context = True
