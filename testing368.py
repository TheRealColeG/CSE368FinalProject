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
    [80]   : SalePrice
    """

    train = pd.read_csv("CSE368FinalProject/train.csv")
    print(len(train))

    difference = 0
    
    for house in train.values:

        """Fields we will use: 
        MSSubClass [1], LotArea [4], Utlities[9], OverallQual [17], OverallCond [18]       
        YearBuilt [19], ExterQual [27], ExterCond [28], TotalBsmtSF [38], CentrailAir [41]
        GrLivArea [46], *COMBINE* BsmtFullBath + BsmtHalfBath + FullBath + HalfBath [47-50]
        BedroomAbvGr [51], KitchenAbvGr [52], Functional [55], GarageCars [61], MiscVal [75]
        YrSold [77], SaleCondition [79]"""
        
        projectedCost = 0

        subClass = house[1]
        match subClass:
            case 20: projectedCost = 200000
            case 30: projectedCost = 100000
            case 40: projectedCost = 150000
            case 45: projectedCost = 125000
            case 50: projectedCost = 175000
            case 60: projectedCost = 200000
            case 70: projectedCost = 150000
            case 75: projectedCost = 225000
            case 80: projectedCost = 125000
            case 85: projectedCost = 75000
            case 90: projectedCost = 70000
            case 120: projectedCost = 175000
            case 150: projectedCost = 200000
            case 160: projectedCost = 210000
            case 180: projectedCost = 180000
            case 190: projectedCost = 200000

        listy = list()
        lotArea = int(house[4])
        projectedCost += int(lotArea * 0.3)

        projectedCost += (int(house[17]) - 5) * 5000
        projectedCost += (int(house[18]) - 5) * 5000

        projectedCost += ((int(house[19])) - 1980) * 2000
        
        exterqual = house[27]
        match exterqual:
            case "Ex": projectedCost += 20000
            case "Gd": projectedCost += 10000
            case "TA": projectedCost += 0
            case "Fa": projectedCost += -10000
            case "Po": projectedCost += -20000

        extercond = house[28]
        match extercond:
            case "Ex": projectedCost += 20000
            case "Gd": projectedCost += 10000
            case "TA": projectedCost += 0
            case "Fa": projectedCost += -10000
            case "Po": projectedCost += -20000

        if (house[41] == "Y"):
            projectedCost += 2500

        if (house[46] < 1300): projectedCost -= 15000
        elif (2000 < house[46] > 1300): projectedCost += 10000
        else : projectedCost += 20000

        projectedCost += ((house[47]+house[48]+house[49]+house[50])-3)*5000
        projectedCost += (house[51]-3)*5000

        projectedCost += (house[52] - 1)*10000

        functionalList = ["Typ","Min1","Min2","Mod","Maj1","Maj2","Sev","Sal"]
        howbad = functionalList.index(house[55])
        projectedCost -= howbad * 5000

        projectedCost += (house[61]-2)*5000

        projectedCost += house[75]*10

        projectedCost += (house[77]-2000)*50

        actualCost = int(house[80])
        print(actualCost - projectedCost)
        difference += actualCost-projectedCost

    print(difference / len(train))
    

    fields = list(train.columns)
