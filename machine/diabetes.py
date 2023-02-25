import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
df = pd.read_csv('../nural/diabetes.csv')
df.loc[df['BloodPressure'] == 0, 'BloodPressure'] = 72
train, test = train_test_split(df, test_size=0.2)
# x_train , y_train
# x_test , y_test
train = pd.DataFrame(train)
x_train = train.drop(columns=["Outcome"], axis=1)
y_train = train["Outcome"]
model =LogisticRegression(max_iter=8500)
model.fit(x_train, y_train)
test = pd.DataFrame(test)
x_test = test.drop(columns=["Outcome"], axis=1)
y_test = test["Outcome"]
pred = model.predict(x_test)
print(accuracy_score(y_test, pred))

