# Network Intrusion Detection Using Machine Learning

## Overview

This project focuses on detecting and classifying network traffic using different Machine Learning algorithms. The project uses network traffic data from the CIC-IDS2017 dataset to identify different types of network activity and network attacks.

Multiple Machine Learning algorithms are implemented and their performance is evaluated under different train-test split ratios and PCA dimensionality settings.

## Dataset

The project uses three CIC-IDS2017 network traffic CSV files:

* Tuesday-WorkingHours.pcap_ISCX.csv
* Wednesday-workingHours.pcap_ISCX.csv
* Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv

The three datasets are combined into a single dataset before preprocessing and model training.

## Data Preprocessing

The following preprocessing steps are performed:

1. Load the three network traffic datasets.
2. Combine the datasets into a single dataset.
3. Remove unnecessary spaces from column names.
4. Convert input features into numerical values.
5. Replace infinite values with missing values.
6. Handle missing values using mean imputation.
7. Encode target labels using LabelEncoder.
8. Split the dataset into training and testing data.
9. Apply PCA after the train-test split.
10. Train the selected Machine Learning algorithm.
11. Predict the classes using the test data.
12. Evaluate the model performance.

## Experimental Setup

Each Machine Learning algorithm is tested using different combinations of train-test split ratios and PCA components.

### Test Sizes

Three different test sizes are used:

* 0.2 → 80% training and 20% testing
* 0.4 → 60% training and 40% testing
* 0.6 → 40% training and 60% testing

### PCA Components

Three different PCA configurations are used:

* 5 components
* 10 components
* 15 components

Therefore, each algorithm is tested using:

**3 Test Sizes × 3 PCA Configurations = 9 Experiments**

## Total Experiments

Every algorithm has 9 separate experiments:

| Test Size | PCA 5        | PCA 10       | PCA 15       |
| --------- | ------------ | ------------ | ------------ |
| 0.2       | Experiment 1 | Experiment 2 | Experiment 3 |
| 0.4       | Experiment 4 | Experiment 5 | Experiment 6 |
| 0.6       | Experiment 7 | Experiment 8 | Experiment 9 |

This experimental setup allows the effect of training data size and PCA dimensionality on model performance to be compared.

## Machine Learning Algorithms

The project contains separate folders for each implemented algorithm:

* Logistic Regression
* Lasso Regression
* Decision Tree
* Gradient Boosting
* LightGBM

Each algorithm folder contains the programs and output screenshots for all 9 experimental configurations.

## Model Evaluation

For classification algorithms, the following evaluation metrics are used:

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report

The results from the different configurations can be compared to determine which combination of test size and PCA components provides better performance.

## Project Structure

```text
Network Intrusion Detection
│
├── LR
│   ├── 9 Python programs
│   ├── 9 output screenshots
│   └── README.md
│
├── Lasso Regression
│   ├── 9 Python programs
│   ├── 9 output screenshots
│   └── README.md
│
├── DT
│   ├── 9 Python programs
│   ├── 9 output screenshots
│   └── README.md
│
├── GB
│   ├── 9 Python programs
│   ├── 9 output screenshots
│   └── README.md
│
└── LGBM
    ├── 9 Python programs
    ├── 9 output screenshots
    └── README.md
```

## Objective

The main objective of this project is to implement and evaluate different Machine Learning algorithms for network intrusion detection and study how different train-test split ratios and PCA component configurations affect model performance.
