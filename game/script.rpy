# You can place the script of your game in this file.
init python:
    config.developer=True   
    config.debug_sound = True
    config.default_text_cps = 2
    #config.main_menu_music = "main-screen-menu.mp3"
        
init:
    $on_screen = Position(xpos = 0.5, xanchor=0.5, ypos=0.65, yanchor=0.5)
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image main_menu_new:
    "World.png"
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    rotate 0
    linear 15.0 rotate 360
    repeat
image main_menu_sm:
    "sunandmoon.png"
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    rotate 0
    linear 15.0 rotate -360
    repeat






image main_menu_bg = im.Scale("background.png", 1280, 720)
image main_menu = "main_menu.png"
image main_menu_past = im.MatrixColor("main_menu.png", im.matrix.desaturate())
image faction_selection = "faction_selection.png"
image character_selection = im.Scale("character-selection.png", 800, 600)
image character_selection_wizards = im.Scale("character_selection_wizards.png", 800, 600)
image intro_scene = "war-city.png"
image good_ending = im.Scale("good-ending.jpg", 800, 600)
image player_scientist = (im.Scale("player_scientist.png", 500, 600))
image player_scientist_pearl = (im.Scale("pearl.png", 500, 600))
image player_scientist_skylar = (im.Scale("skylar.png", 500, 600))
image player_scientist_selection = im.Scale("selection-player-scientist.png", 200, 250)
image player_scientist_femm = im.Alpha((im.Scale("player-scientist-femm.png", 470, 440)), 0.8)
image player_scientist_femm_selection = im.Scale("player-scientist-femm.png", 200, 250)
image player_wizard_pearl = im.Scale("pearl_wizard.png", 500, 600)
image people_monster = im.Scale("People-monster1.png", 750, 900)
image player_wizard_connie = im.Scale("connie.png", 500, 600)
image high_scientist_lab = "high_scientist_office.png"
image high_scientist_lab_past = im.MatrixColor("high_scientist_office.png", im.matrix.desaturate())
image high_wizard_office = im.Scale("high_wizard_office.png", 800, 600)
image wizard_bedroom = "wizard_bedroom.png"
image wizard_bedroom_night = "wizard_bedroom_night.png"
image dream_rose_garden = "rose-dream-1.png"
image bad_dream_rose_garden = "rose-dream-2.png"
image dark_bad_dream_rose_garden = "rose-dream-3.png"
image final_rose_garden = "rose-dream-4.png"
image blood_splatter = im.Scale("blood_splatter.png", 800, 600)
image blood_splatter_dark = im.Scale("blood_splatter_dark.png", 800, 600)
image cave_outside_dream = "cave-dream-1.png"
image cave_inside_dream = "cave-dream-2.png"
image cave_inside_dark_dream = "cave-dream-3.png"
image castle_hallway = im.Scale("castle_hallway.jpg", 800, 600)
image dream_lab = im.Scale("dream_lab.png", 800, 600)
image dream_forest = im.Scale("dream_forest.jpg", 800, 600)
image dream_forest_1 = im.Scale("dream-forest-1.png", 800, 600)
image train_station = im.Scale("train_station.jpg", 800, 600)
image train_inside = im.Scale("train-inside.jpg", 800, 600)
image wizard_train_station = im.Scale("wizard_train_station.png", 800, 600)
image outside_window = im.Scale("outside_window.jpg", 800, 600)
image past_high_wizard_office = im.Scale("High Wizard Office Past.png", 800, 600)
image ghost = im.Scale("ghost.png", 570, 630)
image alan = im.Scale("alan.png", 500, 600)
image ladis = im.Scale("ladis.png", 500, 600)
image lorna = im.Scale("lorna.png", 500, 600)
image medea = im.Scale("medea.png", 500, 600)
image freya = im.Scale("freya.png", 500, 600)
image high_wizard = im.Scale("high_wizard.png", 400, 600)
image thorns1 = "thorns1.png"
image thorns2 = "thorns2.png"
image black = "pureblack.png"
image music_credits = im.Scale("music_credits.png", 800, 600)
image demo_end_screen = im.Scale("demo_end_screen.png", 800, 600)
image juice_bar = ("juicebox.png")
image dwale_bottle = "dwale_bottle.png"
image dwale_bottle_night = im.Scale("dwale_bottle_night.png", 400,450)
image rosemary_pillow = im.Scale("rosemary_pillow.png", 500, 350)
image juicebox = "juice_box.png"
image ash = "ash.png"
image rosemary = "rosemary.png"
image titlecard = "titlecard.png"
image endcard = "endcard.png"



#image high_scientist = im.Scale("high-scientist-1-b.png", 300, 300)



# Declare characters used by this game.
define c = Character("Carlos", color="#710E66", image = "carlos", window_left_padding=250)
define ghost = Character('???', color="#000000", image = "ghost", window_left_padding=250)
define ghost_nopic = Character('???', color="#000000", window_left_padding=250)
define peoplemonster = Character("???", color="#128A00", image = "people_monster", window_left_padding=270)
define e = Character('High Scientist', color="#c8ffc8", image = "high-scientist", window_left_padding=280)
define h_w = Character('High Wizard', color="c8ffc8", image = "h_w", window_left_padding = 300)
define j = DynamicCharacter("Jax", color="#FF0080", image = "jax", window_left_padding = 350)
define Garnet = DynamicCharacter("player_name", color="#c8ffc8", image = "player_scientist", window_left_padding=200)
define Moira = DynamicCharacter("player_name", color="#c8ffc8", image = "player_scientist_femm", window_left_padding=250)
define pearl_scientist = DynamicCharacter("player_name", color="#c8ffc8", image = "player_scientist_pearl", window_left_padding=220)
define skylar_playable = DynamicCharacter("player_name", color="#0489B1", image = "player_scientist_skylar", window_left_padding=220)
define skylar = Character("Skylar", color="#0489B1", image = "player_scientist_skylar", window_left_padding=270)
define pearl_wizard = DynamicCharacter("player_name", color="#c8ffc8", image = "player_wizard_pearl", window_left_padding=260)
define connie_wizard = DynamicCharacter("player_name", color="#A901DB", image = "player_wizard_connie", window_left_padding=300)
define alan = Character("Alan", color="#B43104", image = "alan", window_left_padding =250)
define ladis = Character("Ladis", color= "#2ECCFA", image = "ladis", window_left_padding = 250)
define ash = Character("Ash", color= "#2ECCFA", image = "ash", window_left_padding = 250)
define rosemary = Character("Rosemary", color= "#c8ffc8", image = "rosemary", window_left_padding = 250)
define lorna = Character("Lorna", color= "#c8ffc8", image = "lorna", window_left_padding = 250)
define medea = Character("Medea", color= "#0489B1", image = "medea", window_left_padding = 250)
define freya = DynamicCharacter("Freya", color="#0B0B61", image = "freya", window_left_padding=220)

