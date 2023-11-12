from storyteller.handlers import StatHandler as _StatHandler


class DisciplineHandler(_StatHandler):
    stat_category = "Disciplines"
    remove_zero = True
    singular_name = "Discipline"

    def get_choices(self):
        return getattr(self.game, "vampire_disciplines", list())

    def at_template_change(self):
        self.clear()
