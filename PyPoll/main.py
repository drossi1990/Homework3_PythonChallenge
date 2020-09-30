#!/usr/bin/env python
# coding: utf-8

# In[99]:


import os
import csv


# In[100]:


file = 'budget_data.csv'
Total_Months = 0
Net_profit_loss = 0
Average_profit_loss = int
Row_count = 0 

Profit = 0
Last_Change_Profit=0
Change_Profit = 0
Profit_Change_List = []
Date_List = []


# In[101]:


with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        
        Profit = int(row[1])
        Change_Profit = (Profit - Last_Change_Profit)
        Profit_Change_List.append(Change_Profit)
        Date_List.append(row[0])
        Last_Change_Profit = Profit
        Net_profit_loss = (Net_profit_loss + Profit)
        Row_count = (Row_count + 1)
        


# In[102]:


Year_Seperator = "-20"
Greatest_Increase = max(Profit_Change_List)
Greatest_Increase_Date = Date_List[Profit_Change_List.index(Greatest_Increase)]
Greatest_Increase_Date_re = Year_Seperator.join(Greatest_Increase_Date.split('-'))
Greatest_Decrease = min(Profit_Change_List)
Greatest_Decrease_Date = Date_List[Profit_Change_List.index(Greatest_Decrease)]
Greatest_Decrease_Date_re = Year_Seperator.join(Greatest_Decrease_Date.split('-'))
Average_Change = sum(Profit_Change_List)


# In[103]:


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Row_count}")
print(f"Total: ${Net_profit_loss}")
print(f"Average Change: {Average_Change}")
print(f"Greatest Increase in Profits: {Greatest_Increase_Date_re} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date_re} (${Greatest_Decrease})")


# In[ ]:




