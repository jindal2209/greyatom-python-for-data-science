# --------------
# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)

data.rename(columns = {'Total':'Total_Medals'},inplace = True)

# Summer or Winter
data["Better_Event"] = np.where(data["Total_Summer"]>=data["Total_Winter"], "Summer", "Winter")

# data["Better_Event"] = np.where(data["Total_Summer"]==data["Total_Winter"], "Both", data["Better_Event"])

better_event = data["Better_Event"].value_counts().reset_index().iloc[0,0]

print(better_event)


print(data.head(5))
# Top 10
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)
def top_ten(df, col):
    country_list = []
    temp = list(df.nlargest(10, col)["Country_Name"])
    country_list.extend(temp)
    return country_list 

top_10_summer = top_ten(top_countries,"Total_Summer")
top_10_winter = top_ten(top_countries, "Total_Winter")
top_10 = top_ten(top_countries, "Total_Medals")

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)
# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
# print(summer_df)
winter_df = data[data['Country_Name'].isin(top_10_winter)]
# print(winter_df)
top_df = data[data['Country_Name'].isin(top_10)]
print(top_df)
summer_df.plot(x = 'Country_Name',y = 'Total_Summer',kind = 'bar')
plt.show()
winter_df.plot(x = 'Country_Name',y = 'Total_Winter',kind = 'bar')
plt.show()
top_df.plot(x = 'Country_Name',y = 'Total_Medals',kind = 'bar')
plt.show()
# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
# summer_df = summer_df.set_index('Country_Name')
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df['Golden_Ratio'].idxmax()
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
# winter_df = winter_df.set_index('Country_Name')
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df['Golden_Ratio'].idxmax()
print(winter_country_gold)
print('---------------------------------------------------------------')
top_df["Golden_Ratio"] = top_df["Gold_Total"] / top_df["Total_Medals"]
top_country_gold_index = top_df["Golden_Ratio"].idxmax()
top_country_gold = top_df["Country_Name"][top_country_gold_index]
top_max_ratio = top_df["Golden_Ratio"].max()
# Best in the world 
data.drop(data.tail(1).index,inplace=True)
data_1 = data
# print(data_1.head(2))
data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + data_1['Bronze_Total']
data_1 = data_1.set_index('Country_Name')
most_points = max(data_1['Total_Points'])
best_country = data_1['Total_Points'].idxmax()
print(best_country)

# Plotting the best
# print(data.tail(2))
best = data[data["Country_Name"] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation =45)


