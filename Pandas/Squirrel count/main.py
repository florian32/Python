import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = 0
cinnamon = 0
black = 0
print(data["Primary Fur Color"])
for color in data["Primary Fur Color"]:
    if color == "Gray":
        gray += 1
    elif color == "Black":
        black += 1
    elif color == "Cinnamon":
        cinnamon += 1


print(f"there are {gray} gray squirrels")
print(f"there are {black} black squirrels")
print(f"there are {cinnamon} red squirrels")

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Amount": [gray, cinnamon, black]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("color_count.csv")