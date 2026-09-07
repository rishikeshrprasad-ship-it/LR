# LightGBM

## Overview

LightGBM (Light Gradient Boosting Machine) is a gradient boosting framework designed for efficient and fast Machine Learning. It uses tree-based learning and is suitable for handling large datasets.

In this project, LightGBM is used to classify network traffic into different intrusion detection classes.

## What We Did

The three CIC-IDS2017 datasets were combined and preprocessed. The input features were converted into numerical values, infinite values were handled, and missing values were replaced using mean imputation.

The target labels were converted into numerical classes using LabelEncoder.

The dataset was divided into training and testing sets. PCA was applied after the train-test split to reduce the dimensionality of the input features.

The `LGBMClassifier` was trained using the processed training data and used to predict the classes in the test data.

## Experimental Configurations

LightGBM was executed using 9 different configurations.

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

Each LightGBM experiment is evaluated using:

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report

Each configuration has its own Python program and output screenshot, allowing the results to be compared across different test sizes and PCA settings.
