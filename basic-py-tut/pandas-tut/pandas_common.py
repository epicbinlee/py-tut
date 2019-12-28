import pandas as pd

train = pd.read_csv(r"data/train.csv")
# print(train.head(5))

columns = train.columns.values.tolist()
print(columns)

info = train.info()
# print(info)

age_list = train['Age'].tolist()
# print(age)

age_array = train['Age'].values
# print(age_array)

age_1 = train['Age'][1]
# print(age_1)

# for k, v in train.iteritems():
# print(v)

# for x in train.itertuples():
# print(x)

# for idx, row in train.iterrows():
# print(row['Name'])

# for k, v in train.groupby(train['Pclass']):
# print(v.shape)

# train_sub = train[['Name', 'Age', 'Pclass']]
# train_sub_selected = train_sub[train_sub['Pclass'] == 1].reset_index(drop=True)
# print(train_sub_selected)

# for k, v in train.groupby(train['Pclass']):
#     v1 = v[['Pclass', 'Name']].sort_values(by='Name', ascending=False)[2:5]
#     print(v1)