image side high-scientist = im.Scale("side-high-scientist.png", 300, 300)
image side high-scientist normal = im.Scale("side-high-scientist.png", 300, 300)
image side high-scientist past = im.MatrixColor(im.Scale("side-high-scientist.png", 300, 300), im.matrix.desaturate())

image side h_w past = im.MatrixColor(im.Scale("side-high-wizard.png", 310, 280), im.matrix.desaturate())
image side h_w normal = im.Scale("side-high-wizard.png", 310, 280)
image side h_w = im.Scale("side-high-wizard.png", 310, 280)
image side h_w love = im.Scale("side-high-wizard-love.png", 330, 370)
image side h_w angry = im.Scale("side-high-wizard-angry.png", 270, 300)
image side player_scientist = im.Scale("side-player-scientist.png", 210, 260)
image side player_scientist_femm = im.Scale("side-player-scientist-femm.png", 200, 250)
image side player_scientist_pearl = im.Scale("side-pearl-scientist.png", 240, 290)
image side player_scientist_skylar = im.Scale("side-skylar-scientist.png", 225, 280)
image side skylar = im.Scale("side-skylar-scientist.png", 200, 250)
image side player_wizard_pearl = im.Scale("side-pearl-wizard.png", 250, 330)
image side player_wizard_connie = im.Scale("side-connie-wizard.png", 250, 300)
image side ghost = im.Alpha((im.Scale("side-ghost.png", 220, 250)), 0.8)
image side people_monster = im.Scale("side-people-monster.png", 280, 250)
image side carlos = im.Scale("side-carlos.png", 230, 250)
image side jax = im.Scale("side-jax.png", 350, 270)
image side alan = im.Scale("side-alan.png", 276, 340)
image side ladis = im.Scale("side-ladis.png", 240, 260)
image side ash = im.Scale("side-ash.png", 280, 270)
image side rosemary = im.Scale("side-rosemary.png", 240, 290)
image side lorna = im.Scale("side-lorna.png", 230, 250)
image side medea = im.Scale("side-medea.png", 240, 260)
image side freya = im.Scale("side-freya-normal.png", 220, 280)
image side freya normal = im.Scale("side-freya-normal.png", 225, 282)
image side freya grin = im.Scale("side-freya-grin.png", 220, 280)
image side freya angry = im.Scale("side-freya-angry.png", 220, 280)
image side freya surprise = im.Scale("side-freya-surprise.png", 225, 280)

#image side high_scientist = "high-scientist-1-b.png"


screen factions:
    imagemap:
        ground "faction_selection_ground.png"
        hover "faction_selection_hover.png"

        hotspot (655, 0, 655, 720) clicked Return("scientists")
        hotspot (0, 0, 655, 720) clicked Return("wizards")


screen wizard_selection:
    imagemap:
        ground "wizard_selection_ground.png"
        hover "wizard_selection_hover.png"


        hotspot (284, 291, 357, 395) clicked Return("connie")
        hotspot (712, 246, 290, 440) clicked Return("pearl")

screen scientist_selection:
    imagemap:
        ground "1-scientist_selection_ground.png"
        hover "1-scientist_selection_hover.png"


        hotspot (346, 329, 235, 329) clicked Return("skylar")
        hotspot (752, 349, 244, 323) clicked Return("pearl")


label splashscreen:
    scene black
    with Pause(1)
    
    
    show main_menu_past with dissolve
    with Pause(2)
    
    scene black with dissolve
    with Pause(1)
    
    return

# The game starts here.
label start:
    
    $ romance_points = 0
    $ mystery_points = 0
    #hs_fp = high scientist friendship points
    $ hw_fp = 0
    $ hs_fp = 0
    $ c_fp = 0
    $ j_fp = 0
    $ alan_fp = 0
    $ ladis_fp = 0
    $ lorna_fp = 0
    $ medea_fp = 0
    $ freya_fp = 0
    $ skylar_fp = 0
    $ ash_fp = 0
    $ rosemary_fp = 0
    $ Jax = "???"
    $ Freya ="???"
  #  show faction_selection
