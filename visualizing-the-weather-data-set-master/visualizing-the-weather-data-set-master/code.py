# --------------
# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
from math import ceil
warnings.filterwarnings("ignore")

# https://seaborn.pydata.org/tutorial/categorical.html
# https://www.drawingfromdata.com/setting-figure-size-using-seaborn-and-matplotlib

# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature        based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
    if period=='day':
            df['period'] = df['Date/Time']
            plt.xticks(rotation=90)
    elif period=='month':
            df['period'] = df['Date/Time'].apply(lambda x:pd.to_datetime(x).month)
            plt.xticks(np.arange(1,13), calendar.month_name[1:13], rotation=90)
    elif period == 'year':
            df['period'] = df['Date/Time'].apply(lambda x:pd.to_datetime(x).year)
            plt.xticks(rotation=90)
    
    plt.plot(df.groupby(['period'])[col].mean())
    
    plt.title('Temperature Trend, 2012')
    plt.xlabel(period)
    plt.ylabel(col)
    plt.show()
    





# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar   
    plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    
    """
    categorical_columns = df.select_dtypes(include='object')

    for column in categorical_columns:
            df[column].value_counts(ascending=False).plot(kind='bar',figsize=(10,8),rot=90)

    """
    print(df.shape)
        
    sub_plot_total = len(categorical_columns)
    sub_plot_columns = 2
    sub_plot_rows = round(sub_plot_total / 2)
    #fig, ax = plt.subplots(sub_plot_rows,sub_plot_columns, figsize=(20,10))
    print(sub_plot_total)
    #print(ax)
    
    #print(type(categorical_columns))
    #print(categorical_columns.shape)
    #print(categorical_columns.columns)
    """






# Function to plot continous plots
def plot_cont(df,plt_typ):
    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    
    """
    
    







# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    df.groupby(col1).agg(agg1)[col2].plot(kind='bar')
    




# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df = pd.read_csv(path,sep=',',index_col='Date/Time',parse_dates=True)
#print(weather_df.select_dtypes(include='object'))
#print(weather_df.select_dtypes(include='number'))


# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
weather_df.reset_index(inplace=True)
#line_chart(weather_df,'month','Temp (C)')

# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.
weather_df.set_index('Date/Time',inplace=True)
#plot_categorical_columns(weather_df)


# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot



# Call the function "plot_cont()" with the appropriate parameters to plot boxplot


# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.
weather_df.groupby('Weather').agg({'Temp (C)':'mean','Wind Spd (km/h)':'mean','Dew Point Temp (C)':'mean','Rel Hum (%)':'mean','Wind Spd (km/h)':'mean','Visibility (km)':'mean','Stn Press (kPa)':'mean'})['Visibility (km)'].plot(kind='bar',figsize=(10,8),rot=90)




