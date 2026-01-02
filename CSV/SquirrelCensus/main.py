import pandas as pd

data = pd.read_csv("CSV/SquirrelCensus/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

red_coats = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_coats = len(data[data["Primary Fur Color"] == "Gray"])
black_coats = len(data[data["Primary Fur Color"] == "Black"])
print(f"Cinnamon Coats: {red_coats} Gray Coats: {gray_coats} Black Coats: {black_coats}")

coat_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_coats, red_coats, black_coats]
}

df = pd.DataFrame(coat_dict)
df.to_csv("CSV/SquirrelCensus/squirrel_count.csv")