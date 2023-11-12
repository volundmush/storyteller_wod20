from storyteller.handlers import PowerHandler as _PowerHandler


class CharmHandler(_PowerHandler):
    family = "Charms"
    singular_name = "Charm"
    dynamic_category = True

    def modify_path(self, path: list[str]):
        if len(path) == 1:
            path.insert(0, self.template().name)

    def get_subcategory_choices(self, operation, category: str):
        return self.template().charm_categories

    def at_template_change(self):
        self.clear()
