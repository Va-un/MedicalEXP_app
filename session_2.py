# -*- coding: utf-8 -*-
"""Session 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZKaHh3Nmimx_uQdjPwJdOH7MMjrxxYT0

https://www.kaggle.com/datasets/nanditapore/medical-cost-dataset

#Intro to Pandas

## Acessing the Data
"""

import pandas as pd
import numpy

df = pd.read_csv("medical_cost.csv",index_col= 'Id')



"""**Native accessors**

Native Python objects provide good ways of indexing data. Pandas carries all of these over, which helps make it easy to start with.

Consider this DataFrame:
"""

df



"""## Viewing Data

To access a Specific column we can use two ways

```
# df.columnname
```


```
# df["columnname"]
```
"""

df.age

df['age']

"""To acess the row you can add the row id in front of it with [ ]"""

df['age'][10]

"""## Indexing
The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem. As a novice, this makes them easy to pick up and use. However, pandas has its own accessor operators, **loc** and **iloc**. For more advanced operations, these are the ones you're supposed to be using.


1.index-based selection:



```
# df.iloc[rowid]
```
2.label-based selection:


```
# df.loc[rowid, 'columnid']
```



"""

df.iloc[0]

"""now accessing is similar to string"""

df.iloc[:5]

df.loc[:3, 'children']

df.loc[3, ['bmi',	'children',	'smoker']]

"""## Conditional selection"""

df.sex == "male"

df[df.sex == "male"]

df[(df.sex == "male") & (df.bmi >30)]

"""## Summary Functions and Sorting

**Describe**

Gives a Statistical description of the data.


```
# df.describe()
```
**Unique**

Returns unique values.



```
# df.colname.unique()
```

**value_counts**

Returns number of unique values.


```
# df.colname.valuecounts()
```

**sort_values**


sorts value of given column(can be multiple columns).



```
# df.sort_values(by='column',, ascending=bool)
```
"""

df.describe()

df.region.unique()

df.region.value_counts()

df.sort_values(by='region')

"""## Data Types and Missing Values

**Info**

Gives Breif about Dtypes.

```
# df.info()
```


**Check null values:**
Returns number of null values.

```
# df.isnull().sum()
```
**Fill na**
Helps in filling null values.

```
# df.columnname.fillna("filling data", inplace = True)
```



"""

df.info()

data = [
    ["John Doe", 30, 10000],
    [None, 25, 20000],
    ["Jane Doe", 20, 30000],
    [None, 40, 40000],
    ["Peter", 35, None],
]

MM = pd.DataFrame(data, columns=["Name", "Age", "Salary"])
MM

MM.isnull().sum()

MM.Name.fillna("No_Name")

MM.Salary.fillna(method ='ffill')

"""Although It is filling but the data is not saved, So to that we need to use inplace as well"""

MM.Salary.fillna(method ='ffill', inplace = True)

df.rename(columns={'charges': 'Cost'}, inplace = True)
df

"""# Preprocessing

1. First step is  Identifying Your Data Type and the making the required chages to it so that your model can understand and process the data.

2. Your model can only take in numeric data so you will need to change the data to numeric data.

So what changes will you make to the following data?
"""

df.info()

for i in df.columns:
  print(f"Column {i} has {df[i].nunique()} values.")

"""## Categorical features:

When To use **Label encoder**  & **Onehot-encoding**


```
# pandas.get_dummies(data)
```


```
# label_encoder = preprocessing.LabelEncoder()

df[Colname]= label_encoder.fit_transform(df[Colname])
```




"""

cat = df.select_dtypes(include = object)
cat

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

for i in cat.columns:
  cat[i]= label_encoder.fit_transform(cat[i])


"""## Numeric Features


```
# from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[columnname] = scaler.fit_transform(df[[columnname]])
```


"""

Num = df.select_dtypes(exclude = object)
Num
Y = Num.pop('Cost')

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
Num['bmi'] = scaler.fit_transform(Num[['bmi']])

from joblib import dump

filename = 'Model/Numeric_model.joblib'
dump(scaler, filename)


"""## Combining The Data"""

X = pd.concat([cat,Num], axis = 1)
X

"""# Modeling

Linear Regression Formula:

```
y = b0 + b1x1 + b2x2 + ... + bpxp + ε
```






where:

1. y is the dependent variable
2. x1, x2, ..., xp are the independent variables
3. b0 is the y-intercept
4. b1, b2, ..., bp are the regression coefficients
5. ε is the error term
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2)

# Fit the linear regression model
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
# Predict the values
rmse = mean_squared_error(y_test, y_pred)
print('RMSE:', (rmse))

input = x_train.iloc[0].tolist()
orignal_error = y_train.iloc[0].tolist()
print(orignal_error)

x_train.iloc[0].tolist()

y_pred1 = model.predict([x_train.iloc[0]])
Predicted_error = y_pred1.tolist()[0]
print(f"Error rate is {orignal_error - Predicted_error}")

plt.scatter(y_pred,y_test)
plt.xlabel('True values (expenses)')
plt.ylabel('Predictions (expenses)')
lims = [0, 50000]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims,lims)
plt.title("Errors")

coef = model.coef_
coef

"""## Decision Tree

The DecisionTree Regressor builds a tree-like structure to predict continuous numerical values. It partitions the data based on feature values and computes the average of target values in leaf nodes to make predictions. Proper tuning of hyperparameters is essential to prevent overfitting and ensure optimal performance.



```
# Prediction = Average(Target Values in Leaf Node)
```


"""

from sklearn.tree import DecisionTreeRegressor


model = DecisionTreeRegressor(max_depth =  6, min_samples_leaf= 1 )


model.fit(x_train, y_train)

y_pred = model.predict(x_test)


rmse = mean_squared_error(y_test, y_pred)
print('RMSE:',rmse)

input = x_train.iloc[0].tolist()
orignal_error = y_train.iloc[0].tolist()
print(orignal_error)

x_train

input

y_pred1 = model.predict([input])
Predicted_error = y_pred1.tolist()[0]
print(f"Error rate is {orignal_error - Predicted_error}")

plt.scatter(y_pred,y_test)
plt.xlabel('True values (expenses)')
plt.ylabel('Predictions (expenses)')
lims = [0, 50000]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims,lims)
plt.title("Errors")

from sklearn import tree
a = tree.plot_tree(model, filled=True)
plt.rcParams['figure.figsize'] = [10,10]
plt.title("Visualiing Tree")

"""## Saving model"""

from joblib import dump

filename = 'Model/finalized_model.joblib'
dump(model, filename)

# some time later...

# load the model from disk
from joblib import load

loaded_model = load('Model/finalized_model.joblib')
result = loaded_model.predict(x_test)
rmse = mean_squared_error(y_test, result)
print('RMSE:',rmse)

