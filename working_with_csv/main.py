# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temp = []
#     for row in data:
#        if row[1] != "temp":
#            temp.append(int(row[1]))
#
#     print(temp)
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)
# avg = sum(temp_list)/len(temp_list)
# print(avg)
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# print(data['condition'])
# print(data.condition)

# get data in rows
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp * 9/5 + 32)
# print(monday_temp)

# create dataFrame from Scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angy"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("squirrel_count.csv")
# print(type(data['Primary Fur Color'].value_counts()) )

table = data['Primary Fur Color'].value_counts()
table.to_csv("squirrels.csv")

# #Central Park Squirrel Data Analysis
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

