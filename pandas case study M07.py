import pandas as pd 
pd

#CREATE 

# Create from a CSV
df = pd.read_csv('telco_churn.csv')

# Create from a Dictionary
tempdict = {'col1':[1,2,3],'col2':[4,5,6],'col3':[7,8,9]}
dictdf = pd.DataFrame.from_dict(tempdict)

# READ

# show Top 5 and Bottom 5 Rows
df.head(10)

dictdf.head()
df.tail(15)

# Show Columns and Data Type
df.columns 
df.dtypes

#Summary Statistics
df.describe(include='object')

#Filtering Colums
df.State 
df['International plan']
df[['State', 'International plan']]
df.State.unique()

#Filtering on rows
df.head()
df[df['International plan']=='No']
df[(df['International plan']=='No') & (df['Churn']==False)]

#Indexing with iloc
df.iloc[14]
df.iloc[14,0]
df.iloc[22:33]

#indexing with loc
state = df.copy()
state.set_index('State', inplace=True)
state.head()
state.loc['OH']

#UPDATE

# Dropping Rows
df.isnull().sum()
df.dropna(inplace=True)
df.isnull().sum() 

#Dropping Colums
df.drop('Area Code', axis=1)

#Creating Calculated Columns
df['New Column'] = df['Total night minutes'] + df['Total intl minutes']
df.head()

#Updating an Entire Column
df['New Column'] = 100
df.head()

#Updating a Single Value
df.iloc[0,-1] = 10
df.head()

# Condition based Updating using Apply
df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)
df[df['Churn']==True].head()

# Delete/Output

#Output to CSV
df.to_csv('output.csv')

#Output to JSON
df.to_json()

#Output to HTML
df.to_html()

#Delete a DataFrame
del df


