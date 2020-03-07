# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data=pd.read_csv(path)
#plt.hist(data['Rating'])
data['Rating'].plot(kind='hist')
plt.show()
data=data[data['Rating']<=5]
#plt.hist(data['Rating'])
data['Rating'].plot(kind='hist')
plt.show()

#Code ends here


# --------------
# code starts here
total_null=data.isnull().sum()
percent_null=total_null/data.isnull().count()
missing_data=pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
print(missing_data)

data.dropna(inplace=True)
total_null_1=data.isnull().sum()
percent_null_1=total_null_1/data.isnull().count()
missing_data_1=pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])
print(missing_data_1)
# code ends here


# --------------

#Code starts here
chart=sns.catplot(x="Category",y="Rating",data=data, kind="box",height = 10)
plt.xticks(rotation=90)
plt.title('Rating vs Category [BoxPlot]')
plt.show()



#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

#Removing `,` from the column
data['Installs']=data['Installs'].str.replace(',','')

#Removing `+` from the column
data['Installs']=data['Installs'].str.replace('+','')

#Converting the column to `int` datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le=LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs']=le.fit_transform(data['Installs'])

#Setting figure size
plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Installs[RegPlot]',size = 20)

#Code ends here



# --------------
#Code starts here
print(data['Price'].value_counts())
data['Price']=data['Price'].str.replace('$','')
data['Price']=data['Price'].astype(float)
sns.regplot(x="Price", y="Rating", data=data)
plt.title('Rating vs Price [RegPlot]')



#Code ends here


# --------------

#Code starts here

#Finding the length of unique genres
print( len(data['Genres'].unique()) , "genres")

#Splitting the column to include only the first genre of each app
data['Genres'] = data['Genres'].str.split(';').str[0]

#Grouping Genres and Rating
gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

print(gr_mean.describe())

#Sorting the grouped dataframe by Rating
gr_mean=gr_mean.sort_values('Rating')

print(gr_mean.head(1))

print(gr_mean.tail(1))

#Code ends here



# --------------

#Code starts here

#Converting the column into datetime format
data['Last Updated'] = pd.to_datetime(data['Last Updated'])

#Creating new column having `Last Updated` in days
data['Last Updated Days'] = (data['Last Updated'].max()-data['Last Updated'] ).dt.days 

#Setting the size of the figure
plt.figure(figsize = (10,10))

#Plotting a regression plot between `Rating` and `Last Updated Days`
sns.regplot(x="Last Updated Days", y="Rating", color = 'lightpink',data=data )

#Setting the title of the plot
plt.title('Rating vs Last Updated [RegPlot]',size = 20)

#Code ends here

