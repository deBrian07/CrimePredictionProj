import pandas as pd
import matplotlib.pyplot as plt

def dataTransform():
    # MERGING DATA
    # data1 = pd.read_csv('Crime_Data_from_2010_to_2019.csv')
    # data2 = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

    # merged_data = pd.concat([data1, data2])
    # merged_data.to_csv('data.csv')

    # IMPORT DATA
    data = pd.read_csv('data.csv')

    # print(len(data1) + len(data2))
    # print(len(data))

    # All the possible weapons
    # print("All possible weapon used: ")
    # weapons = data['Weapon Desc'].unique();
    # for i in range(0,len(weapons)):
    #     print(i, "   ", weapons[i]);

    # Frequency of each level of crime
    # frequency = data['Crm Cd Desc'].value_counts()
    # frequency.plot(kind = 'bar')
    # plt.show()
    # print(frequency.to_string())

    # Frequency of Crime in hour
    # time_in_hours = (data['TIME OCC'] / 100).round()
    # frequency = time_in_hours.value_counts()
    # print(frequency.to_string())

    # Dataframe with HOUR, COUNTY, MONTH
    # hour = (data['TIME OCC'] / 100).round()
    # county = data['AREA NAME']
    # month = data['DATE OCC'].str.split('/').str[0] # split with /, get the first element
    #
    # data2 = pd.concat([hour, county, month], axis = 1)
    # data2.to_csv('HourCountyMonth.csv')

    # Frequency by county
    #data2 = pd.read_csv('HourCountyMonth.csv')
    # frequency = data['AREA NAME'].value_counts()
    # frequency.plot(kind = 'bar')
    # plt.show()


dataTransform()