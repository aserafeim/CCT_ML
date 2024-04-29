import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('Crit_temp.csv')

sns.set_style('darkgrid')

sns.pairplot(df, hue="species")