#with fade

    #$ faction = renpy.imagemap("faction_selection_ground.png", "faction_selection_hover.png", [
     #                           (655,2,621,715, "scientists"),
      #                          (0,0,655,720, "wizards"),
       #                         ])




   # while faction not in ["wizard", "wizards", "Wizard", "Wizards", "scientist", "scientists", "Scientist", "Scientists"]:
    #    $ faction = renpy.input("Wizard or Scientist? Choose your faction. (Please enter the name of your faction.)")
    show faction_selection
    with fade
    "Choose your faction:"
    call screen factions

    $ faction = _return
    
    if faction == "wizards":
        call screen wizard_selection
        
        $ identity = _return
        # $ identity = identity.strip()
        
        
        if identity == "Connie" or identity == "connie":
            $ p = connie_wizard
        
        if identity == "Pearl" or identity == "pearl":
            $ p = pearl_wizard
        

    
        stop music fadeout 2.0
        play music "opening_narration.mp3"
        
                
        scene main_menu_past
        with fade
        
        $ player_name = "Garnet"
        
        h_w "I'd been the head of the wizard council for what seemed like nearly a century when the incidents occurred."
        
        h_w "It was a few years after the war, one of the council members, Merlin the 17th, had been murdered under quite mysterious circumstances."
        
        h_w "I had discussed what to do with my fellow council members and none of us could figure out what caused his murder. My first theory was that it was not magic, but that it was something mortal."
        
        h_w " I decided to send word of what had happened to the High Scientist in Copernica, and I had received a response."
        
        scene high_scientist_lab_past
        with fade
        
        e past "'I'll send one of my scientists immediately. I would like to prevent any conflict.'"
        
        h_w "Of course they wanted to prevent conflict, they were weak. If another war broke out the wizards would surely win."
        
        h_w "I had decided that the only way to quell any conflict this might cause before it began was to make sure that one of my wizards to accompany the scientist at all times."
        
        h_w "I flipped through the suggestions the council had given me, and found a number of excellent candidates. Alan Stumbledork, Ladis of Glass, Medea the 22nd, Lorna Black, Gandirk the Off-White, and…"
        
        h_w "Oh, who might this one be?"
        
        $ player_name = renpy.input("What is your name?")
        
        $ player_name = player_name.strip()
        $ player_name = player_name.capitalize()
        
        if player_name == "":
            $ player_name="Garnet"
            
            
        h_w "Ah yes, %(player_name)s."
        scene black
        with fade
        h_w "I think they’ll do just fine."

        scene titlecard
        with Dissolve(2.0)
        $ renpy.pause(5.0)
        stop music fadeout 4.0
        
        scene wizard_bedroom_night
        with Dissolve(3.0)
        play music "castle_night.mp3"
        
        "You are having some trouble sleeping that night. The full moon is shining through the stain glass window, the rainbow light cascading around your room and reflecting off dust particles in a way that made them glitter like a million fireflies."
        
        "You open your eyes out of frustration and growl at your surroundings. The High Wizard wants you awake by dawn’s first light, not only so you can get to the train station on time to pick up the pesky scientist, but also so you can wake up Alan as well."
        
        "Why they wanted Alan of all wizards to join you was beyond your comprehension. All you know is that you need to fall asleep fast or you’re going to have to stay up all night."
        
        "To your left, your pillow of rosemary rests on your bedside table, while to your right your bottle of Dwale rests on the counter."
        
        menu:
            ""
            "Use rosemary pillow":
                jump dream_rosemary
            
            "Get up and take Dwale.":
                jump dream_dwale
        
        
        label after_dreams:
            stop music fadeout 1.0
            scene endcard
            with Dissolve(2.0)
            $ renpy.pause(10.0)
            "Go to main menu ->"

        return
            


        label after_menu:
            stop music fadeout 2.0
            scene wizard_bedroom
            with dissolve
            "You wake up with a start, air filling your lungs as your hand grips at your chest. A cold sweat dripping down your brow and your heart beats fast."
            play sound "whispers.mp3"
            "It was all a dream, it had to be a dream. A final whisper echoed through your mind as you become fully awake."
            if dream == "rosemary":
                "“We will all be one.”"
            if dream == "dwale":
                "“You killed us...”"
            stop sound fadeout 3.0
            play music "castle_night.mp3"
            "You proceed to get ready, trying to ignore the lingering thoughts of your nightmarish dreams. Once your cloak is on, you leave your room and head down the hallway of the castle."
            scene castle_hallway
            with dissolve
            "The castle you live is called Eastend, which lies on the eastern most point of Wardenburrough."
            "It’s an older castle, but the architecture is lovely, and the room you live in is large enough to accommodate all of your belongings."
            "Alan lives down the hall, his chambers located right next to a set of stairs that lead up to one of the castle’s many watchtowers. His door is made of a thin wood, which suits his personality quite well—he’s weak willed and can be broken down quite easily."
            "You listen closely at his door, the eerie silence must mean that he has yet to actually wake up."
            play sound "knock-knock.mp3"
            "With a sigh, you knock on his door loudly."
            p "Hello?"
            alan "Eep!"
            "Something falls down in the room, his door remaining closed."
            #show alan
            menu:
                ""
                "Are you okay?":
                    p "Uh Alan, are you okay in there?"
                    alan "I’m fine! I’m just peachy! Uh… Oh crap! It’s already 6:00!"
                    alan "I really wanted to take a shower, darn… I’ll try to be out in a minute!"
                "Get up, you git!":
                    p "Get up, you git! It's time to go."
                    alan "I’m up, I’m up! Jeez, %(player_name)s, what climbed into your ear this morning?"
                    $alan_fp -= 1
                    p "It’s already 6:00, we’re going to be late if you keep this up!"
        label after_menu:
            "Typical Alan Stumbledork."
            "After five minutes Alan opens his door and you see exactly what you would expect."
            "Alan, looking very disheveled and with a bandage on his cheek and tissues in his nose."
            "He must have really hurt himself getting out of bed this morning."
            menu:
                ""
                "(kind) Are you alright?":
                    "You give him a sympathetic look."
                    p "Are you alright? That looks like it hurts."
                    alan "Not really, but I’ll be okay. Always am."
                    "With a light sigh you pull out your stone wand and wave it in front of his nose, at the end of the motion you touch the tip of your wand to his cheek."
                    "He winces, then blink."
                    alan "You fixed my nose."
                    $ alan_fp += 1
                    "You give him a warm smile."
                    p "You're welcome."
                "(cold) You've looked better.":
                    p "Well, you've definitely looked better."
                    "Alan glares at you miserably."
                    alan "So have you."
                    "He wipes his nose and sniffles."
                    p "Are you really going to cry now? Wow."
                    "Alan straightens up indignantly."
                    alan "No, I'm not!"
                    "He wipes his entire face on one of his long billowy sleeves, snot and “manly” tears staining the cloth."
                    "You roll your eyes."
                    p "Oh, for Merlin’s sake have some dignity."
                    "You wave your stone wand in front of his face irritably and jab his nose with it."
                    alan "Hey-ouch!"
                    $ alan_fp -= 1
                    p "Right. Now that's fixed, let's get to the train station."
        label after_menu:
            play music "wizard-train-station.mp3"
            scene wizard_train_station
            with fade
        "The train station smells like cotton candy, but with a lingering odor of old cheese. The usual dust that circulates through the air is about half as much as usual, which is very strange to you. Despite the intense scents, the air is a bit easier to breath, which was oddly refreshing. It’s 7:44, which means the train will be arriving in around fifteen minutes."
        "Alan is trying to contain his excitement, but was doing a rather poor job of it. You on the other hand aren't that excited. In fact, you couldn’t care less. You fought against scientists during the war, they weren’t all the council made them out to be."
        "You pull out your trusty magic mirror, checking to see if anyone you may like is nearby. You only see Medea, Ladis and Lorna."
        "They must all be having breakfast together."
        menu:
            ""
            "Contact Ladis of Glass":
                p "Mirror, mirror, oh looking glass, let me speak to Ladis of, well...Glass."
                "Rhyming magic isn't your forte."
                "Ladis appears on the mirror a few moments later, her white hair slightly tousled and ice crystals forming on her eyelashes. She doesn’t look very pleased to see your face. "
                ladis "It's not even noon, %(player_name)s, what do you want?"
                menu:
                    ""
                    "I was just wondering if you were near the train station.":
                        p "Sorry, I was just wondering if you were in the area!"
                        "You see Ladis roll her eyes through the screen."
                        ladis "Literally, don’t even talk to me. I am so tired and this summer heat is killing my magic right now. Do you see my hair right now? I’m actively considering freezing myself right now."
                        "You go slightly red from embarrassment."
                        p "Oh, I'm really sorry. I hope you feel better."
                        $ ladis_fp -= 1
                        ladis "Whatever, bye."
                    "(tease) Sleepy, princess?":
                        p "Aww, are you sleepy princess?"
                        ladis "Obviously. My magic sucks right now, I HATE summer. I hate this heat, I just need to snuggle a snowman or something."
                        p "Or you need someone as cold hearted as you."
                        "You snicker as she rolls her eyes, but gives you a slight hint at a smile.."
                        ladis "Haha, very funny, you. If you find a spell that’ll allow me to become a cold blooded creature, tell me. I can’t stand being this warm."
                        p "you'll be the first to know. See ya."
                        $ ladis_fp += 1
                        ladis "Later, your majesty."
            "Contact Lorna Black.":
                p "Mirror, mirror, despite this...crack, let me speak to Lorna Black!"
                "That’s probably the first time that you used rhyming magic well."
                p "(That wasn't half bad! Score one to %(player_name)s.)"
                "Lorna answers immediately. She appears to have been doing some magic that ended poorly, a fresh band-aid sitting on her nose. She sighs."
                lorna "Hello, %(player_name)s."
                menu:
                    ""
                    "Are you alright?":
                        p "Are you doing ok? I was just checking to see if you’re anywhere near the train station."
                        "Lorna sighs again."
                        lorna "No, I’m in the castle. Thanks for checking on me though."
                        "She attempts to give you a smile, but it's as if she's forgotten how."
                        p "No problem, Lorna. Hey, if anything isn’t going well you know you can talk to me."
                        lorna "Mhmm, sure. Bye."
                    "Nice nose.":
                        "You can't help but smirk at the sight of Lorna's nose."
                        p "Nice nose. Are you near the train station?"
                        "Lorna rolls her eyes heavily."
                        $ lorna_fp -= 1
                        lorna "No, I'm in the castle. Bye."

            "Contact Medea the 22nd.":
                p "Mirror, mirror, through my, er, contact galleria...? Let me speak to Medea."
                "Having to rhyme in order for the mirror to work often makes really strange sounding spells."
                p "(That. Was. Terrible. I need to practice rhyming magic more...)"
                "Medea is happily eating a piece of toast and looks like a sparking ball of sunshine."
                menu:
                    ""
                    "Are you near the train station?":
                        p "Hey Medea, you wouldn't happen to be near the train station would you?"
                        medea "No, but I see you and Alan are at the train station."
                        "Alan peers over and waves."
                        alan "Hi Medea! I love you!"
                        "In his excitement, he crashes into a bystander."
                        alan "Ah!"
                        freya angry "Hey-!"
                        "The magic compact the bystander was holding hits the ground and shatters."
                        freya angry "..."
                        alan "*Gulp*"
                        p "(Uh oh.)"
                        menu:
                            ""
                            "Let Alan deal with it.":
                                "You sigh, turning away."
                                "On your compact, Medea looks up from her toast and raises an eyebrow."
                                p "What? He can take care of it himself."
                                "Medea shakes her head and laughs. It sounds fake."
                                "In the background, you hear Alan yelp loudly."
                                medea "Haha, he’s a riot, isn’t he?"
                                p "Yeah sure… I guess I’ll see you later."
                                medea "Can’t wait to meet that scientist, I hope they’re lovely!"
                            "Intervene":
                                p "Uh, sorry Medea, give me a sec-"
                                "You rush over to Alan, turning to face the bystander."
                                p "I'm so sorry about my friend, he didn't mean to bump into you like that."
                                freya angry "Yeah, well your 'friend' should watch where the hell he's going."
                                "They glare at Alan angrily. He smiles weakly."
                                "You nudge Alan hard."
                                alan "Oh right! Uh...sorry?"
                                freya angry "...Whatever."
                                "They start picking up the pieces of the compact. Alan shrugs awkwardly, then takes a few steps backwards."
                                "The bystander waves their wand at the pieces, muttering. There's a few sparks of magic, but nothing happens."
                                freya angry "Come on...come on!"
                                menu:
                                    ""
                                    "Help fix the compact.":
                                        p "Here, let me."
                                        "You pull out your wand for the second time this morning, and whisper an incantation."
                                        "The pieces of the compact fly together as if being pulled by an invisible magnet. The cracks glow for a second, then disappear."
                                        "You hand it to them."
                                        p "Good as new!"
                                        freya surprise "Uh, thanks..."
                                        "They examine the compact carefully."
                                        freya grin "I've never been too good with fixer spells, but wow! This looks better than it did before it broke."
                                        freya normal "Look, sorry about that back there. I mean, I'm not saying your friend isn't a complete and utter klutz, but I probably could've handled that better. It's kinda been a hectic morning."
                                        freya "I'm Freya."
                                        $ Freya = "Freya"
                                        "She puts her hand forward. You shake her hand."
                                        p "Nice to meet you, Freya. I'm %(player_name)s."
                                        "You see Freya's eyes go to the mirror you're holding."
                                        freya "Whoa, is that a magic mirror? That's so cool! I've always wanted one, but those things are hella expensive. Plus I am terrible at rhyming, so maybe that's not the best idea."
                                        "She opens her mouth to say something else, but at the moment the train whistles."
                                        freya "Ah, shoot that's my train. I gotta go, but here-"
                                        "She pulls out her wand and a blank card. She gives the wand a small wave, and her signature appears on the card."
                                        "She hands the card to you, and you slip it into your back pocket."
                                        freya "You should be able to contact me on my compact with that. Can't say I'd be much help in the spell department, but if you need anything else...I owe you."
                                        p "It was nothing, really."
                                        "The train horn blows again to signal it will be leaving shortly. Freya turns to leave."
                                        freya "Thanks again. Oh, and %(player_name)s?"
                                        freya grin "It was nice to meet you too."
                                        "With that, she runs towards the train, boarding just as the doors begin to close. You walk back to Alan, and watch the train leave the station."
                                        alan "I don't think I like her too much. She's a bit...intimidating."
                                        p "Yeah, well you did just crash into her and break her stuff. It was understandable."
                                        alan "Just so you know, I didn't need you to interrupt your call with Medea and come over here, I could've handled it myself!"
                                        p "Shoot!"
                                        "You look at your mirror. The line with Medea is dead."
                                        p "(She probably won't be too happy about that...)"
                    "Mmm, toast.":
                        "You look at the toast through the screen, you mouth watering slightly."
                        p "Mmm, toast. Now I wish I'd had breakfast."
                        medea "I wish I had more."
                        "She laughs fakely when suddenly more toast appears on the plate in front of her."
                        p "Aww, why are you so much better at magic than me?"
                        "Medea laughs again."
                        medea "It's because I am better than you, silly!"
                        "You frown and try to keep from getting mad at her."
                        p "At least I'm not the twenty-second person to have my name."
                        "Medea laughs yet again, but this time you know for sure she's faking it."
                        medea "Touche. Well, see you later!"
                        $ medea_fp -= 1
                        p "Bye!"
        label after_menu:
            "Well that conversation was virtually useless. Alan Stumbledork seems to be content with looking at the train schedule, but something is really bugging you. Why aren’t there more people at the station? A scientist, the enemy, is coming into the land and there aren’t even guards…"
            "'Have you ever seen Wardenburrough station so empty? It's amazing, isn't it?'"
            play sound "magic_sparkle.mp3"
            show high_wizard at on_screen
            with dissolve
            "The High Wizard appeared next to you, their fabulous beard floating as they gently landed on the cobblestone floor. The High Wizard’s aura filled the station, bringing a sort of special energy into it."
            alan "Your Highness! You're joining us?"
            hide high_wizard
            with dissolve

            h_w "Not quite. I'm here to see someone a hundred times better than any scientist."
            
            menu:
                ""
                "Who?":
                    p "Who are you here to see, your Highness?"
                    "The High Wizard smiles."
                    h_w "Only the most handsome and kind wizard I know."
                    p "Ohhh, I see."
                    $ hw_fp += 1
                    "You smile, knowing the High Wizard is taking about none other than Jax the Valiant, war hero and boyfriend to the High Wizard."
                "It's probably dangerous.":
                    p "You probably shouldn’t be here, your highness. The scientist could try to kill you the second they see you."
                    "The High Wizard scoffs."
                    h_w "They may try to kill me, doesn’t mean they will! Nothing will stop me from seeing my Jax come home."
                    alan "But your Highness-"
                    "The High Wizard looks at Alan furiously."
                    $ hw_fp -= 1
                    h_w "No. One. Will. Stop. Me."
                    "You didn't think it was possible for Alan to go any redder. He looks as if now would be the perfect moment for the ground to swallow him whole."
                    "If only he'd paid more attention in Earth class."
        label after_menu:
            "The train suddenly arrives, at 8 o’clock on the dot. You’ve never seen the High Wizard so ecstatic, they’re filling the entire train station with joy. The train slowly comes to a stop, the smell of soot and metal swirls through the station. The train doors open a few moments later, and a man steps out."
            "It's Jax the Valiant."

            h_w love "Jackie!"

            $ Jax = "Jax"

            "The High Wizard laughs with joy and runs into his arms, hugging and kissing him."

            j "At least someone missed me."
            h_w love "Who wouldn't??"

            "Another person exits the train, wearing a labcoat."
            "It's them. The scientist."
            "They spot you and avoid the adorable couple, making their way towards you. Alan looks up from the train schedule and makes eye contact with them, immediately dropping the schedule."
            "Oh dear gods."

            "The scientist holds out their hand for you to shake."
            skylar "Hello, I'm Skylar. I assume you're the ones the High Wizard sent to meet me?"
            menu:
                ""
                "Shake their hand.":
                    "You remain civil and shake Skylar’s hand."
                    p "It’s nice to finally meet you. You know your assignment, correct?"
                    $ skylar_fp += 1
                "Don't shake their hand.":
                    "You look at their gloved hand distastefully."
                    p "We don’t shake hands with scientists here. I assume you know your assignment?"
                    $ skylar_fp -= 1
        label after_menu:
            "Skylar clears their throat."
            skylar "Ah yes, I am to investigate the murder of Merlin the 17th and solve the case. Sort of like a class-A, Sherlock Holmesian detective."
            "You nod slowly, but Alan seems quite enthusiastic about this newcomer."
            alan "Exactly like Sherlock Holmes! Oh it’s great to meet you! I’m Alan Stumbledork--but please call me Alan."
            "Skylar cracks a real smile for the first since arriving."
            skylar "It's nice to meet you too, Alan."
            "As you look to the High Wizard and Jax, who are now talking while continually glancing at your small group, you think about what this all means. Were the events from the war finally fading into the past? Was this scientist a good person at all?"
            "It was all hard to tell, though one thing was for sure."
            "Your dream last night was still haunting you…It was most definitely an omen."
            stop music fadeout 1.0

            scene music_credits
            with Dissolve(2.0)
            $ renpy.pause(5.0)

            scene demo_end_screen
            with Dissolve(2.0)
            $ renpy.pause(10.0)







                                                                                                                                                                                                                           
                                                                                                                                                                                                                           
        return
    
    
        
        
        
    if faction == "scientists":
    
    
        call screen scientist_selection


        
        $ identity = _return
        
        
        if identity == "Pearl" or identity == "pearl":
            $ p = pearl_scientist
        
        
        if identity == "Skylar" or identity == "skylar":
            $ p = skylar_playable
            
        play music "opening_narration.mp3"
       
        
        show main_menu_past
        with fade
        
        #scene intro_scene
       
        $ player_name = "Garnet"
       # show high_scientist 

        e "As the High Scientist, I worked with the Community and Cooperation of the Sciences (the CCS) along with the Common Peoples Coalition (the CPC) in order to preserve peace and prosperity within all of Copernica."
        

        e "The events that I'm about to transcribe occurred long after the Arcana War."
        
        e "I had found five possible successors to my position already, even though I had only been in power for a decade or two at this point. Some of them were raised within some of the old science families including, Rosemary Franklin, Giovanni da Vinci, and Ash Lovelace. "
        
        e "However two of them were newcomers in a sense. There was Carlos, a passionate scientist who was the son of one of the members of the CPC and… oh goodness, what was their name again?"
        
        $ player_name = renpy.input("What is your name?")
        
        $ player_name = player_name.strip()
        $ player_name = player_name.capitalize()
        
        if player_name == "":
            $ player_name="Garnet"

