# --------------
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







