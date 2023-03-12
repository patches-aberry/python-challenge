#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd


# In[87]:


#define file path
path = "Resources/election_data.csv"
#read CSV data to data frame
ed_df = pd.read_csv(path)


# In[88]:


#count number of votes cast
total_votes = ed_df["Ballot ID"].count()


# In[89]:


#create list of candidates
can_list = ed_df["Candidate"].unique()
#create empty arrays to hold totals and percent values. 
can_tot = [0] * len(can_list)
can_per = [0] * len(can_list)


# In[90]:


#Loop through list of candidates, add to arrays of values depending on how they performed. 
for i in range(len(can_list)):
    count_list = ed_df.loc[ed_df["Candidate"]==can_list[i],["Ballot ID"]]
    #Add to list of candidates totals
    can_tot[i] = count_list["Ballot ID"].count()
    #Add to list of candidates percentages
    can_per[i] = can_tot[i] / total_votes
    #format percentage
    can_per[i] = can_per[i]*100
    can_per[i] = "%.3f" % can_per[i]


# In[81]:


#Grab winner name
winner_name = can_list[can_tot.index(max(can_tot))]


# In[82]:


#create output in terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for j in range(len(can_list)):
    print (can_list[j] + ": " + str(can_per[j]) + "% (" + str(can_tot[j]) + ")")
print("-------------------------")
print("Winner: " + winner_name)
print("-------------------------")


# In[83]:


#Write file out
with open("analysis/Output.txt", "w") as text_file:
    text_file.write("Election Results" + "\n")
    text_file.write("-------------------------"+ "\n")
    text_file.write("Total Votes: " + str(total_votes)+ "\n")
    text_file.write("-------------------------"+ "\n")
    for j in range(len(can_list)):
        text_file.write(can_list[j] + ": " + str(can_per[j]) + "% (" + str(can_tot[j]) + ")"+ "\n")
    text_file.write("-------------------------"+ "\n")
    text_file.write("Winner: " + winner_name + "\n")
    text_file.write("-------------------------"+ "\n")

