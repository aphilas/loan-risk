import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score, validation_curve
from sklearn.svm import SVC
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

df = pd.read_excel('https://github.com/aphilas/loan-risk/blob/main/Risk%20data.xlsx?raw=true')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # Drop "#Unnamed" colums
# df.head()
df

df.describe()



target = df.RISK.astype('category').cat.codes

input = df.drop(['ID', 'RISK'], axis='columns')
input.INCOME = pd.cut(input.INCOME, bins=[15000, 20000, 24000, 30000, 42000, 60000], labels=False)
input.AGE = pd.cut(input.AGE, bins=[17, 21, 31, 41, 51], labels=False)
input.NUMKIDS = pd.cut(input.NUMKIDS, bins=[-1,0,1,5 ], labels=False) 
input.NUMCARDS = pd.cut(input.NUMCARDS, bins=[-1,1,2,7 ], labels=False) 
input.STORECAR = pd.cut(input.STORECAR, bins=[-1,1,2,3,6 ], labels=False)
input.LOANS = pd.cut(input.LOANS, bins=[-1,0,1,6 ], labels=False)
input = pd.get_dummies(input, columns=['GENDER', 'MARITAL', 'HOWPAID', 'MORTGAGE'], drop_first=True)
input

score_sums = dict()

for i in range(20):
    for column in list(input):
        X_train, X_test, y_train, y_test = train_test_split(input.drop(column, axis='columns'), target, test_size=0.2)
        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X_train,y_train)
        score = knn.score(X_test,y_test)

        try:
            score_sums[column] += score
        except KeyError:
            score_sums[column] = score

scores = sorted([ (score_sums[column] / 20, column) for column in list(input) ], key=lambda v:v[0], reverse=True)

# score of model with respective columns dropped
# appears to be random!?
scores 

# STORECAR, GENDER_m, AGE, HOWPAID_weekly

# 60-20-20
train_ratio = 0.6
validation_ratio = 0.2
test_ratio = 0.2

X_train, X_test, y_train, y_test = train_test_split(input, target, test_size=1 - train_ratio)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=test_ratio/(test_ratio + validation_ratio)) 

### testing n_neighbors param, as an example

# use validation or training set!?
param_range = (2, 3, 4, 5)
train_score, val_score = validation_curve(KNeighborsClassifier(), X_val, y_val, cv=10, param_name='n_neighbors', param_range=param_range)

plt.plot(param_range, np.median(train_score, 1), color='blue', label='training score')
plt.plot(param_range, np.median(val_score, 1), color='red', label='validation score')
plt.legend(loc='best')
plt.ylim(0, 1)
plt.xlabel('param')
plt.ylabel('score')

###

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
knn.score(X_test, y_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(input,target)
# score = knn.score(X_test,y_test)
scores = cross_val_score(knn, input, target, cv=10)
scores.mean()

X_train, X_test, y_train, y_test = train_test_split(input, target, test_size=0.2)
dtree = DecisionTreeClassifier( max_depth=8)

dtree.fit(X_train, y_train)
dtree.score(X_test, y_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
knn.score(X_test,y_test)

svc = SVC()
svc.fit(X_train, y_train)
svc.score(X_test, y_test)
