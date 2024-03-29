# -*- coding: utf-8 -*-
"""Sreya Doppalapudi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YKaywvQ8a2KVmHIjGX-Zchf7Gtqoe4u-
"""

import pandas as pd
import scipy.stats as sci
import seaborn as sns
import matplotlib.pyplot as plt
xl = pd.ExcelFile("/content/TableauSalesData.xlsx")
Data = xl.parse("Orders")

#Obtain the goal of Increasing Profits by 10% through removing underperforming products. 
def menu():
  print("Obtain the goal of Increasing Profits by 10% through removing underperforming products.")
  while True:
    print("###############################################################################")
    print("\nWhich analytic would you like to see?\n")
    print("1: Regions by Lowest Profits")
    print("2: Central Region States by Lowest Profits")
    print("3: Comparison of Texas and Illinois Category's by Lowest Profits")
    print("4: Texas Sub-Categories by Lowest Profits")
    print("5: Texas Citys' Binder Quantities by Lowest Profits")
    print("6: Houston Binder Product Names by Lowest Profits")   
    userinp = input("\n\nEnter the number corrosponding to the analytic. Enter 0 to exit")
    print("###############################################################################")
    if userinp.isdigit() != True:
      print("\nPlease enter a number 1-6 OR enter 0 to exit.\n")
    elif int(userinp)==1:
      print("\nYou chose 1. Here are the Regions by Lowest Profits")
      regions()
    elif int(userinp)==2:
      print("\nYou chose 2. Here are the Central Region States by Lowest Profits")
      states()
    elif int(userinp)==3:
      print("\nYou chose 3. Here is the Comparison of Texas and Illinois Category's by Lowest Profits")
      TexIllCatProf()
    elif int(userinp)==4:
      print("\nYou chose 4. Here are the Texas Sub-Categories by Lowest Profits")
      TexasSubCatProf()
    elif int(userinp)==5:
      print("\nYou chose 5. Here are the Texas Citys' Binder Quantities by Lowest Profits")
      TexascityBinders()
    elif int(userinp)==6:
      print("\nYou chose 6. Here are the Houston Binder Product Names, Sales, and Quantity by Lowest Profits")
      HoustonBinders()
    elif int(userinp)==0:
      break
    else:
      print("Please enter a number 1-6 OR enter 0 to exit.")
menu()

#1 Regional Profits
def regions():
  Regions = Data[["Region","Profit"]].groupby(by="Region").sum()
  display(Regions)

#2 Central Regions States' Profits 
def states():
  Regions = Data[["Region","Profit"]].groupby(by="Region").sum()
  CentralRegion = Data.loc[Data["Region"]=="Central"]
  CentralRegionbyStateAscending = CentralRegion[["State", "Profit"]].groupby(by="State").sum().sort_values(by="Profit",ascending=True)
  display(CentralRegionbyStateAscending)

#3 The Texas category profits compared to Illinois
def TexIllCatProf():
  CentralRegion = Data.loc[Data["Region"]=="Central"]
  TexasCat = CentralRegion.loc[CentralRegion["State"]=="Texas"]
  TexasProf = TexasCat[["Category","Profit"]].groupby(by="Category").sum()
  IllinoisCat = CentralRegion.loc[CentralRegion["State"]=="Illinois"]
  IllinoisProf = IllinoisCat[["Category","Profit"]].groupby(by="Category").sum()
  print("****TEXAS CATEGORY PROFITS****")
  display(TexasProf)
  print("\n\n\n****ILLINOIS CATEGORY PROFITS****")
  display(IllinoisProf)

#4 the Texas Sub-category profits
def TexasSubCatProf():
  CentralRegion = Data.loc[Data["Region"]=="Central"]
  TexasCat = CentralRegion.loc[CentralRegion["State"]=="Texas"]
  TexasOfficeSupplies = TexasCat.loc[TexasCat["Category"]=="Office Supplies"]
  TexasSubcatOS = TexasOfficeSupplies[["Sub-Category", "Profit"]].groupby(by="Sub-Category").sum().sort_values(by="Profit", ascending=True)
  TexasSubcatOS = TexasSubcatOS.reset_index()
  barchart1 = sns.barplot(x="Sub-Category", y="Profit", data=TexasSubcatOS)
  barchart1.set_title("Texas Sub-Category Profits")
  print("\nThe Binders Sub-Categroy for Texas has significant profit loss compared to the other Sub-Categories")
  plt.show()
  display(TexasSubcatOS)

#5 Texas Citys' Binder Profits
def TexascityBinders():
  CentralRegion = Data.loc[Data["Region"]=="Central"]
  TexasCat = CentralRegion.loc[CentralRegion["State"]=="Texas"]
  TexasOfficeSupplies = TexasCat.loc[TexasCat["Category"]=="Office Supplies"]
  TexasBinders = TexasOfficeSupplies.loc[TexasOfficeSupplies["Sub-Category"]=="Binders"]
  TexasBinderNames = TexasBinders[["Product Name", "Profit"]].groupby(by="Product Name").sum().sort_values(by="Profit", ascending=True)
  TexasBinderCity = TexasBinders[["City", "Profit", "Quantity"]].groupby(by="City").sum().sort_values(by="Profit", ascending=True)
  #display(TexasBinderNames)
  #City binder profit
  TexasBinderCity = TexasBinderCity.reset_index()
  display(TexasBinderCity)

#6 Houston Binder Products, Quantity, and Sales by Lowest Profits
def HoustonBinders():
  HoustonTexas = Data.loc[Data["City"]=="Houston"]
  HoustonBinders = HoustonTexas.loc[HoustonTexas["Sub-Category"]=="Binders"]
  HoustonBindersProfit = HoustonBinders[["Product Name","Profit","Sales", "Quantity"]].groupby(by="Product Name").sum().sort_values(by="Profit", ascending=True)
  display(HoustonBindersProfit)
