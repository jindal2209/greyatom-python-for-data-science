# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate((data,new_record))
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = np.mean(age)
age_std = age.std()
print(max_age)
print(min_age)
print(age_mean)
print(age_std)
race_0 = census[:,2][census[:,2] == 0]
race_1 = census[:,2][census[:,2] == 1]
race_2 = census[:,2][census[:,2] == 2]
race_3 = census[:,2][census[:,2] == 3]
race_4 = census[:,2][census[:,2] == 4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
for a in [race_0,race_1,race_2,race_3,race_4] :
    if len(a)==min(len_0,len_1,len_2,len_3,len_4):
        minority_race = a[0]
print(minority_race)
senior_citizens = census[:,0][census[:,0]>60]
working_hours_sum = census[:,6][census[:,0]>60].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = (working_hours_sum/senior_citizens_len).round(2)
print(avg_working_hours)
high = census[:,7][census[:,1]>10]
low = census[:,7][census[:,1]<=10]
avg_pay_high = high.mean().round(2)
avg_pay_low = low.mean().round(2)
print(avg_pay_high)
print(avg_pay_high>avg_pay_low)




#Code starts here




