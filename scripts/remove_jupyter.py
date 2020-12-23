import os
import pandas as pd
import numpy as np
from os import path
import codecs




base = "/Users/juanhuerta/personal_projects/code/blog/mini_book/_build/html/"

replace =  "Powered by <a href=\"https://jupyterbook.org\">Jupyter Book</a>"



with_ = " "

for filename in os.listdir(base):    # Load MIDI file into PrettyMIDI object
    if path.isdir(base + filename):
            for new_filename in os.listdir(base + filename):  # Load MIDI file into PrettyMIDI object
                if new_filename.endswith('.html'):
                    pa = base + filename +"/"+ new_filename
                    f = codecs.open(pa, 'r')
                    # for line in f.read():
                    s = f.read().replace(replace, with_)
                    with open(pa, 'w') as filetowrite:
                        filetowrite.write(s)

    else:
        ##these dont matter for my use case
        if filename.endswith('.html'):
            print(base + filename)

