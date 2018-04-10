import pandas as pd
import numpy as np


def column_fix(df):
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
