#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by schaffer at 11/22/19

"""
from pathlib import Path
import sys

from guitar_scraping.clean_data import get_guitars, get_sales
from guitar_scraping.db_interface import add_df_to_db
from guitar_scraping.db_interface.data_models import GuitarInfo, SalesInfo
from tqdm import tqdm

directory = Path(__file__).absolute().parents[1] / "data"
pattern = sys.argv[1] if len(sys.argv) > 1 else "????-??-??"
data_dirs = [*directory.glob(pattern)]

progress_bar = tqdm(data_dirs)
for day in progress_bar:
    progress_bar.set_description(str(day))
    pattern = "/*.csv"
    guitars = get_guitars(str(day) + pattern)
    add_df_to_db(guitars, GuitarInfo)
    sales = get_sales(str(day) + pattern)
    add_df_to_db(sales, SalesInfo)
