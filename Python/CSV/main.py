import pandas

data = pandas.read_csv('./squirrel_data.csv')
data['Primary Fur Color'].to_list()
Black = len(data[data['Primary Fur Color'] == 'Black'])
Cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
Gray = len(data[data['Primary Fur Color'] == 'Gray'])

print(Gray)
print(Cinnamon)
print(Black)

data_Dict = {
    "Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [Gray, Cinnamon, Black]
}

df = pandas.DataFrame(data_Dict)
df.to_csv("squirrel_number.csv")