
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

N_TRIALS = 60
MIN_WAIT_TIME = 2000
MAX_WAIT_TIME = 3000
MAX_RESPONSE_DELAY = 2000


LEFT_RESPONSE_KEY = misc.constants.K_f
LEFT_RESPONSE_KEY_CHAR = 'F'
RIGHT_RESPONSE_KEY = misc.constants.K_j
RIGHT_RESPONSE_KEY_CHAR = 'J'

exp = design.Experiment(name="Contra & Inspilateral Reaction Times", text_size=40)
#control.set_develop_mode(on=True)
control.initialize(exp)

target = stimuli.FixCross(size=(50, 50), line_width=4)
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





exp.add_data_variable_names(['trial', 'wait', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for i_trial in range(N_TRIALS):
    blankscreen.present()
    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    exp.clock.wait(waiting_time)
    target.present()
    key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
    exp.data.add([i_trial, waiting_time, key, rt])

control.end()