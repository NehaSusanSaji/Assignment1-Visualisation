# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:29:03 2023

@author: neham
"""

import pandas as pd
import matplotlib.pyplot as plt


def lineplot(df):
    """ 
    Function to plot a line graph.
    Argument: A dataframe 
    
    The function is called and a dataframe is passed on to the function
    as the argument.The function then plots a line graph using the data 
    from the dataframe.
    
    """    
    plt.figure()
    
    #variable to store the list of countries
    countries = ['Afghanistan', 'Bhutan']
    
    #plots the line graph with the year column as x-axis and the percentage 
    #of population as the y-axis
    plt.plot(df['Year'], df[countries])
    
    #gives the respective labels to the x and y axes
    plt.xlabel("Year")
    plt.ylabel("Percentage of Population")
    
    #gives the title of the plot
    plt.title("Access of electricity to percentage of population in\n" +
              "Afghanistan and Bhutan over 10 years")
    
    #sets the limits of x and y axes 
    plt.ylim(40)
    plt.xlim(2011, 2020)
    
    #gives the list as the ticks of x-axis 
    plt.xticks([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    
    #shows the legend of the plot at the specified location
    plt.legend(countries, loc='lower right')
    
    plt.show()
    return
    

def barplot(df):
    """
    Function to plot a bar graph.
    Argument: A dataframe
    
    The function is called and a dataframe is passed on as the argument. The
    function then plots a bar graph using the data given in the dataframe.
    
    """
    plt.figure()
    
    #plots the bar graph with countries column as the x-axis and percentage 
    #column as the y-axis and the bars with the specified width
    plt.bar(df["Countries"], df["Percentage"], width=0.8)
    
    #gives the plot the specified title
    plt.title("Renewable energy consumption of 7 European Countries\n"
              + "in 2019")
    
    #gives the limit to the y-axis
    plt.ylim(0, 70)
    
    #shows the ticks of x-axis vertically
    plt.xticks(rotation='vertical')
    
    #gives the specified labels to the x and y axes respectively
    plt.xlabel("Country")
    plt.ylabel("Renewable energy consumption (in %)")
    
    plt.show()
    return


def piechart(df):
    """
    Function to plot a pie chart.
    Argument: A dataframe
    
    The function is called and a dataframe is passed on as the argument. 
    Then the function plots a pie chart using the data from the dataframe.

    """
    plt.figure()
    
    #plots the pie chart with MtCO₂e column as the division factor of the 
    #pie and Country column as the labels, with the specific percentages in
    #each wedges
    plt.pie(df["MtCO₂e"], labels=df["Country"], autopct='%0.1f%%',\
            pctdistance=0.8)
    
    #shows the legend in the specified location
    plt.legend(df["MtCO₂e"], loc='best', bbox_to_anchor=(-0.5,0.8,0.2,0.2),\
               fontsize='small', title='in MtCO₂e')
    
    #shows the specified title
    plt.title("Greenhouse gas emissions (in MtCO₂e) of top 10 emitters\n"\
              + "in the year 2019")
        
    plt.show()
    return


#reads in the excel file as dataframe and is stored in df_electricity
df_electricity = pd.read_excel("Access to electricity.xlsx")
print(df_electricity,'\n')
lineplot(df_electricity)       #calls the function lineplot()


#reads in the excel file as dataframe and is stored in df_energy
df_energy = pd.read_excel("Renewable energy consumption.xlsx")
print(df_energy,'\n')
barplot(df_energy)             #calls the function barplot()


#reads in the excel file as dataframe and is stored in df_ghemission
df_ghemission = pd.read_excel("Greenhouse gas emissions.xlsx")
print(df_ghemission,'\n')  
piechart(df_ghemission)        #calls the function piechart()  

