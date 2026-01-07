import pandas as pd

df = pd.read_csv(r'E:\KBK\python\Book\data\welfare.csv')

# print(df.head())
# print(type(df))
# print(df.shape)
# print(df.shape[0])
# print(df.shape[1])
# print(df.columns)
# print(df.dtypes)
# print(df.info())

print('\n# gender_df')
gender_df = df['gender']
print(gender_df)

subset = df[['gender', 'birth', 'marriage']]
print(subset.head())
print(subset.tail())

# print(df.loc[0])
# print(df.loc[99])

number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1
print(df.loc[last_row_index])

# print(df.tail(n = 1))
# print(df.tail(n = 2))
# print(df.loc[[0, 99, 999]])

subset_loc = df.loc[0]
subset_tail = df.tail(n = 1)
print(type(subset_loc))
print(type(subset_tail))

# GroupBy

print(df['marriage'].unique())
print(df.groupby('marriage')['code_religion'].mean())

mygrouping = df.groupby('marriage')
print(type(mygrouping))
print(mygrouping)

grp_code_religion = mygrouping['code_religion']
print(type(grp_code_religion))

mean_code_religion = grp_code_religion.mean()
print(mean_code_religion)

multi_group_var = df.groupby(['marriage', 'birth'])[['code_religion', 'income']].mean()
print(multi_group_var)
print(type(multi_group_var))