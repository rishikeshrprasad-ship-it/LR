# Decision Tree

## Overview

Decision Tree is a supervised Machine Learning algorithm that can be used for classification. It makes predictions by creating a tree structure based on decision rules derived from the input features.

In this project, Decision Tree is used to classify network traffic into different intrusion detection classes.

## What We Did

The three CIC-IDS2017 datasets were combined and preprocessed. The input features were converted into numerical values, missing and infinite values were handled, and target labels were encoded.

The dataset was divided into training and testing sets, followed by PCA after the train-test split.

The Decision Tree classifier was trained on the processed training data and used to predict the test classes.

## Experimental Configurations

The Decision Tree model was tested using 9 different configurations.

### Test Sizes

* 0.2
* 0.4
* 0.6

### PCA Components

* 5
* 10
* 15

This results in:

**3 Test Sizes × 3 PCA Settings = 9 Experiments**

## Model Configuration

* Algorithm: Decision Tree Classifier
* Criterion: Entropy
* Random State: 0

## Evaluation

Each experiment is evaluated using:

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report

A separate Python program and output screenshot are provided for each configuration.