#        show good_ending
#        with dissolve
        
#        if identity == "a":
#            show player_scientist at Position(xpos = 0.5, xanchor=0.5, ypos= 0.75,
#                yanchor= 0.5)
#            with dissolve
            
#        if identity == "b":
#            show player_scientist_femm
#            with dissolve

#        if identity == "c":
#            show player_scientist_pearl
#            with dissolve

        e "Ah yes, %(player_name)s! How could I possibly forget."
        
        e "%(player_name)s wasn't like the others at all. They went above and beyond the call of duty, serving within the army toward the tail end of the war, even spending some time on the frontline."
        e "Anyway, I had received communications from the High Wizard of Houdin that one of their council members, Merlin the 17th, had been murdered. I would not refuse this cry for assistance of course, as we of Copernica have a goal of keeping peace between our two countries in order to preserve progress, for progress is the only thing that matters."
        
        scene high_scientist_lab_past
        with fade

        h_w past "'I doubt that our magics killed him. We've already examined his body. There was no magical residues of any kind.'"

        e past "'Interesting... I'll send one of my scientists immediately. I would like to prevent any conflict.''"

        show main_menu_past
        with fade
        e normal "After our communications I looked through my personal catalogue of trusted scientists and found the perfect candidate."
        hide main_menu_past
        scene black

        e "%(player_name)s."

        stop music fadeout 4.0
        scene titlecard
        with Dissolve(2.0)
        $ renpy.pause(5.0)

        
        
        scene high_scientist_lab
        with Dissolve(4.0)
        
        play music "high_scientist.mp3" fadein 3.0 loop
        
        
        p "..."
        
        "You pace around the room for what seems to be the tenth time, contemplating why the High Scientist requested an audience with you."
        "Was it possible that you violated one of the codes of conduct?"
        "Whatever it was, it made a shiver go down your spine.  You sit down in front of the  counter, scanning the surrounding beakers and vials filled with strange chemicals, among other various scientific tools."
        "You only wish you had a laboratory as wonderful as the High Scientist's."
        play sound "lab-door-opens.mp3"
        "*Lab door opens*"
        
        e "Ah, you're here. Have a seat, Dr %(player_name)s. I deeply apologize, I had some other business to attend to."
        
        "The high scientist seems extremely distracted, more so than usual."
        
    menu:
        ""
        "Good morning, doctor.":
            p "No worries. Good morning, doctor."
            $ hs_fp += 1

            
            e "Good morning to you as well, Dr %(player_name)s. Please sit, I have something intriguing I need you to look into."
        
        "Am I in trouble, doctor?":
            p "Uh, I'm not in trouble right? I swear I had nothing to do with the slightly-unauthorized experiment in building 302."
            p "...Mostly, anyway."
            e "Not at all, Dr %(player_name)s. Please, take a seat. I have something interesting that I want you to look into."
            
    menu: 
        ""
        "How can I assist you?":
            "You take a seat opposite the High Scientist, feeling a mix of curiosity and slight anxiety."
            p "What is it, doctor? How can I assist you?"
            
            e "Well, there has been a murder among the ranks of the Wizards and I want you to make sure it wasn't one of our scientists. I don't want to risk another conflict with them."
            
        "I would help, but...":
            p "I have many experiments I’m running right now, and are you sure you want me? Carlos is usually best with fieldwork."
            
            "The High Scientist seems slightly irritated by your response."
            
            e " Don't lie to me Garnet, I checked my catalogue and it showed that you were available for forensic work."

            e "Carlos may be better at fieldwork but that's not what is needed. This is important on both a scientific and diplomatic level. I want you to investigate a murder among the Wizards."
            
            $ hs_fp -= 1


            

    label after_menu:
        
        p "A murder??" 
        
        e "Yes, one of the leader of their council was murdered three days ago and it has been causing a panic among the council. Especially since they think it was us."
        
        p "When will I be leaving?"
        
        e "Tomorrow morning at 6:54. You’ll be leaving Geode station heading toward Wickwood station, which is in Wardenburrough."
        
        p "(Wardenburrough... that's in the Wizard’s territory isn't it? I’m actually going there?)"
        
        p "So you want me to analyze the scene and determine who the killer is?"
        
        e "Precisely. Also, it would be best if you were to make some friends while you’re there. You may be in Wardenburrough for some time."
        
    menu:
        
        ""
        
        "How long am I staying in Wardenburrough?":
            p "How long am I staying in Wardenburrough?"
            
            e "However long it takes to keep the peace and solve the crime."
            
        
        "Friends? With Wizards?":
            p "Friends? With Wizards? Doctor, you can't be serious!"
            
            $ hs_fp -= 1
            
            e "Yes, you’ll have to make friends! %(player_name)s, do you want to see another war between us and them? We wouldn't be able to hold our defenses like that again, not this soon." 
            e "A war like that again would plunge us back into the dark ages!"
        
    label after_menu:
        
        if hs_fp == 1:
            e "You're the only one I trust to handle this, %(player_name)s. You've proven yourself time and time again."
        else:
            e "I chose you because I saw the potential in you. A true scientist would take up this challenge and find the solution to the case, not turn their backs."
        
        e "Now then, you’ll accept this assignment?"
        
    menu:
        ""
        "Yes, doctor.":
            e "Excellent. I’ll send Carlos to get you in the morning. He arranged your trip. Good luck, %(player_name)s."
        
        "...":
            $ hs_fp -= 1
            e "I’ll take that as a yes. You’re dismissed. Carlos will fetch you in the morning."
     
    label after_menu:
        
        "You nodded at the High Scientist and stood up, leaving the laboratory. You've never been to Wardenburrough, in fact, you’d never been to any Wizard controlled territory."
        
        "Would the wizards attack you the moment they saw you? Would they welcome you? All you knew was that this was going to be a long and harsh assignment."
        
        #" %(hs_fps"
        
        stop music fadeout 6.0
        
        
        #show dream_forest_1
        #with Dissolve(3.0)
        
       # play music "dream_music.mp3" fadein 5.0 loop
        
        #"Your dreams that night revolved around the magics and a dark figure. The ghostly form that haunted your dream followed you through the forest..."

        #$ renpy.play('boom.mp3')
       # with hpunch
        
       # ghost "..."
        
        #p "...?!"
        
        #show dream_forest
        #with fade
        
        #"It continued following you to the forest, occasionally approaching close enough that you could feel their breath against the back of your neck. A whisper would sometimes caress your ear, but the words were inaudibly quiet."
        
        #"When you arrived at a clearing within the forest, in the center of a large Fairy Circle, suddenly the whispers became clear as the figure wrapped around you, its shadowy presence enveloping and consuming you."
     
        #$ renpy.play('boom.mp3')
        #with hpunch
        
        #ghost "The world will end because of you."
        
        
        #stop music 
        
        scene black
        with fade
        play music "bensound-house.mp3"
        scene juicebox
        with fade 

        ash "Hello? Paging Doctor %(player_name)s, you're needed in the conversation!"

        "You blink a couple of times, focusing back in on the bar. You are in a place called the Juicebox. It is a bar that isn't frequented by many in the scientific community and rests in the sixth district of Geode, the capital city of Galilei, which is the southern province of Copernica."

        p "Sorry Ash! I spaced out there."

        ash "Come on, tell us why the High Scientist requested an audience with you!"

        rosemary "You realize that doesn't happen everyday right? He doesn't usually request meetings, much less talk to anyone actually--what did he say?"

        menu:
            ""
            "Tell them the truth":
                jump scientist_truth
            "Inform them it's none of their business":
                jump scientist_classified

        label after_convo:
            "You take a small sip of your drink. It tastes like strawberries, cream soda, and some foreign spicy element you can't quite put your finger on."
            "You stay in the Juicebox for some time before parting ways with your friends."
            "This would be the last time you would see them in a very long time."

            scene black
            with fade



            stop music fadeout 1.0
            scene endcard
            with Dissolve(2.0)
            $ renpy.pause(10.0)
            "Go to main menu ->"

        return

        
       # scene train_station
        #with Fade(0.5, 1.0, 0.5#)
        
     ##   $ renpy.play("boom.mp3")
      ##  with hpunch
       ## p "...huh?"
        #play sound("train.mp3")
        
        #"*Train whistle blows*"
        
        #play music "magical_journey.mp3" fadein 1.0 loop
        

        #"Your train arrived promptly at the station, 6:54 on the dot. You looked at Carlos for reassurance as you walked toward the train."
        
        #c "Don’t worry, you’ll do fine, %(player_name)s. Just don’t stress out too much, okay?"
        
    #menu: 
        #""
        #"I won’t.":
            #p "I won't, you know I don’t."
            #$ c_fp += 1 
            #c "Yeah, sure you won’t. Kick their butts--or you know, don’t, because that could potentially destroy what little peace we have. Haha!"
            
        #"Can’t you go instead?":
            #p "Please, can't you go instead?"
            #$ c_fp += 1
            #c "Aww, don’t be scared, you’ll do fine. If you need anything you call us, we’ll pick you up in a tank if we have to, heheh. Good luck, I believe in you."
            
    #label after_menu:
        
        #scene train_inside
        #with fade
        
        #"With that the train door closed, and you were separated from everyone you had ever known. You were now willingly going into enemy territory on one of their trains."
        
        
        #"You grasp the ticket tightly in your hand as you walk down the aisle, trying to find a seat. You have the aisle seat next to an older person with an eyepatch--he’s a wizard. He’s asleep, thank Newton, but he’s also not going anywhere."

        #"With a large gulp, you sit down, your nerves running high and your heartbeat fluttering anxiously. There was no way you could sleep on the train to recover the sleep you lost from that nightmare."
        
        #"You fidget uncomfortably in your seat as the the train starts rising up slowly. At first you think it is simply climbing up a hill, but as the train gains speed you realize that there are no hills, in fact, the train is no longer on the ground. You’re in the air, you’re flying in a magical train."
        
    #menu:
        #""
        #"Grip the seat and hold on for dear life.":
            #p "What the...!?!?"
            #"The Wizard next to you senses your tension in his sleep, either due to his magical powers or by the way you suddenly grabbed his arm accidentally as you gripped the seat. They raise a bushy eyebrow and turn to you, removing their hand from your clutches."
            #j "I guess you've never been on one of our trains before."
            #"He smiles kindly, which is an expression you’ve never seen on a Wizard before. They always seemed so angry. Upon further investigation it occurs to you that this Wizard is actually quite attractive."
            #j "I'm Jax."
            #$ Jax = "Jax"
            #"You blush slightly, and try to regain your composure."
        
        #"Lean over the wizard next to you to look out of the window.":
            #show outside_window
            #with fade
            #p "(Whoa...!)"
            #p "(You've GOT to be kidding me...this thing flies?)"
            #"You watch as the train flies higher and higher, until the people on the ground resemble ants."
            #p "(You've got to admit...this is just incredible.)"
            #play music "sudden.mp3"
            #$renpy.play("boom.mp3")
            #with hpunch
            #p "What the-?!"
            #hide outside_window
            #"The Wizard’s eye flutters open and they immediately grab you. Their grip is tight and you yelp loudly, looking at them fearfully. Their eye is glowing a deep, menancing red."
            #$ j_fp -= 1
            #j "Who are you and what are you doing?"
            #"The wizard glares at you, his face cold."
            #menu:
                #""
                #"(scared) Um, I'm sorry...":
                    
                    #"You begin to quiver slighty under the wizard's forbidding stare."
                    #p "*gulp* I’m sorry, I just wanted to look out the window..."
                    
                    #j "..."
                    
                    #stop music fadeout 1.0
                    
                    #"They look at you sympathetically and realize that you couldn’t hurt a fly even if you tried. Their eye changes to yellow and their grip loosens on your arm." 
                
                    #play music "magical_journey.mp3" fadein 1.0
                
                    #j "I’m sorry, I shouldn’t have done that. I’m still not used to the war being over. Reflexes, and all that. I'm Jax, by the way."
                    #$ Jax = "Jax"
                    
                #"(panicked) I was just looking...!":
                    #p "I just wanted to look out of the window! I’m sorry, I’m sorry!"
                    #"You wince away from the Wizard and close your eyes, preparing for a spell that they may cast."
                    
                    #j "..."
                    #stop music fadeout 1.0
                
                    #"Their eye immediately changes to off white and their expression softens. They let you go, their hand gently brushing against where they grabbed you."
                    #play music "magical_journey.mp3" fadein 1.0
                    
                    #j "Are you alright? I’m sorry if I hurt you, you caught me off guard. I’m Jax."
                    #$ Jax = "Jax"
                    #"Jax smiles at you, as if trying to show you that they meant no harm."
                
                #"...":
                    #stop music fadeout 4.0
                    #"They look at you curiously, but you remain silent. Their glare becomes sympathetic as they realize that you couldn’t hurt a fly even if you tried. Their eye changes to yellow and their grip loosens on your arm."
                    #play music "magical_journey.mp3" fadein 1.0
                    #j "I'm sorry if I hurt you, you just startled me."
                    #"They pause for a moment, and the silence makes you feel awkward. Then they smile at you."
                    #j "I should probably introduce myself. I'm Jax."
                    
            #menu:
                #""
                #"Accept their apology.":
                    #p "It's my fault, I shouldn't have leaned over you like that. But I appreciate the apology. It's nice to meet you."
                    #"You give them a quick smile."
                #"Snub them.":
                    #"You turn away irritably."
                    #p "Talk about overreacting..."
                    #"You glance back at the wizard. They seem slightly amused by your response."
                    
                #"...":
                    
                    #j "I see you're not one for talking?"
            #label after_menu:
            
            



    #label after_menu:
        #"The train's shaking slowly subsides, to your great relief."
        #play sound "train_alert.mp3"
        #"You hear a small bing, followed by a message from the train driver:"
        #"'Attention, all passengers: We have now reached altitude. You may roam the train freely, though only platinum members may enter VIP carts 1 through 5.'"
        #"'Please remember to be courteous to your fellow passengers. Thank you for riding with us, we hope you enjoy your flight.'" 
        
        #p "I’m %(player_name)s, by the way."
        
        #j "It's a pleasure to meet you."
        
        #"There is an awkward silence between the two of you."
        #menu:
            #"Make small talk":
                #p "So...where are you headed?"
                
                #j "I’m going to Pangaea station."

                #p "Oh, so am I actually! What a coincidence."

                #"Jax raises an eyebrow at you."

                #j "A scientist heading into Wizard territory? Well, that's not something you see every day."

            #"...":
                #"You remain silent."

    #label after_menu:
        #"Jax leans back in his seat, looking out the window. You wonder for a moment what madness he must have seen during the war. Considering his eyepatch it was likely that he fought on the frontlines."
        #"You think back to the war, remembering hearing about the terrible things that occurred in the beginning. You were too young to be part of the main war effort in the beginning, but you remember your mother leaving home back then. The war was barbaric."
        #"You close your eyes and exhale, trying to calm your mind. You’d have to keep up your guard from now on."
        #scene black
        #with Dissolve(3.0)
        #stop music fadeout 3.0
        #""
        #"WE WILL ALL BE ONE"

        #scene music_credits
        #with Dissolve(2.0)
        #$ renpy.pause(5.0)

        #scene demo_end_screen
        #with Dissolve(2.0)
        #$ renpy.pause(10.0)
        #"Go to main menu ->"




        #return
    
    
    
    
    
    
