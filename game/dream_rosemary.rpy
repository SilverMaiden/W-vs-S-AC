label dream_rosemary:
                $ dream = "rosemary"
                play sound "found_item.mp3"
                show rosemary_pillow
                with dissolve

                "You sigh heavily and reach toward the rosemary pillow, the silky blue fabric shifting in your hand. You place the pillow over your nose, breathing in deeply, the hypnotic scent overwhelming your senses."
                hide rosemary_pillow
                with dissolve
                "After a few deep breaths you begin to feel drowsy and fall into a hypnotic and restful sleep."
                
                
                show dream_rose_garden
                with fade
                
                play music "sweet_dream.mp3" fadein 2.0
                
                "You are suddenly in the middle of a garden of pink and white roses. The grass tickles your barefeet and you giggle, breathing in deeply, smelling rosemary and nothing else."
                
                "You start running at first, laughing but then you fall."
                
                stop music 
                p "Aaah!"
                play music "creepy_dream.mp3"
                show bad_dream_rose_garden
                with Dissolve(2.0)
    
                $ renpy.play('boom.mp3')
                with hpunch
                
                "A sharp pain comes over your leg, which is now covered in thorns."
                
                $ renpy.play('boom.mp3')
                with hpunch
                
                show final_rose_garden
                with dissolve
                
                "You try to untangle yourself but all your efforts are only causing more damage. Your skin becomes covered in blood, the scene grows dark and a whisper nips at your ear."
                show thorns1
                play sound "splat.mp3"

                p "AHHHH! HELP ME!!"
                $ renpy.play('boom.mp3')
                with hpunch
                ghost "We will all be one."

                "You turn around frantically, staring at a figure without face, the only defining feature being a large gaping hole--a toothless orifice that could possibly be described as a mouth."
                show thorns2
                play sound "splat.mp3"
                "It spoke again, it’s words filling everything and your mind becoming numb as it consumed you."
                
                ghost "WE WILL ALL BE ONE. WE WILL BE ONE. I AM EVERYTHING."

                $ renpy.play('boom.mp3')
                with hpunch
                show blood_splatter_dark
                show ghost
                "I AM EVERYTHING."

                scene black
                with fade

                jump after_dreams



