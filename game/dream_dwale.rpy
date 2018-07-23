label dream_dwale:
    
                $ dream = "dwale"
                play sound "found_item.mp3"
                show dwale_bottle_night at on_screen
                with dissolve
                "You get out of bed and saunter over to the counter, grumbling to yourself about the damn light in your room. You take the small flask of Dwale and open the top, using the small eyedropper to retrieve a single tiny drop and place it on your tongue."
                hide dwale_bottle_night
                with dissolve
                "The drug starts taking effect once you set the flask down and you quickly get into bed before you pass out."


                show cave_outside_dream
                with dissolve

                play music "sudden.mp3"
                play music "howling-wind.mp3"
                play sound "whispers.mp3"
                "Suddenly, you find yourself in a dark cavern. The floor is covered in a slimy green ooze, you get up immediately and try to brush it off yourself. You feel damp and ill, and the wind coming from deep within the cavern makes you shiver."
                "Wait, wind?"
                "You look back and see the way out, but the cavern is calling you into it… or something in the cavern is calling you. You hear a voice in the back of your mind, but it must be nothing. Right?"

                p "..."

                ghost_nopic "It’s your fault...It’s all your fault..."

                show cave_inside_dream
                with dissolve

                "You walk further into the cavern, reaching into your robe and grasping at your wand. The smooth stone is warmer than the cave, as if it’s trying to comfort you, or as if it’s afraid."
                #stop music
                play music "creepy_dream.mp3"
               
                show cave_inside_dark_dream
                with dissolve

                $ renpy.play('boom.mp3')
                with hpunch
                "A green hand comes out of the floor, wrapping around your leg and dragging you into its slimy depths."


                p "AAAAAAAAAAAH!!!!"

                "You can't fight it."
                "You shut your eyes and you can’t breath."
                p "Hnnggg....!"

                $ renpy.play('boom.mp3')
                with hpunch
                peoplemonster "YOU KILLED US. YOU KILLED US."
                show people_monster at on_screen
                peoplemonster "YOU KILLED US."

                scene black
                with fade
                jump after_dreams
