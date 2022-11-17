import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as ppl
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":

    """COLUMNS:
    [0-4]: Id,MSSubClass,MSZoning,LotFrontage,LotArea,
    [5-9]: Street,Alley,LotShape,LandContour,Utilities,
    [10-14]: LotConfig,LandSlope,Neighborhood,Condition1,Condition2,
    [15-19]: BldgType,HouseStyle,OverallQual,OverallCond,YearBuilt,
    [20-24]: YearRemodAdd,RoofStyle,RoofMatl,Exterior1st,Exterior2nd,
    [25-29]: MasVnrType,MasVnrArea,ExterQual,ExterCond,Foundation,
    [30-34]: BsmtQual,BsmtCond,BsmtExposure,BsmtFinType1,BsmtFinSF1,
    [35-39]: BsmtFinType2,BsmtFinSF2,BsmtUnfSF,TotalBsmtSF,Heating,
    [40-44]: HeatingQC,CentralAir,Electrical,1stFlrSF,2ndFlrSF,
    [45-49]: LowQualFinSF,GrLivArea,BsmtFullBath,BsmtHalfBath,FullBath,
    [50-54]: HalfBath,BedroomAbvGr,KitchenAbvGr,KitchenQual,TotRmsAbvGrd,
    [55-59]: Functional,Fireplaces,FireplaceQu,GarageType,GarageYrBlt,
    [60-64]: GarageFinish,GarageCars,GarageArea,GarageQual,GarageCond,
    [65-69]: PavedDrive,WoodDeckSF,OpenPorchSF,EnclosedPorch,3SsnPorch,
    [70-74]: ScreenPorch,PoolArea,PoolQC,Fence,MiscFeature,
    [75-79]: MiscVal,MoSold,YrSold,SaleType,SaleCondition,
    [80]  : SalePrice
    """

    train = pd.read_csv("CSE368FinalProject/train.csv")
    
    for house in train.values:

        projectedCost = 0

        actualCost = house[80]


        print(actualCost)

    fields = list(train.columns)
