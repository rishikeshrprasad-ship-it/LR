# ML Experiment Results Workbook

## Overview

This repository contains the results of machine learning experiments conducted using different algorithms, train/test splits, and PCA dimensionality-reduction configurations.

The main file in this repository is:

**ML_Experiment_Results_Workbook.xlsx**

The workbook is designed to systematically record model performance, compare different experiments, and identify the best-performing configuration for each algorithm.

## Models Evaluated

### Classification Models

The workbook contains results for:

- Logistic Regression
- Decision Tree
- Gradient Boosting
- LightGBM

These models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Class-wise Precision
- Class-wise Recall
- Class-wise F1 Score
- Class-wise Support
- Macro Average Precision
- Macro Average Recall
- Macro Average F1 Score
- Weighted Average Precision
- Weighted Average Recall
- Weighted Average F1 Score

The classification results cover **11 classes, from Class 0 through Class 10**.

### Regression Model

The workbook also contains:

- Lasso Regression

Lasso Regression is evaluated using:

- MAE
- MSE
- RMSE
- R²

## Experiment Configuration

Each experiment records the configuration used for training and evaluation:

| Field | Description |
|---|---|
| Experiment | Identifier or description of the experiment |
| Test Size | Proportion of data used for testing |
| Train Size | Proportion of data used for training |
| PCA Components | Number of principal components used for dimensionality reduction |

These configuration values allow different experiments to be compared consistently.

## Logistic Regression

The Logistic Regression section contains classification results for different experiments.

For each experiment, the workbook records:

- Accuracy
- Precision
- Recall
- F1 Score

It also provides detailed performance for **Class 0 through Class 10**, including:

- Precision
- Recall
- F1 Score
- Support

The section also contains classification-report metrics:

- Report Accuracy
- Report Accuracy Support
- Macro Average Precision
- Macro Average Recall
- Macro Average F1 Score
- Macro Average Support
- Weighted Average Precision
- Weighted Average Recall
- Weighted Average F1 Score
- Weighted Average Support

## Lasso Regression

The Lasso Regression section contains regression results for different experiment configurations.

The recorded metrics are:

- **MAE** — Mean Absolute Error
- **MSE** — Mean Squared Error
- **RMSE** — Root Mean Squared Error
- **R²** — Coefficient of Determination

For MAE, MSE, and RMSE, lower values generally indicate better performance. For R², a value closer to 1 generally indicates better model performance.

## Decision Tree

The Decision Tree section contains classification results for different experiments and PCA configurations.

The results include:

- Accuracy
- Precision
- Recall
- F1 Score
- Class-wise Precision
- Class-wise Recall
- Class-wise F1 Score
- Class-wise Support
- Macro Average metrics
- Weighted Average metrics

Detailed performance is recorded for **Class 0 through Class 10**.

## Gradient Boosting

The Gradient Boosting section contains classification experiment results across different configurations.

The workbook records overall performance as well as detailed class-level metrics for **Class 0 through Class 10**.

The main metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- Macro Average metrics
- Weighted Average metrics

## LightGBM

The LightGBM section contains classification results for different experimental configurations.

The results include overall model performance and class-level performance for **Class 0 through Class 10**.

This allows LightGBM to be compared directly with:

- Logistic Regression
- Decision Tree
- Gradient Boosting

## Overall Summary

The **Overall Summary** section provides a consolidated comparison of the experiments.

It contains:

| Field | Description |
|---|---|
| Algorithm | Machine learning algorithm |
| Experiment | Experiment identifier |
| Test Size | Test dataset proportion |
| Train Size | Training dataset proportion |
| PCA Components | Number of PCA components |
| Accuracy/F1 or Main Metric | Primary metric used for comparison |

This section provides a quick overview of model performance without requiring the user to review every individual experiment.

## Best Results

The **Best Results** section identifies the best-performing experiment for each algorithm.

It contains:

| Field | Description |
|---|---|
| Algorithm | Machine learning algorithm |
| Best Experiment | Best-performing experiment |
| Test Size | Test dataset proportion |
| Train Size | Training dataset proportion |
| PCA Components | PCA configuration |
| Metric Used | Metric used to determine the best result |
| Score | Best achieved score |

The metric used to determine the best result depends on the model type and evaluation objective.

For classification models, **Accuracy or F1 Score** may be used as the primary comparison metric.

For Lasso Regression, **MAE, RMSE, or R²** may be used depending on the evaluation objective.

## PCA and Dimensionality Reduction

Several experiments include a **PCA Components** parameter.

Principal Component Analysis (PCA) is used to reduce the dimensionality of the feature space while retaining important information from the original features.

Testing different numbers of PCA components allows the experiments to determine whether dimensionality reduction improves model performance while potentially reducing model complexity.

## Evaluation Metrics

### Classification Metrics

**Accuracy:** Measures the proportion of correctly classified observations among all observations.

**Precision:** Measures how many observations predicted as a particular class were actually members of that class.

**Recall:** Measures how many actual observations belonging to a class were correctly identified.

**F1 Score:** Combines Precision and Recall into a single metric.

**Macro Average:** Calculates the metric independently for each class and gives every class equal importance.

**Weighted Average:** Calculates the metric for each class while weighting each class according to its number of samples.

**Support:** Represents the number of actual samples belonging to each class.

### Regression Metrics

**MAE (Mean Absolute Error):** Measures the average absolute difference between predicted and actual values.

**MSE (Mean Squared Error):** Measures the average squared difference between predicted and actual values.

**RMSE (Root Mean Squared Error):** Is the square root of MSE and represents prediction error on the same scale as the target variable.

**R² (R-Squared):** Measures how well the regression model explains the variance in the target variable.

## Purpose

The main purpose of this workbook is to provide a structured way to:

- Track machine learning experiments
- Compare different algorithms
- Compare different train/test splits
- Evaluate the effect of PCA components
- Analyze class-level classification performance
- Compare model evaluation metrics
- Identify the best-performing experiment
- Maintain a record of machine learning experimentation

## Repository Structure

```text
ML-Experiment-Results/
│
├── README.md
│
└── ML_Experiment_Results_Workbook.xlsx
