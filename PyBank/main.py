#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[133]:


#define file path
path = "Resources/budget_data.csv"
#read CSV data to data frame
bd_df = pd.read_csv(path)


# In[134]:


# * The total number of months included in the dataset
tot_months = bd_df["Date"].count()


# In[50]:


#Create a copy of the main data frame
change_df = bd_df.copy()

#insert "Change" column
change_df["Change"]=0


# In[135]:


#initialize our change_var at 0.
change_var = 0 

#Loop through DataFrame 
for i in change_df.index:
    #this if loop skips the top row calculation to avoid an exception. 
    if i > 0:
        change_var = change_df["Profit/Losses"][i] - change_df["Profit/Losses"][i-1]
    elif i == 0:
        change_var = 0
    #set the change column value to the change var caculated on the previous row
    change_df["Change"][i] = change_var


# In[136]:


#* The net total amount of "Profit/Losses" over the entire period
net_total = bd_df["Profit/Losses"].sum()


# In[137]:


#* The changes in "Profit/Losses" over the entire period, and then the average of those change
avg_change = change_df["Change"].mean()
avg_change = "%.2f" % avg_change


# In[138]:


#* The greatest increase in profits (date and amount) over the entire period
max_increase = change_df["Change"].max()
#find index value of date of max increase
date_index_in = change_df.loc[change_df["Change"] == max_increase].index


# In[139]:


#* The greatest decrease in profits (date and amount) over the entire period
max_decrease = change_df["Change"].min()
#find index value of date of max decrease
date_index_de = change_df.loc[change_df["Change"] == max_decrease].index


# In[124]:


#Your analysis should look similar to the following:

#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $22564198
 # Average Change: $-8311.11
 # Greatest Increase in Profits: Aug-16 ($1862002)
#  Greatest Decrease in Profits: Feb-14 ($-1825558)
#  ```

print( "Financial Analysis" )
print(" ----------------------------" )
print("Total Months: " + str(tot_months) )
print("Total: " + str(net_total) )
print("Average Change: $" + avg_change)
print("Greatest Increase in Profits: " + change_df.iat[date_index_in[0], 0] + " ($" + str(max_increase) + ")")
print("Greatest Decrease in Profits: " + change_df.iat[date_index_de[0], 0] + " ($" + str(max_decrease) + ")")


# In[132]:


#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
with open("analysis/Output.txt", "w") as text_file:
    text_file.write( "Financial Analysis\n")
    text_file.write(" ----------------------------\n" )
    text_file.write("Total Months: " + str(tot_months)+'\n' )
    text_file.write("Total: " + str(net_total) +"\n")
    text_file.write("Average Change: $" + avg_change+"\n")
    text_file.write("Greatest Increase in Profits: " + change_df.iat[date_index_in[0], 0] + " ($" + str(max_increase) + ")\n")
    text_file.write("Greatest Decrease in Profits: " + change_df.iat[date_index_de[0], 0] + " ($" + str(max_decrease) + ")")

