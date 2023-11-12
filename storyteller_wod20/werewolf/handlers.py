from storyteller.handlers import PowerHandler as _PowerHandler


class GiftHandler(_PowerHandler):
    """
    Werewolf Gifts are weird.

    ("Gifts", "Ragabash", "1", "Open Seal")

    """

    family = "Gifts"
    singular_name = "Gift"
    dynamic_category = True
    subcategories = [str(x) for x in range(1, 11)]

    def get_subcategory_choices(self, operation, category: str):
        return self.subcategories

    def at_template_change(self):
        self.clear()

    def render_subcategory(self, category, subcategory, plural=True):
        return f"|c{category} Level {subcategory} {self.plural_name if plural else self.singular_name}|n"
