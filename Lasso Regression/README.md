# Lasso Regression

## Overview

Lasso Regression is a linear regression algorithm that uses **L1 regularization** to reduce model complexity and perform feature selection. It adds a penalty to the regression coefficients, which can force some coefficients to become zero.

In this project, Lasso Regression is applied to the CIC-IDS2017 network traffic dataset to study its performance under different train-test split ratios and PCA dimensionality settings.

## Dataset

The project uses three CIC-IDS2017 network traffic CSV files:

* Tuesday-WorkingHours.pcap_ISCX.csv
* Wednesday-workingHours.pcap_ISCX.csv
* Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv

The three datasets are combined before preprocessing.

## Data Preprocessing

The following preprocessing steps are performed:

1. The three datasets are loaded and combined.
2. Column names are cleaned by removing extra spaces.
3. Feature values are converted into numeric values.
4. Infinite values are replaced with missing values.
5. Missing values are handled using `SimpleImputer` with mean strategy.
6. The target variable is encoded using `LabelEncoder`.
7. The dataset is divided into training and testing sets.
8. PCA is applied **after the train-test split**.

## Experimental Setup

Nine experiments are performed by changing:

### Train-Test Split

* 80% Training / 20% Testing
* 60% Training / 40% Testing
* 40% Training / 60% Testing

### PCA Components

* 5 components
* 10 components
* 15 components

This results in **9 different experimental configurations**.

## Lasso Regression Model

The model is implemented using:

```python
from sklearn.linear_model import Lasso

regressor = Lasso(alpha=0.1)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
```

The `alpha` parameter controls the strength of L1 regularization.

## Evaluation Metrics

The performance of Lasso Regression is evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

## Experimental Files

Each experiment contains:

* One Python program file containing the complete implementation.
* One output image containing the execution result.

The file naming format is:

`test_size_nPCA_Lasso_program.py`

and

`test_size_nPCA_Lasso_output.png`

For example:

`0.2_n5_Lasso_program.py`

represents a 20% test size with 5 PCA components.

## Objective

The objective is to analyze how different train-test split ratios and PCA component selections affect the performance of Lasso Regression on network traffic data.

## Conclusion

Lasso Regression provides a regularized linear approach for analyzing the network traffic dataset. Comparing all nine configurations helps identify the effect of data splitting and dimensionality reduction on regression performance.

