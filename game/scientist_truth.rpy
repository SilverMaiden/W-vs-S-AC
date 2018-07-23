label scientist_truth:
    "You lean in, looking around Juicebox and making sure no one is listening. "

    p "The High Scientist told me that he wants to investigate a murder in Houdin."

    "Ash and Rosemary stare at you in shock."

    rosemary "You’re going to Wizard territory? %(player_name)s, are you crazy?"

    ash "Is he forcing you to take the job? This could be really dangerous %(player_name)s. You went on the frontlines once. You saw what they did…"

    menu:
        ""
        "We need to keep the peace":
            p "That’s why I need to go. He wants us to help them so we can keep peace with them. For progress."
            "Rosemary nods."
            rosemary "Progress is key. Just like the council says."
            ash "%(player_name)s, promise me you'll be careful."
            $ ash_fp += 1

            menu:
                ""
                "Bah, I'm always careful":
                    p " Come on guys, you know me! I’m always careful."
                    "Ash smiles."
                    ash "Always the careful one."
                    rosemary "Sometimes it’s good to be reckless, %(player_name)s. Don’t let your cautious nature prevent progress."

                "Won't make any promises":
                    p "I'm not going to make any promises."
                    "Ash sighs and smiles."
                    ash "That's our %(player_name)s."
                    "Rosemary giggles."
                    rosemary "This is exactly why he assigned you to this."
                    $ rosemary_fp += 1
        
        "He's making me go...":
            p "I mean, he’s forcing me to do the job, but it’s not like I have any other choice. If I don’t accept the work he’s less likely to send me on assignments… Also, progress won’t be made."
            rosemary "That would be a shame."
            ash "You'll be careful, right?"

            menu:
                ""
                "I'll do what I have to":
                    "You shrug."
                    p "Depends on what I have to do, I suppose. Hopefully the Wizards won’t kill me."
                    "Ash frowns."
                    ash "Come on %(player_name)s, don't say stuff like that!"
                    rosemary "Well, at least they're trying to be realistic..."
                "Of course":
                    "You smile."
                    p "Of course I will be."
                    ash "That's good."
                    rosemary "Be realistic %(player_name)s, you might not be able to avoid the trouble."
                    p "Don't make me think about it."

    jump after_convo
