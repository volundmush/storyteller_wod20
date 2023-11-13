from storyteller.handlers import (
    TemplateHandler as _TemplateHandler,
    FieldHandler as _FieldHandler,
)
from storyteller.handlers import (
    AttributeHandler as _AttributeHandler,
    AbilityHandler as _AbilityHandler,
)
from storyteller.handlers import (
    AdvantageHandler as _AdvantageHandler,
    MeritHandler as _MeritHandler,
)
from storyteller.handlers import (
    FlawHandler as _FlawHandler,
    BackgroundHandler as _BackgroundHandler,
)

from storyteller.handlers import (
    FooterHandler as _FooterHandler,
    PoolHandler as _PoolHandler,
)


class TemplateHandler(_TemplateHandler):
    pass


class FieldHandler(_FieldHandler):
    pass


class AttributeHandler(_AttributeHandler):
    pass


class AdvantageHandler(_AdvantageHandler):
    pass


class AbilityHandler(_AbilityHandler):
    def render_sheet(self, viewer, width: int, lines):
        self.render_sheet_tri_categories(
            viewer,
            width,
            lines,
            ["talents", "skills", "knowledges"],
            "abilities",
            name_category=False,
        )


class BackgroundHandler(_BackgroundHandler):
    pass


class MeritHandler(_MeritHandler):
    pass


class FlawHandler(_FlawHandler):
    pass


class FooterHandler(_FooterHandler):
    pass


class PoolHandler(_PoolHandler):
    pass
