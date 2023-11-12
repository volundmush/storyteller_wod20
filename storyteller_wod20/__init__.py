def init(settings, plugins):
    settings.STORYTELLER_GAMES["V20"] = (
        "storyteller_wod20.vampire.V20",
        "Vampire: The Masquerade 20th Anniversary Edition",
        "V20",
    )
    settings.STORYTELLER_GAMES["W20"] = (
        "storyteller_wod20.werewolf.W20",
        "Werewolf: The Apocalypse 20th Anniversary Edition",
        "W20",
    )
    settings.STORYTELLER_GAMES["M20"] = (
        "storyteller_wod20.mage.M20",
        "Mage: The Ascension 20th Anniversary Edition",
        "M20",
    )
    settings.STORYTELLER_GAMES["C20"] = (
        "storyteller_wod20.changeling.C20",
        "Changeling: The Dreaming 20th Anniversary Edition",
        "C20",
    )

    settings.STORYTELLER_DEFAULT_GAME = "V20"
