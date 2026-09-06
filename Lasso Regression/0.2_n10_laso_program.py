import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

df1 = pd.read_csv('C:/Users/Rishikesh/Desktop/PYTHON GROUP PROJECT/Tuesday-WorkingHours.pcap_ISCX.csv', low_memory=True)
df2 = pd.read_csv('C:/Users/Rishikesh/Desktop/PYTHON GROUP PROJECT/Wednesday-workingHours.pcap_ISCX.csv', low_memory=True)
df3 = pd.read_csv('C:/Users/Rishikesh/Desktop/PYTHON GROUP PROJECT/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv', low_memory=True)

dataset = pd.concat([df1, df2, df3], ignore_index=True)

dataset.columns = dataset.columns.str.strip()

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

X = X.apply(pd.to_numeric, errors='coerce')

X.replace([np.inf, -np.inf], np.nan, inplace=True)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X = imputer.fit_transform(X)

from sklearn.preprocessing import LabelEncoder

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0,
    stratify=y
)

from sklearn.decomposition import PCA

# Apply PCA to reduce dimensionality (fit only on training data)
pca = PCA(n_components=10)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

from sklearn.linear_model import Lasso

regressor = Lasso(alpha=0.1)

regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

print("Lasso Regression")

print("\nMean Absolute Error : {:.4f}".format(
    mean_absolute_error(y_test, y_pred)
))

print("\nMean Squared Error : {:.4f}".format(
    mean_squared_error(y_test, y_pred)
))

print("\nRoot Mean Squared Error : {:.4f}".format(
    np.sqrt(mean_squared_error(y_test, y_pred))
))

print("\nR2 Score : {:.4f}".format(
    r2_score(y_test, y_pred)
))