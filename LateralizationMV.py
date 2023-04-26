
#! /usr/bin/env python 
""" Simple Reaction Times of Ipsilateral and Contralateral Hand to Lateralized Visual Stimuli 

"""

"""Implementation of Berlucchi et als Simple Reaction Times of Ipsilateral and Contralateral Hand to Lateralized Visual Stimuli 
 (see https://github.com/chrplr/PCBS/blob/master/pdfs/papers-for-projects/Berlucchi%20et%20al.%20-%201971%20-%20SIMPLE%20REACTION%20TIMES%20OF%20IPSILATERAL%20AND%20CONTRALAT.pdf). 
This experiment is to be done in the lab, with the position of the head held constant by means of a head and chin rest, adjusted so that the right eye is positioned in the centre of the hemisphere. 
Note: The left eye is to be completely occluded with a special mask
"""


import pandas as pd
import argparse
import pygame 

import random
from expyriment import design, control, stimuli, misc

N_TRIALS = 60 # 6 times this in original paper 
MIN_WAIT_TIME = 2000 # as per original paper 
MAX_WAIT_TIME = 3000# as per original paper 
MAX_RESPONSE_DELAY = 2000 # TBC

GREY = (80, 80, 80)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


#CUE_DISPLAY_DURATION = 100  # 100 in hte original paper
#CUE_TARGET_INTERVAL = 400  # 0, 400 or 800 in the original paper
TARGET_DISPLAY_DURATION = 100  #35 MS in the original paper
#MAX_RESPONSE_DURATION = 1700


LEFT_RESPONSE_KEY = misc.constants.K_f
LEFT_RESPONSE_KEY_CHAR = 'F'
RIGHT_RESPONSE_KEY = misc.constants.K_j
RIGHT_RESPONSE_KEY_CHAR = 'J'

exp = design.Experiment(name="Contra & Inspilateral Reaction Times", text_size=40)


control.set_develop_mode(on=True)
control.initialize(exp)

print(exp.screen.window_size)

cross_white = stimuli.FixCross(size=(20, 20), colour=WHITE, line_width=4)



 

blankscreen = stimuli.BlankScreen()

instructions = stimuli.TextScreen("Instructions",
    f"""You are going to see sequence of square patches of lights, flashed on different points on the screen. 
Your task will be to respond as soon as you see the stimulus by pressing the indicated switches 
Very important:
1: You must stay fixated on the central cross and not move your right eye. 
2. You must respond quickly while avoiding errors. However, these are almost inevitable. If you do, don't get distracted, and focus on the next try. Dont respond before seeing stimulus 
Place your index finger on the keys '{LEFT_RESPONSE_KEY_CHAR}' (left) et '{RIGHT_RESPONSE_KEY_CHAR}' (right) then press your finger on the space button to start,
    
    There will be {N_TRIALS} trials in total.
   """, text_size=20)


LHShandinstructions = stimuli.TextScreen("Hand Instructions",
    f""" For this block please use your LHS and place your index finger on  '{LEFT_RESPONSE_KEY_CHAR}'. Press Space button to proceed. 
    
   
   """, text_size=20)


RHShandinstructions = stimuli.TextScreen("Hand Instructions",
    f""" For this block please use your RHS and place your index finger on '{RIGHT_RESPONSE_KEY_CHAR}'. Press Space button to proceed. 
    
   
   """, text_size=20)

# practise trials : 5 with both hands in the stimulus position
i=0
while i<5:

    #for i in stimulus : flash one stimulus, allow for both responses 
# stimulus randomised both hands , LHS vs RHS 

    i+=1


##### target trials 

# find a way to incorporate these in, with the a=tanalpha , 1140px=30cm(or size of screen)- corresponding to 


five_nasal = stimuli.Circle(radius=10, colour=WHITE, line_width=4, position=(-17.5, 250)) 
twenty_nasal = stimuli.Circle(radius=10, colour=WHITE, line_width=3, position=(-72.79, 250))
thirtyfive_nasal = stimuli.Circle(radius=10, colour=WHITE, line_width=3, position=(-140, 250))
five_temporal = stimuli.Circle(radius=10, colour=GREEN, line_width=3, position=(17.5, 250))
twenty_temporal = stimuli.Circle(radius=10, colour=GREEN, line_width=3, position=(72.79, 250))
thirtyfive_temporal = stimuli.Circle(radius=10, colour=GREEN, line_width=3, position=(140, 250)) 

five_nasal.preload()
twenty_nasal.preload()
thirtyfive_nasal.preload()
five_temporal.preload()
twenty_temporal.preload()
thirtyfive_temporal.preload()

nasal_block = [five_nasal, twenty_nasal, thirtyfive_nasal] * 5
temporal_block = [five_temporal, twenty_temporal, thirtyfive_temporal] * 5

random.shuffle(nasal_block)
random.shuffle(temporal_block)

# #MYSTIMULI = dict( fiveleft=five_nasal, 
#                        twentyleft=twenty_nasal, 
#                        thirtyfiveleft=thirtyfive_nasal, fiveright=five_temporal, 
#                        twentyright=twenty_temporal, 
#                        thirtyfiveright=thirtyfive_nasal)


exp.add_data_variable_names(['trial', 'wait', 'respkey', 'RT'])

########################################
control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait(keys=[misc.constants.K_t, misc.constants.K_SPACE])


#************NASAL PART********************

for i in range(4):

    if i ==0 or i==4:

        LHShandinstructions.present()
        exp.keyboard.wait(keys=[misc.constants.K_t, misc.constants.K_SPACE])

        for stim in nasal_block:
            blankscreen.present()
            cross_white.present()
            waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
            exp.clock.wait(waiting_time)
            print(stim)
            stim.present()
            exp.clock.wait(TARGET_DISPLAY_DURATION)
            #blankscreen.present()
            key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
            exp.data.add([ waiting_time, key, rt])

            #tbc - record lhs vs rhs + stimuli , reaction time 

    else:
        RHShandinstructions.present()
        exp.keyboard.wait(keys=[misc.constants.K_t, misc.constants.K_SPACE])
        for stim in nasal_block:

            RHShandinstructions.present()
            blankscreen.present()
            cross_white.present()

            waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
            exp.clock.wait(waiting_time)
            print(stim)
            stim.present()
            exp.clock.wait(TARGET_DISPLAY_DURATION)
            #blankscreen.present()
            key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
            exp.data.add([ waiting_time, key, rt])
 


#************TEMPORAL PART********************
for i in range(4):

    if i ==0 or i==4:

        LHShandinstructions.present()
        exp.keyboard.wait(keys=[misc.constants.K_t, misc.constants.K_SPACE])

        for stim in temporal_block:

            cross_white.present()

            blankscreen.present()
            waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
            exp.clock.wait(waiting_time)
            print(stim)
            stim.present()
            exp.clock.wait(TARGET_DISPLAY_DURATION)
            #blankscreen.present()
            key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
            exp.data.add([ waiting_time, key, rt])

            # ONE HAND  
        
    else:
         


        RHShandinstructions.present()
        exp.keyboard.wait(keys=[misc.constants.K_t, misc.constants.K_SPACE])

        for stim in temporal_block:

            cross_white.present()

            blankscreen.present()
            waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
            exp.clock.wait(waiting_time)
            print(stim)
            stim.present()
            exp.clock.wait(TARGET_DISPLAY_DURATION)
            #blankscreen.present()
            key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
            exp.data.add([ waiting_time, key, rt])

            # OTHER HAND - HOW DO I RANDOMIZE?




control.end()