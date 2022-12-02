import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as ppl
from sklearn.linear_model import LinearRegression
import random

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

    train = pd.read_csv("train.csv")

    MAE = 0
    MSE = 0

    
    for house in train.values:

        """Fields we will use: 
        MSSubClass [1], LotArea [4], Utlities[9], OverallQual [17], OverallCond [18]       
        YearBuilt [19], ExterQual [27], ExterCond [28], TotalBsmtSF [38], CentrailAir [41]
        GrLivArea [46], *COMBINE* BsmtFullBath + BsmtHalfBath + FullBath + HalfBath [47-50]
        BedroomAbvGr [51], KitchenAbvGr [52], Functional [55], GarageCars [61], MiscVal [75]
        YrSold [77], SaleCondition [79]"""

        projectedCost = 90000

        listy = list()
        lotArea = int(house[4])
        projectedCost += int(lotArea * 0.3)

        #overall quality, overall condition
        y = 5 #5
        x = 6000 #6000
        projectedCost += (int(house[17]) - y) * x
        projectedCost += (int(house[18]) - y) * x

        #Year Built
        y = 1975 #1975
        x = 1000 #1000
        projectedCost += ((int(house[19])) - y) * x
        
        exterqual = house[27]
        x = 1.4
        match exterqual:
            case "Ex": projectedCost += 75000*x
            case "Gd": projectedCost += 0
            case "TA": projectedCost += 0
            case "Fa": projectedCost += -10000*x
            case "Po": projectedCost += -20000*x

        #Central Air
        x = 10000 #7500
        if (house[41] == "N"):
            projectedCost -= x

        #sq. ft. above ground
        x=7500
        y=2
        if (house[46] < 1300): projectedCost -= x
        elif (2000 < house[46] > 1300): projectedCost += x*y
        else : projectedCost += x*(y**2)

        #All baths
        x = 5000 #5000
        y = 1 #3
        projectedCost += ((house[47]+house[48]+house[49]+house[50])-y)*x

        #Bedrooms abv ground
        x = 10000 #10000
        y = 3 #3
        projectedCost += (house[51] - y)*x

        #Kitchens abv ground
        x = 15000 #15000
        projectedCost += (house[52])*x

        """ functionalList = ["Typ","Min1","Min2","Mod","Maj1","Maj2","Sev","Sal"]
        howbad = functionalList.index(house[55])
        x = 0 #1000
        projectedCost -= howbad * x"""

        """
        #Cars that can fit in garage
        x = 0 #10000
        y = 0 #2
        projectedCost += (house[61] - y)*x
        """

        #Misc Val?
        y = 2 #2
        projectedCost += house[75]*y

        #Year Sold
        x = 6000 #6000
        y = 2000 #2000
        projectedCost += (house[77] - y)*x

        actualCost = int(house[80])
        if (actualCost > 450000):
            pass
            print(actualCost, ":", projectedCost)
        else:
            MAE += abs(actualCost-projectedCost)
            MSE += (actualCost-projectedCost)**2

    print("MAE: ","{:,}".format(math.trunc(MAE / len(train))))
    print("MSE: ","{:,}".format(math.trunc(MSE / len(train))))

    fields = list(train.columns)
