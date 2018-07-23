label scientist_classified:
    p "It’s classified information, I couldn’t tell you if I wanted to."
    ash "Come on, tell us!"
    "You lean back in your chair, but remain quiet. Ash stares at you in dismay."
    rosemary "We tell you about our assignments all the time %(player_name)s. It’s only fair you tell us about this one."
    p "Not this time."
    $ ash_fp -= 1
    $ rosemary_fp -= 1

    jump after_convo
