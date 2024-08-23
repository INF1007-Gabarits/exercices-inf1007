#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error


# TODO: Définissez vos fonctions ici
def preprocess_data(path: str="./data/winequality-white.csv") -> tuple:
    df = pd.read_csv(path, sep=";", header=0)
    y = df["quality"]
    X = df.drop(columns=["quality"])

    return train_test_split(X.to_numpy(), y.to_numpy(), test_size=0.1)


def train_and_eval_model(model, X_train: list, X_test: list, y_train: list, y_test: list) -> list:
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    make_plot(np.arange(len(y_test)), y_test, pred, model.__class__.__name__)

    return pred


def make_plot(x: np.ndarray, target: list, pred: list, model_name: str) -> None:
    fig = plt.figure()
    plt.plot(x, target, label="Target values")
    plt.plot(x, pred, label="Predicted values")
    plt.legend()
    plt.title(f"{model_name} predictions analysis")
    plt.xlabel("Number of samples")
    plt.ylabel("Quality")

    fig.savefig(f"./{model_name}.png")


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    X_train, X_test, y_train, y_test = preprocess_data()
    rf_pred = train_and_eval_model(RandomForestRegressor(), X_train, X_test, y_train, y_test)
    lr_pred = train_and_eval_model(LinearRegression(), X_train, X_test, y_train, y_test)

    print(f"Random Forest mse: {mean_squared_error(y_test, rf_pred)}")
    print(f"Linear regression mse: {mean_squared_error(y_test, lr_pred)}")