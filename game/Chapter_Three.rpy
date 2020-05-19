label Start_chp3:
    $ CurrentChap = 3
    $unknowName = "???"
    scene Drak_pic
    unknow "I will find you.."
    show VampySprite at left
    mc "what?!"
    hide VampySprite
    unknow "You are the key.."
    show VampySprite at left
    mc "who are you??!"
    jump wake_up


label wake_up:

    scene Farmhouse_Bed
    show VampySprite

    mc "It's a dream?"
    mc "(Feeling headache)"
    mc "Ugh, I should go for a walk"

    jump meet_anna


label meet_anna:

    scene Strip_Mall
    show Anna at right
    Anna "Hey, sir"
    show VampySprite at left
    mc "Huh? Did you talk to me?"
    Anna "Do you believe destiny?"
    mc "What? Who are you?"
    Anna "I am a fortuneteller, my name is Anna, follow me I will show the path of your destiny."
    $AnnaName = "Anna"
    menu:
        "No, get away from me.": #trust - 1
            $ total_trust -= 1
            $ trust_for_anna -=1
            $ first_choice = 1

        "...":
            $ first_choice = 1

        "Really? Show me something.": #trust + 2
            $ total_trust += 2
            $ trust_for_anna += 2
            $ first_choice = 0

    if first_choice == 0:
        jump in_Psychic_store
    if first_choice == 1:
        Anna "Are you afraid to face your destiny, your depth of yourself?"
        menu:
            "Hmph, are you Seriously? I gonna tear down your lies.": #trust -1
                $ total_trust -= 1
                $ trust_for_anna -= 1
                Anna "You won't"
                jump in_Psychic_store

            "Definitely not!": #trust + 1
                $ total_trust += 1
                $ trust_for_anna += 1
                Anna "Good"
                jump in_Psychic_store

label in_Psychic_store:
    scene Psychic_store
    show Anna at right
    show VampySprite at left
    Anna "Welcome to my place, let's see what Madame Fate has in store for us, what?"
    menu:
        "Who am I?":
            Anna "You are on the path to discovering yourself, Once the time is up, you will know that for sure"
            $last_choice = 1
        "Why I am here?":
            Anna "Something led you here, that is your destiny"
            $last_choice = 2
    if last_choice == 1:
        menu:
            "Why I am here?":
                Anna "Something led you here, that is your destiny"
    if last_choice == 2:
        menu:
            "Who am I?":
                Anna "You are on the path to discovering yourself, Once the time is up, you will know that for sure"
    mc "Hmm..."
    jump ask_crystal_ball


label ask_crystal_ball:
    show VampySprite at left
    show Anna at right
    Anna "Okay, we done, and 10 dollars, please."
    mc "Wait, what? That's all you got? you want me pay 10 dollats for just bullshit?"
    Anna "Yes...oh, no worry, now look at the crystal ball, it will tell you your destiny...I guess"
    mc "Fine."
    hide VampySprite
    hide Anna
    "*Two minutes later..*"
    show VampySprite at left
    mc "Okay, it's time to leave, I don't want to play a silly game with such swindler"
    show Anna at right
    Anna "No...just waiting for 2 more... 5 more minutes it might will..."

    scene Crystal_ball
    "*Suddenly, Anna disappear and everything turns to dark, the crystal ball starts flashing*"
    $unknowName = "*The sound in your mind*"
    unknow "\n
             The chaos and darkness are around over you"
    unknow  "\n
            You either destroy them or dead with chaos and darkness, most importantly..."
    scene Psychic_store
    "*Everything turn it back*"

    show Anna at right
    Anna "*fake cough fake cough* Unfortunately, I out of power today but the crystal ball will work for next time, I guarantee you!"
    show VampySprite at left
    mc "Wait, what? you mean the crystal ball doesn't work?! But I hear some..."
    Anna "Don't be angry my friend, you are the lucky one because the first time customer for free for today’s promo"
    mc "Er.."
    Anna "Thanks for visit here, and I see you next time!"

    jump after_meet_anna

label after_meet_anna:
    scene Strip_Mall
    show VampySprite
    mc "Hmm...That sound seems have some connection with today's dream"
    mc "I need to figure out it."
    $ Night_count = 0
    jump Chapter_Three_Morning

label Chapter_Three_Morning:

    if Night_count == 3:
        jump Start_chp4 #chapter start here
    $ Night_count += 1


    scene Farmhouse_Day
    "You wake up feeling refreshed. What do you do?"

    if jd_dead == True:
        menu:
            "Go get supplies?":
                jump time_with_jane
            "Go to the creek?":
                jump time_with_cash
            "Go to Psychic store?":
                jump time_with_ana

    if janeD_dead == True:
        menu:
            "Tend to the crops?":
                jump John_info
            "Go to the creek?":
                jump time_with_cash
            "Go to Psychic store?":
                jump time_with_ana

    if jc_dead == True:
        menu:
            "Tend to the crops?":
                jump John_info
            "Go get supplies?":
                jump time_with_jane
            "Go to Psychic store?":
                jump time_with_ana

label time_with_ana:
    scene Psychic_store
    show Anna at right
    show VampySprite at left
    Anna "Hey, [MCname], welcome back, what brings you back here?"
    menu:
        "Your power, that's why I am come back here":
            $ total_trust += 1
            $ trust_for_anna += 1
            #trust +1

        "I just feel boring and try to make some fun here":
            $ total_trust -= 1
            $ trust_for_anna -= 1
            #trust -1

    Anna "Fine, let's see what Madame Fate has in store for us, what?"
    menu:
        "Ask some question for you":
            $ choice_with_ana  = 1
            $ total_trust += 1
            $ trust_for_anna += 1
            #trust + 1

        "Get something on the crystal ball":
            $ choice_with_ana = 2

    if choice_with_ana == 1:
        menu:
            "Who am I?":
                Anna "You are on the path to discovering yourself, Once the time is up, you will know that for sure"
                $ the_last_choice = 1
            "Why I am here?":
                Anna "Something led you here, that is your destiny"
                $ the_last_choice = 2
        if the_last_choice == 1:
            menu:
                "Why I am here?":
                    Anna "Something led you here, that is your destiny"
        if the_last_choice == 2:
            menu:
                "Who am I?":
                    Anna "You are on the path to discovering yourself, Once the time is up, you will know that for sure"

    if choice_with_ana == 2:
        #for here the message will change when the trust of anna increase more
        scene Crystal_ball
        $unknowName = "*The sound in your mind*"
        unknow "\n
                 The chaos and darkness are around over you"
        unknow  "\n
                You either destroy them or dead with chaos and darkness"
        scene Psychic_store
    show VampySprite at left
    mc "Hmm...Okay, I got something, bye"
    show Anna at right
    Anna "Thanks for visit here, and I see you next time!"
    if CurrentChap == 3:
        jump Chapter_Three_Morning
