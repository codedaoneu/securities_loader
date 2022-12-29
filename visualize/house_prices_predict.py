import os
import sys

import mlflow
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

if __name__ == '__main__':
    try:
        data = pd.read_csv('data/house_prices/train.csv')
    except Exception as E:
        print("Unable to read file data, detail: {0}".format(E))

    model_data = data[["SalePrice", "LotArea", "WoodDeckSF", "OpenPorchSF",
                       "1stFlrSF", "GrLivArea", "MSSubClass", "MSZoning", "Neighborhood", "BedroomAbvGr"]]

    model_data_all = pd.get_dummies(model_data
                                    , prefix=["MSSubClass", "MSZoning", "Neighborhood", "BedroomAbvGr"]
                                    , columns=["MSSubClass", "MSZoning", "Neighborhood", "BedroomAbvGr"]
                                    , drop_first=False
                                    )
    Y = model_data_all["SalePrice"]
    X = model_data_all.loc[:, model_data_all.columns != "SalePrice"]

    # train test split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=40)

    if int(sys.argv[1]) == 1:
        intercept = True
    elif int(sys.argv[1]) == 0:
        intercept = False
    else:
        raise "wrong intercept input (intercept must be 0 or 1)"

    with mlflow.start_run():
        reg = LinearRegression(fit_intercept=intercept)
        reg.fit(X_train, Y_train)
        Y_pred = reg.predict(X_test)

        n = X_test.shape[0]
        p = X_test.shape[1]

        r2 = metrics.r2_score(Y_test, Y_pred)
        r2_adjusted = 1 - (1 - r2) * (n - 1) / (n - p - 1)

        # test_result = pd.concat([Y_test, Y_pred], axis=1)
        # test_result.columns = ["Y_test", "Y_pred"]
        # test_result["resid"] = test_result["Y_test"] - test_result["Y_pred"]
        # test_result.sort_values(by="resid", ascending=False)
        #
        # # Sai số trung bình của tập test:
        # print(test_result["resid"].mean())
        # print(test_result["resid"].std())

        print(reg.intercept_)
        print(reg.coef_, 5)
        print(r2)
        print(r2_adjusted)