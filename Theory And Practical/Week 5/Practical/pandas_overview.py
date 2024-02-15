import numpy as np
import pandas as pd
## Series

series1=pd.Series([10, 20, 30, 40, 50],
                  index=['a', 'b','c','d','e'])
# print(series1)
# print(series1['a'])

student_names = {
    "Student1": "Zahir",
    "Student2": "Barry",
    "Student3": "Bruce Wayne"
}
series2 = pd.Series(student_names, index=["Student1", "Student3"])
# print(series2)
# print(series2["Student3"])


## Dataframes

# Via a dictionary
# data={
#     'Name': ['Batman', 'Superman', 'Wonderwoman', 'Flash', 'Cyborg'],
#     'True identity': ['Bruce Wayne', 'Clark Kent', 'Diana Prince', 'Barry Allen', 'Victor Stone']
# }
# df = pd.DataFrame(data)
# print(df)

# Via a python list
# data=[
#         ['Batman', 'Bruce Wayne'],
#         ['Superman', 'Clark Kent'],
#         ['Wonderwoman', 'Diana Prince' ],
#      ]
# df=pd.DataFrame(data, columns=["Name", "True Identity"])
# print(df)

# from a csv file
# df = pd.read_csv('credit.csv', delimiter=' ')
# print(df)

# empty dataframe
# df = pd.DataFrame()
# print(df)

## Index
# Default
# df = pd.read_csv('credit.csv', delimiter=' ')
# print(df)

# Setting index
# data={
#     'Name': ['Batman', 'Superman', 'Wonderwoman', 'Flash', 'Cyborg'],
#     'True identity': ['Bruce Wayne', 'Clark Kent', 'Diana Prince', 'Barry Allen', 'Victor Stone']
# }
# df = pd.DataFrame(data)
# df.set_index('Name', inplace=True)
# print(df)

# Range index
# student_grades = {
#     'Name': ['John', 'Joe', 'Sheldon'],
#     'Gpa': [3.1, 2.0, 3.5]
# }
# df = pd.DataFrame(student_grades, index=pd.RangeIndex(5, 8, name="custom_index"))
# print(df)

# Index renaming
# student_grades = {
#     'Name': ['John', 'Joe', 'Sheldon'],
#     'Gpa': [3.1, 2.0, 3.5]
# }
# df=pd.DataFrame(student_grades)
# df.rename(index={0:'A', 1:'B',2:'C'}, inplace=True)
# print(df)

## Pandas data cleaning

# Missing values 
# data = {
#     'A': [1,2,3, None, 5, 1,2,3, None, 5],
#     'B':[None,2,3,4,5, None,2,3,4,5],
#     'C':[1,2,None, None,5,1,2,None, None,5]
# }
# df=pd.DataFrame(data)
# print("Dirty dataframe")
# print(df)
# print("Clean dataframe")
# # clean_df=df.dropna()
# # print(clean_df)
# # df.fillna(0, inplace=True)
# df.fillna(df.mean(), inplace=True)
# print(df)

# Duplicates
data={
    'A':['1','2','2','3','3','4'],
    'B':[5, 6, 6, 7,7,8]
}

df=pd.DataFrame(data)
print(df)
print("These are the duplicates")
print(df[df.duplicated()]) # Returns the rows that are duplicates
df.drop_duplicates(subset=['A'], keep='first', inplace=True)
print("df without duplicates")
print(df)


# Aggregate
# data={
#     'Category': ['a','a','b', 'b'],
#     'Value': [10,15,20,25]
# }

# df =pd.DataFrame(data)
# print(f"Total sum: {df['Value'].aggregate('sum')}")
# print(f"Avg Value: {df['Value'].aggregate('mean')}")
# print(f"Max Value: {df['Value'].aggregate('max')}")
# print(f"Min Value: {df['Value'].aggregate('min')}")

# result = df.groupby('Category')['Value'].agg(['sum', 'mean','max', 'min'])
# print(result)