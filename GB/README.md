# Gradient Boosting

## Overview

Gradient Boosting is an ensemble Machine Learning technique that combines multiple decision trees to create a strong predictive model.

In this project, histogram-based gradient boosting is used to classify different types of network traffic and intrusion classes.

## What We Did

The three CIC-IDS2017 network traffic datasets were combined and preprocessed. Input features were converted into numerical values, infinite values were handled, missing values were imputed, and target labels were encoded.

The dataset was split into training and testing sets. PCA was then applied after the train-test split to reduce the feature dimensionality.

The Gradient Boosting model was trained using the processed training data and used to predict the test classes.

## Experimental Configurations

The algorithm was executed using 9 different combinations.

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

| Test Size | PCA 5 | PCA 10 | PCA 15 |
| --------- | ----- | ------ | ------ |
| 0.2       | ✓     | ✓      | ✓      |
| 0.4       | ✓     | ✓      | ✓      |
| 0.6       | ✓     | ✓      | ✓      |

## Evaluation

Each experiment is evaluated using:

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report

The corresponding Python program and output screenshot for each configuration are included in this folder.

