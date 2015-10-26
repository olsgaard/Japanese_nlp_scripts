# -*- coding: utf-8 -*-
"""
@author: Mads Olsgaard, 2014

Released under BSD-3 License

This scripts loads japanese text files and do various statistics on linguistic data
"""
#############
## Imports ##
#############

from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import matplotlib
import re, codecs

matplotlib.rc('font', family='TakaoPGothic')

################
## Load files ##
################

file1 = codecs.open("wikipedia_jp.txt", 'r', 'utf-8').read()
file2 = codecs.open("gutenberg_jp.txt", 'r', 'utf-8').read()

data = file1+file2

print("length of data file: ", len(data))

def plot_data(data, max=100):
    c = Counter(data)
    print("length of c", len(c))
    
    common = c.most_common(max)
    keys = [x[0] for x in common]
    values = [x[1] for x in common]
    y_pos = range(len(common))

    
    pl.figure()
    pl.plot(sorted(values, reverse=True))
    pl.xticks(y_pos, keys)
    pl.show()


print("distribution of all characters")
plot_data(data)
