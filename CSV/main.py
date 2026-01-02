# data = []
# with open("CSV/weather_data.csv", "r") as file:
#     for line in file:
#         data.append(line.strip())

# print(data)

# import csv

# with open("CSV/weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     # data = csv.DictReader(file)
#     temp = []
#     for row in data:
#         # temp.append(int(row["temp"]))  # Used with DictReader()
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)
    

import pandas 

# data = pandas.read_csv("CSV/weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].tolist()
# average_temp = sum(temp_list) / len(temp_list)  Same as the line below
# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()
# print(max_temp)

# Data in a row
# print(data[data.temp == data.temp.max()])

# Convert Monday temp to fahrenheit
# monday_temp = data.at[0, "temp"]
# fahrenheit_temp = (monday_temp * 9 / 5) + 32
# print(fahrenheit_temp)

# Create data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("CSV/new_data.csv")
print(data)