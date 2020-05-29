# --------------
# MY CODE
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank = pd.read_csv(path)

#Code starts here
categorical_var = bank.select_dtypes(include ='object')
print(categorical_var)
numerical_var = bank.select_dtypes(include ='number')
print(numerical_var)
banks = bank.drop("Loan_ID",axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
print(bank_mode)
banks = banks.fillna(bank_mode)
print(banks)
avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount')
print(avg_loan_amount)
loan_approved_se =  len(banks[banks["Self_Employed"]=="Yes"][banks[banks["Self_Employed"]=="Yes"]["Loan_Status"] == "Y"])
print(loan_approved_se)
loan_approved_nse =  len(banks[banks["Self_Employed"]=="No"][banks[banks["Self_Employed"]=="No"]["Loan_Status"] == "Y"])
print(loan_approved_nse)
percentage_se = round((loan_approved_se/614)*100,2)
percentage_nse = round((loan_approved_nse/614)*100,2)
loan_term = banks["Loan_Amount_Term"].apply(lambda x:x/12)
big_loan_term = len(loan_term[loan_term >= 25])
loan_groupby = banks.groupby("Loan_Status")
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()





## Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 



# code starts here
# GREY ATOM CODE
#Load Dataset

bank = pd.read_csv(path)
    
# Display categorical variable

categorical_var=bank.select_dtypes(include='object')
print("Categorical variables : ",categorical_var)

#Code for numerical variable

numerical_var=bank.select_dtypes(include='number')
print("Numerical Variables : ",numerical_var)

# load the dataset and drop the Loan_ID
banks= bank.drop(columns='Loan_ID')


# check  all the missing values filled.
print(banks.isnull().sum())

# apply mode 
bank_mode = banks.mode().iloc[0]

# Fill the missing values with 
banks.fillna(bank_mode, inplace=True)

# check again all the missing values filled.
print(banks.isnull().sum())

# check the avg_loan_amount
avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)
print (avg_loan_amount)

# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]

# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]

#print percentage of loan for non self employed
print (percentage_nse)

# loan amount term 
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )

big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])
print(mean_values)


