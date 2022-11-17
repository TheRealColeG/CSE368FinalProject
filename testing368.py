import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as ppl
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":

    train = pd.read_csv("CSE368FinalProject/train.csv")

    fields = list(train.columns)

    print(fields)
