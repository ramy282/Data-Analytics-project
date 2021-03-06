import pandas as pd
import seaborn as sns
import  numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from  sklearn import tree
from collections import Counter
from sklearn.cluster import DBSCAN
import graphviz
from numpy import where, datetime64
from sklearn.preprocessing import StandardScaler


#read data
data = pd.read_csv("C:\\Users\\Ramy Anwar\\Desktop\\kc_house_data.csv")

#3-describe dataset
des = data.describe()
shape = data.shape

print(des)
print(shape)

#4-data cleaning
data = data.drop_duplicates()
print(data.isna().sum())

#5-Data Visualization
#scatter plot
sns.scatterplot(x='price', y='sqft_living' , data=data )
plt.show()
#observation: the sqft is highly affecting on price

sns.scatterplot(x='price', y='bedrooms' , data=data )
plt.show()
#observation: no of rooms is highly affecting on price
sns.scatterplot(x='price', y='condition' , data=data )
plt.show()

#histogram
plt.hist(data['bedrooms'] , bins=range(1,1000))
plt.xlim([0,9])
plt.ylim([0,13000])
plt.xlabel("No of Bedrooms")
plt.ylabel("total apartement")
plt.show()

#observation: most of the apartement contains from 3 to 4 bedrooms

#7-anomloies detection

df=data.copy()
df=df.dropna()[['price','sqft_lot']]

stscaler = StandardScaler().fit(df)
df = pd.DataFrame(stscaler.transform(df))
print(df)
df.describe()

dbsc = DBSCAN(eps = 1.3, min_samples = 200).fit(df)
labels = dbsc.labels_
print(Counter(labels))

outliers=df[dbsc.labels_==-1]

#outliers
plt.scatter(df[0],df[1])
plt.scatter(outliers[0],outliers[1])
plt.xlabel('Price')
plt.ylabel('sqf_lot')
plt.show()

#8-Predictive Analysis
train = data.drop(['id','price' ,'sqft_lot','date','condition' ,'zipcode', 'sqft_above' , 'yr_renovated','sqft_living15' ], axis=1)
test = data ['price']

xtrain , xtest , ytrain , ytest = train_test_split(train , test , test_size=0.3 , random_state=9)
linear = LinearRegression()
linear.fit(xtrain, ytrain)
pred = linear.predict(xtest)
print("prediction")
print(pred)
print("score: ")
print(linear.score(xtest , ytest))

model = RandomForestRegressor(n_estimators=90)
model.fit(train , test)
prediction = model.predict(train)
print(model.feature_importances_)
print("score: ")
print(model.score(train , test))