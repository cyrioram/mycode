#!/usr/bin/env python3

feedback = 'You are '

while True:
##Watch for num entries only
    try:
        foodiness = float(input("On a scale from 1 to 100 with 1 being the most picky, how picky of an eater are you "))


        ##While foodiness is NOT number shortcircuit around if else block and print retry message

        # if input value was between 1 and 100
        if foodiness >= 75.0:
            feedback = feedback + 'definitely NOT a picky eater. Whatever the size, shape, smell, or texture; if it is food, you will put it in your mouth. You probably look down your nose at anyone who IS a picky eater, but look on the bright side — you can eat anything they do not finish!'
       
        elif foodiness >= 50.0 and foodiness <= 74.9:
            feedback = feedback + 'not that much of a picky eater. You are never afraid to try something new, even if that occasionally means eating things that make you want to be sick in your mouth.'

        elif foodiness >= 25.0 and foodiness <= 49.9:
            feedback = feedback + 'a very picky eater! So much so that going out for dinner is a never ending round of \"could I have [x] but without the [y]\". People give you shade, but what do people know!? Eat whatever you want, and politely turn your nose up at anything you DO NOT want near your face. Especially goat\'s cheese.'

        elif foodiness >=0.0 and foodiness <= 24.9:
            feedback = feedback + 'the pickiest of ALL the picky eaters. So much so that people are often giving you shit about it. But that\'s because they just don\'t understand. What they call picky, you just call having high standards! Eat what you want, and don\'t let anyone make you feel bad about it.'
        print(feedback)
        break

    ##NAN entry short circuit
    except:
        print("Type a number between 1 and 100, genius.")

