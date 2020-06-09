import pandas as pd 

pd.set_option('display.expand_frame_repr', False)

def explore_data(df):
    print(df.head())
    print(df.info())
    print(df.isnull().sum())
    duplicates =df.duplicated()
    print(df[duplicates].sum())

#Loading file and checking sheet names
xls = pd.ExcelFile('KPMG_VI_New_raw_data_update_final.xls')
sheets = xls.sheet_names

#Exploring sheet1: Transactions
Transactions_df=pd.read_excel('KPMG_VI_New_raw_data_update_final.xls',
                              sheet_name = 1,
                              header=1) 
explore_data(Transactions_df)

##ISSUE1:Changing the type of product_first_sold_date to date##

Transactions_df['product_first_sold_date'] = pd.to_datetime(Transactions_df['product_first_sold_date'],
                                                             unit = 's')
print(Transactions_df.head(10))

##ISSUE2:dates referes to the same day with different time! CALRIFICATION NEEDED##
##ISSUE3:missing values choosing to drop them depends on the analysis ##

#Checking data consistancy
Tcol=list(Transactions_df.columns)
for col1 in Tcol[6:10]:
    print("this is colomn : ",col1)
    print(Transactions_df[col1].value_counts())



####################################################
#Exploring sheet2: NewCustomerList 

NewCustomerList_df = pd.read_excel('KPMG_VI_New_raw_data_update_final.xls',                              
                                   sheet_name = 2,
                                   header=1)
explore_data(NewCustomerList_df)

##ISSUE4:some null values that should be considered when analysing.##
##ISSUE5:unnamed columns starting from 16 to 20 should be dropped##

NewCustomerList_df= NewCustomerList_df.drop(NewCustomerList_df.columns[16:21]
                                            , axis=1)
print(NewCustomerList_df.info())

Ncol=list(NewCustomerList_df.columns)
for col2 in Ncol:
     print("this is colomn : ",col2)
     print(NewCustomerList_df[col2].value_counts())

#data seems to be consistant


#####################################################
#Exploring sheet3 CustomerDemographic 

CustomerDemographic_df=pd.read_excel('KPMG_VI_New_raw_data_update_final.xls',                              
                                    sheet_name = 3,
                                    header=1)
explore_data(CustomerDemographic_df)
Dcol=list(CustomerDemographic_df.columns)
for col4 in Dcol:
     print("this is colomn : ",col4)
     print(CustomerDemographic_df[col4].value_counts())

##ISSUE6:default column has nonsensedata##
     
#dropping default
#CustomerDemographic_df= CustomerDemographic_df.drop('default',axis=1)

##ISSUE7: gender column contains inconsistent values ##

CustomerDemographic_df['gender'] = CustomerDemographic_df['gender'].replace('F','Female').replace('Femal','Female').replace('M','Male').replace('U','Unspecified')
print(CustomerDemographic_df.head(10))

#####################################################
#Exploring sheet4: CustomerAddress 

CustomerAddress_df = pd.read_excel('KPMG_VI_New_raw_data_update_final.xls',
                                    sheet_name = 4,
                                    header=1)
explore_data(CustomerAddress_df)

##ISSUE8:CustomerAddress_df has more customer ids than transaction_df##


