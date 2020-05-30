# --------------
import pandas as pd
df = pd.read_csv(path)
df["state"] = df["state"].apply(lambda x : x.lower())
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]
sum_row = df[['Jan','Feb','Mar','total']].sum()
df_final = pd.read_csv(path)
df_final = df_final.append(sum_row,ignore_index=True)
print(df_final)


# --------------
import requests

# Code starts here
url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
df1 = df1.iloc[11:]
df1.columns = df1.iloc[0]
df1 = df1[1:]

print(df1)


# Code ends here



# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)
# print(df1)
mapping = dict(zip(df1["United States of America"] ,df1['US']))
df_final['abbr'] = df_final['state'].map(mapping)
# print(df1.columns)
# Code starts here



# Code ends here


# --------------
# Code stars here
df_final['abbr'][df_final["state"] == "Mississipi"] = 'MS'
df_final['abbr'][df_final["state"] == "Tenessee"] = 'TN'

print(df_final)

# Code ends here


# --------------
# Code starts here
# print(df_final)
# mapping = dict(zip(df1["United States of America"] ,df1['US']))
# df_final['abbr'] = df_final['state'].map(mapping)
df_sub = df_final.groupby("abbr")[['abbr','Jan',"Feb","Mar","total"]].sum()
print(df_sub)
formatted_df = df_sub.applymap(lambda x : "${}".format(x))
print(formatted_df)
# Code ends here


# --------------
# Code starts here
sum_row = df[["Jan","Feb","Mar","total"]].sum()
df_sub_sum = sum_row.T
df_sub_sum = df_sub_sum.apply(lambda x : "${}".format(x))
final_table = formatted_df.append(df_sub_sum,ignore_index=True)


# Code ends here


# --------------
# Code starts here
df_sub['total'] = df_sub[['Jan','Feb',"Mar"]].sum()
df_sub['total'].plot.pie()
print(df_sub['total'])

# Code ends here


