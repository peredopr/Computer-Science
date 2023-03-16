import pandas as pd
#import csv

#with open("weather_data.csv", "r") as data_file:
    #data = csv.reader(data_file)
    #temperatures = []
    #for row in data:
        #if row[1] != "temp":
            #temperatures.append(int(row[1]))
#print(temperatures)

data = pd.read_csv("./weather_data.csv")

temperatures = data['Temperature'].to_list()
print(temperatures)
print("\n")

print(data[data.Temperature == data.Temperature.min()])
print(data[data.Temperature == data.Temperature.max()])
print("\n")

monday = data[data.Day == "Monday"]
monday_temp = monday.Temperature * 9/5 + 32
print(monday_temp)
print("\n")

data_dict = {
    "Movies" : ["Iron Man", "Thor", "Spider-man"],
    "Ratings" : ["9.7", "9.6", "9.9"]
}

dataframe = pd.DataFrame(data_dict)
print(dataframe)