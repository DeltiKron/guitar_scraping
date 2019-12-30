#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by schaffer at 11/22/19

"""
from glob import glob

import pandas as pd
import seaborn as sns
from os.path import dirname, join, abspath, basename
from clean_data import get_cleaned_df

directory = dirname(dirname(abspath(__file__)))
data_dirs = glob(join(directory, "data", "????-??-??"))

data_sets = {basename(d): glob(join(d, "*.csv")) for d in data_dirs}


daily_frames = {}
for day, files in data_sets.items():
    dfs = [get_cleaned_df(f) for f in files]
    daily_frame = pd.concat(dfs)
    daily_frames[day] = daily_frame
