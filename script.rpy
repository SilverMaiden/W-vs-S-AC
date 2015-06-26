# You can place the script of your game in this file.


# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image main_menu = "wizards-vs-scientists"
image intro_scene = "war-city.png"
image good_ending = im.Scale("good-ending.jpg", 800, 600)
image player_scientist = im.Alpha((im.Scale("player_scientist.png", 440, 500)), 0.8)
image player_scientist_femm = im.Alpha((im.Scale("player_scientist_femm.jpg", 470, 440)), 0.8)
image high_scientist_lab = im.Scale("high-scientist-lab.jpg", 800, 600)

 

#image high_scientist = im.Scale("high-scientist-1-b.png", 300, 300)



# Declare characters used by this game.
define e = Character('High Scientist', color="#c8ffc8", image = "high-scientist", window_left_padding=250)
define p_m = DynamicCharacter("player_name", color="#c8ffc8", image = "player_scientist", window_left_padding=250)
define p_f = DynamicCharacter("player_name", color="#c8ffc8", image = "player_scientist_femm", window_left_padding=250)
image side high-scientist = "side-high-scientist.png"
image side player_scientist = "side-player-scientist.png"
image side player_scientist_femm = "side-player-scientist-femm.png"
#image side high_scientist = "high-scientist-1-b.png"


# The game starts here.
label start:
    
    $ romance_points = 0
    $ mystery_points = 0
    #hs_fp = high scientist friendship points
    $ hs_fp = 0
    
    #show character_page
    #with fade
    $ identity = renpy.input("To select your character, enter the letter associated with that particular character.")
   # $ identity = identity.strip()
    
    if identity == "a":
        $ p = p_m
        
    if identity == "b":
        $ p = p_f
    
    
    play music "intro_music.mp3"
   
    
    show intro_scene
    with fade
    
    #scene intro_scene
   
    $ player_name = "Garnet"
   # show high_scientist 

    e "I can only vaguely recall the events that transpired after the war."
    

    e "I had been the leader of the scientific community for a few years at that point,"
    
    e "and I had found a number of rather promising possible successors to my position already."
    
    e "Leonardo da Vinci, Marie Curie, Carlos, and… Oh, I can’t seem to remember their name..."
    
    $ player_name = renpy.input("What is your name?")
    
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name="Garnet"
    
    show good_ending
    with dissolve
    
    if identity == "a":
        show player_scientist
        with dissolve
        
    if identity == "b":
        show player_scientist_femm
        with dissolve



    e "Ah yes, %(player_name)s, that was it! How could I possibly forget..."
    
    e "%(player_name)s played a very vital part in our relationship with the Wizards. In fact, I would even go as far as to say that" 
    e "%(player_name)s was the one who dictated our very future with them."
    
    e "Now let me tell you that story..."
    
    hide player_scientist
    
    stop music fadeout 3.0
    
    show high_scientist_lab
    with Dissolve(3.0)
    
    play music "lab_music.mp3" loop
    
    p "*Yawn*"
    
    p "...Where are they? It's not like them to be late..."
    
    "You had been a scientist for a few years now and were still quite young, at least compared to the Wizards."
    "You had never really hated the Wizards personally, it was all just politics. You had done your duty and fought against them during the tail end of the war, though you had never participated in combat."
    "Your job had been to crack and translate messages between the Wizards over their “magic” communication frequencies."
    "You didn’t believe the source of their power was really magic --it was science."
    "Everything came down to science."
    
    p "..."
    
    "You pace around the room for what must be the tenth time, stopping at the counter again."
    "Surrounding you are beakers and vials filled with strange chemicals, among other various scientific tools."
    "You wait in the laboratory of the High Scientist, the leader of the Community and Cooperation of the Sciences(the CCS). You have been called here for a meeting, the subject of which has yet to be revealed to you."
    "Hopefully, it’s not something troubling."
    
    play sound "lab-door-opens.mp3"
    "*Lab door opens*"
    
    e "Ah, you’re here. Sorry I’m late, %(player_name)s, I had some other business to attend to."
    
    "The high scientist seems extremely distracted, more so than usual."
    
menu:
    ""
    "Good morning, doctor.":
        p "No worries. Good morning, doctor."
        hs_fp += 1
        
        e "Good morning to you as well, %(player_name)s. Please sit, I have something intriguing I need you to look into."
    
    "Am I in trouble, doctor?":
        p "Uh, I'm not in trouble right? I swear I had nothing to do with the slightly-unauthorized experiment in building 302."
        p "...Mostly, anyway."
        e "Not at all, %(player_name)s. Please, have a seat. There is something interesting that I want you to look into."
        
menu: 
    ""
    "Take a seat":
        "You take a seat opposite the High Scientist, feeling a mix of curiosity and slight anxiety."
        
    "Remain standing":
        p "Actually, I'd prefer to stay standing, if you don't mind."
        
        "The High Scientist rolls his eyes."
        e "Yes yes, whatever you like."

menu:
    ""
    "I'd be happy to help":
        p "What's going on, doctor? How can I help?"
        "The High Scientist sighs heavily."
        e "I’m afraid to say there has been a murder among the ranks of the Wizards."
    
    "I would, but...":
        p "I was actually in the middle of running some experiments...Besides, are you sure you want me on this? Carlos is usually best when it comes to fieldwork."
        
        

label after_menu:
    

    return
