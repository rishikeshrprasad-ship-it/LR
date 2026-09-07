ML Experiment Results Workbook
Overview

This repository contains the results of machine learning experiments conducted using different algorithms, configurations, train/test splits, and PCA dimensionality-reduction settings.

The main file in this repository is:

ML_Experiment_Results_Workbook.xlsx

The workbook is designed to systematically record model performance, compare experiments, and identify the best-performing configuration for each algorithm.

Models Evaluated

The workbook contains experiment results for the following machine learning algorithms:

Classification Models
Logistic Regression
Decision Tree
Gradient Boosting
LightGBM

These models are evaluated using classification metrics such as:

Accuracy
Precision
Recall
F1 Score
Class-wise Precision
Class-wise Recall
Class-wise F1 Score
Class-wise Support
Macro Average Precision
Macro Average Recall
Macro Average F1 Score
Weighted Average Precision
Weighted Average Recall
Weighted Average F1 Score
Regression Model
Lasso Regression

Lasso Regression experiments are evaluated using:

Mean Absolute Error (MAE)
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
R² Score
Experiment Configuration

Each experiment records the configuration used to train and evaluate the model.

The main configuration fields are:

Field	Description
Experiment	Identifier or description of the experiment
Test Size	Proportion of data used for testing
Train Size	Proportion of data used for training
PCA Components	Number of principal components used for dimensionality reduction

These configuration values allow different experiments to be compared consistently.

Logistic Regression

The Logistic Regression section contains classification results for multiple experiments.

For each experiment, the workbook records overall performance metrics including:

Accuracy
Precision
Recall
F1 Score

It also provides detailed class-level performance for Class 0 through Class 10.

For each class, the following metrics are recorded:

Precision
Recall
F1 Score
Support

The section also contains classification-report metrics, including:

Report Accuracy
Report Accuracy Support
Macro Average Precision
Macro Average Recall
Macro Average F1 Score
Macro Average Support
Weighted Average Precision
Weighted Average Recall
Weighted Average F1 Score
Weighted Average Support

This detailed structure makes it possible to evaluate both overall model performance and performance across individual classes.

Lasso Regression

The Lasso Regression section records regression experiment results.

Each experiment contains:

Test Size
Train Size
PCA Components
MAE
MSE
RMSE
R²

These metrics can be used to evaluate prediction error and the overall goodness of fit of the regression model.

For error-based metrics such as MAE, MSE, and RMSE, lower values generally indicate better performance.

For R², a value closer to 1 generally indicates better explanatory performance.

Decision Tree

The Decision Tree section contains classification experiment results.

Each experiment records:

Train/test configuration
PCA components
Accuracy
Precision
Recall
F1 Score

Detailed class-level metrics are provided for Class 0 through Class 10, including:

Precision
Recall
F1 Score
Support

The section also contains macro-average and weighted-average classification metrics.

Gradient Boosting

The Gradient Boosting section contains classification experiment results for different configurations.

The recorded metrics include:

Accuracy
Precision
Recall
F1 Score
Class-wise Precision
Class-wise Recall
Class-wise F1 Score
Class-wise Support
Macro-average metrics
Weighted-average metrics

The results can be used to compare how different train/test splits and PCA configurations affect Gradient Boosting performance.

LightGBM

The LightGBM section contains classification experiment results across different configurations.

The workbook records overall and class-level performance, including:

Accuracy
Precision
Recall
F1 Score
Class-wise Precision
Class-wise Recall
Class-wise F1 Score
Class-wise Support
Macro-average metrics
Weighted-average metrics

This allows LightGBM performance to be compared against the other classification algorithms in the workbook.

Overall Summary

The workbook includes an Overall Summary section that provides a consolidated view of model performance.

The summary contains:

Field	Description
Algorithm	Machine learning algorithm
Experiment	Experiment identifier
Test Size	Test dataset proportion
Train Size	Training dataset proportion
PCA Components	Number of PCA components
Accuracy/F1 or Main Metric	Primary metric used to evaluate the experiment

This section makes it easier to compare the major algorithms without reviewing every individual experiment.

Best Results

The Best Results section identifies the best-performing experiment for each algorithm.

It contains:

Field	Description
Algorithm	Machine learning algorithm
Best Experiment	Best-performing experiment
Test Size	Test dataset proportion
Train Size	Training dataset proportion
PCA Components	PCA configuration
Metric Used	Metric used to determine the best result
Score	Best achieved score

The metric used to determine the best result depends on the type of model and evaluation objective.

For classification models, Accuracy or F1 Score may be used as the primary comparison metric.

For regression models, metrics such as MAE, RMSE, or R² may be used depending on the evaluation objective.

PCA and Dimensionality Reduction

Several experiments include a PCA Components parameter.

Principal Component Analysis (PCA) is used to reduce the dimensionality of the feature space while retaining important information from the original features.

Testing different numbers of PCA components allows the experiments to determine whether dimensionality reduction improves model performance while potentially reducing model complexity.

Evaluation Approach

The experiments are structured to enable comparison across:

Different machine learning algorithms
Different train/test splits
Different PCA component configurations
Overall model performance
Individual class performance
Macro-average performance
Weighted-average performance

This provides a consistent framework for identifying the most effective model and configuration.

Classification Metrics
Accuracy

Accuracy represents the proportion of correctly classified observations out of the total observations.

Precision

Precision measures how many of the observations predicted as a particular class were actually members of that class.

Recall

Recall measures how many of the actual observations belonging to a class were correctly identified.

F1 Score

F1 Score combines precision and recall into a single metric and is particularly useful when both false positives and false negatives are important.

Macro Average

Macro average calculates the metric independently for each class and then takes the average, giving each class equal importance.

Weighted Average

Weighted average calculates the metric for each class and weights the result according to the number of samples in each class.

Support

Support represents the number of actual samples belonging to each class.

Regression Metrics
MAE

Mean Absolute Error measures the average absolute difference between predicted and actual values.

MSE

Mean Squared Error calculates the average squared difference between predicted and actual values.

RMSE

Root Mean Squared Error is the square root of MSE and represents prediction error on the same scale as the target variable.

R²

R² indicates how well the model explains the variance in the target variable.

Purpose of the Workbook

The workbook is intended to provide a structured record of machine learning experimentation.

It can be used to:

Track different model experiments.
Compare classification algorithms.
Evaluate class-level model performance.
Compare different PCA configurations.
Analyze the effect of different train/test splits.
Identify the best-performing experiment.
Maintain a reproducible record of model evaluation.
Support future model selection and optimization.
Repository Structure
ML-Experiment-Results/
│
├── README.md
│
└── ML_Experiment_Results_Workbook.xlsx

How to Use
Download or clone this repository.
Open ML_Experiment_Results_Workbook.xlsx.
Review the results for each algorithm.
Compare experiments using the recorded evaluation metrics.
Use the Overall Summary section for a quick comparison.
Use the Best Results section to identify the best configuration for each algorithm.
Project Status

Status: Machine Learning Experimentation and Model Performance Analysis

The workbook can be updated as additional experiments, configurations, or models are evaluated.

Author

Your Name
