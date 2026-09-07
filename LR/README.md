# Logistic Regression

## Overview

Logistic Regression is a supervised Machine Learning algorithm commonly used for classification problems.

In this project, Logistic Regression is used to classify different types of network traffic in the CIC-IDS2017 dataset.

## What We Did

The three network traffic datasets were combined and preprocessed. Numerical conversion, infinite-value handling, mean imputation, and target label encoding were performed.

The dataset was then divided into training and testing sets. PCA was applied after the train-test split to reduce the dimensionality of the input features.

The Logistic Regression model was trained using the training data and used to predict the classes in the testing data.

## Experimental Configurations

To study the effect of different data splits and PCA dimensions, Logistic Regression was executed 9 times.

### Test Sizes

* 0.2 → 80% training, 20% testing
* 0.4 → 60% training, 40% testing
* 0.6 → 40% training, 60% testing

### PCA Components

* 5
* 10
* 15

Therefore:

**3 Test Sizes × 3 PCA Settings = 9 Experiments**

## Experiments

| Test Size | PCA Components |
| --------- | -------------- |
| 0.2       | 5, 10, 15      |
| 0.4       | 5, 10, 15      |
| 0.6       | 5, 10, 15      |

Each configuration has a separate Python program and corresponding output screenshot.

## Evaluation

The classification performance is evaluated using:

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report

The 9 outputs can be compared to determine how the test size and PCA components affect Logistic Regression performance.

