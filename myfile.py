# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import numpy as np
import datetime

d = st.date_input(
    "Fecha de cumple",
    datetime.date(2019,7,6))
st.write("Tu cumple es:",d)

