import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

# ---------------------------------------------------------
# Loading Dataset
# ---------------------------------------------------------

print("Loading datasets...")

df1 = pd.read_csv(
    'C:/Users/Rishikesh/Desktop/PYTHON GROUP PROJECT/Tuesday-WorkingHours.pcap_ISCX.csv',
    low_memory=True
)
print("Tuesday loaded")

df2 = pd.read_csv(
    'C:/Users/Rishikesh/Desktop/PYTHON GROUP PROJECT/Wednesday-workingHours.pcap_ISCX.csv',
    low_memory=True
)
print("Wednesday loaded")

df3 = pd.read_csv(
    'C:/Users/Rishikesh/Desktop/PYTHON GROUP PROJECT/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv',
    low_memory=True
)
print("Thursday loaded")

dataset = pd.concat([df1, df2, df3], ignore_index=True)

print("Datasets combined")

dataset.columns = dataset.columns.str.strip()

# ---------------------------------------------------------
# Separating X and y
# ---------------------------------------------------------

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

X = X.apply(pd.to_numeric, errors='coerce')

X.replace([np.inf, -np.inf], np.nan, inplace=True)

# ---------------------------------------------------------
# Imputation
# ---------------------------------------------------------

from sklearn.impute import SimpleImputer

print("Starting imputation...")

imputer = SimpleImputer(
    missing_values=np.nan,
    strategy='mean'
)

X = imputer.fit_transform(X)

print("Imputation completed")

# ---------------------------------------------------------
# Label Encoding
# ---------------------------------------------------------

from sklearn.preprocessing import LabelEncoder

labelencoder_y = LabelEncoder()

y = labelencoder_y.fit_transform(y)

# ---------------------------------------------------------
# Train Test Split
# ---------------------------------------------------------

from sklearn.model_selection import train_test_split

print("Starting train-test split...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=0,
    stratify=y
)

print("Train-test split completed")

# ---------------------------------------------------------
# PCA
# ---------------------------------------------------------

from sklearn.decomposition import PCA

print("Starting PCA...")

pca = PCA(n_components=5)

X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

print("PCA completed")

# ---------------------------------------------------------
# Histogram Gradient Boosting Classifier
# ---------------------------------------------------------

from sklearn.ensemble import HistGradientBoostingClassifier

print("Starting Gradient Boosting...")

classifier = HistGradientBoostingClassifier(
    max_iter=50,
    learning_rate=0.1,
    max_leaf_nodes=15,
    random_state=0
)

classifier.fit(X_train, y_train)

print("Gradient Boosting completed")

# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

y_pred = classifier.predict(X_test)

print("Prediction completed")

# ---------------------------------------------------------
# Evaluation
# ---------------------------------------------------------

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:\n")
print(cm)

print("\nAccuracy : {:.4f}".format(
    accuracy_score(y_test, y_pred)
))

print("\nPrecision : {:.4f}".format(
    precision_score(
        y_test,
        y_pred,
        average='weighted',
        zero_division=0
    )
))

print("\nRecall : {:.4f}".format(
    recall_score(
        y_test,
        y_pred,
        average='weighted',
        zero_division=0
    )
))

print("\nF1 Score : {:.4f}".format(
    f1_score(
        y_test,
        y_pred,
        average='weighted',
        zero_division=0
    )
))

# ---------------------------------------------------------
# Classification Report
# ---------------------------------------------------------

print("\nClassification Report")
print("=" * 70)

print("{:<10} {:<12} {:<12} {:<12} {:<12}".format(
    "Class",
    "Precision",
    "Recall",
    "F1-Score",
    "Support"
))

print("-" * 70)

report = classification_report(
    y_test,
    y_pred,
    output_dict=True,
    zero_division=0
)

for i in range(len(labelencoder_y.classes_)):

    class_name = str(i)

    print("{:<10} {:<12.2f} {:<12.2f} {:<12.2f} {:<12}".format(
        class_name,
        report[class_name]["precision"],
        report[class_name]["recall"],
        report[class_name]["f1-score"],
        int(report[class_name]["support"])
    ))

print("-" * 70)

print("{:<10} {:<12} {:<12} {:<12} {:<12}".format(
    "Accuracy",
    "",
    "",
    "{:.2f}".format(report["accuracy"]),
    int(report["weighted avg"]["support"])
))

print("{:<10} {:<12.2f} {:<12.2f} {:<12.2f} {:<12}".format(
    "Macro Avg",
    report["macro avg"]["precision"],
    report["macro avg"]["recall"],
    report["macro avg"]["f1-score"],
    int(report["macro avg"]["support"])
))

print("{:<10} {:<12.2f} {:<12.2f} {:<12.2f} {:<12}".format(
    "Weighted Avg",
    report["weighted avg"]["precision"],
    report["weighted avg"]["recall"],
    report["weighted avg"]["f1-score"],
    int(report["weighted avg"]["support"])
))

print("=" * 70)