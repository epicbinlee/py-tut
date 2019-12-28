import pandas as pd

test_dict = {'id': [1, 2, 3, 4, 5, 6],
             'name': ['Alice', 'Bob', 'Bob', 'Eric', 'Bob', 'Eric'],
             'math': [90, 89, 99, 78, 97, 93],
             'english': [89, 94, 80, 94, 94, 90]}
test_dict_df = pd.DataFrame(test_dict)

gp1 = test_dict_df.groupby('name')
for idx, content in gp1:
    print(idx)
    print(content)

gpd = gp1.describe()
print(gpd)

mens = test_dict_df.groupby('name')['math'].sum()
# print(mens)
