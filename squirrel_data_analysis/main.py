import pandas
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = squirrel_data["Primary Fur Color"]

black = 0
gray = 0
cinnamon = 0
No_Data = 0

for n_color in color:
    if n_color == "Gray":
        gray += 1
    elif n_color == "Cinnamon":
        cinnamon += 1
    elif n_color == "Black":
        black += 1
    else:
        No_Data += 0

squirrel_Count = {

    "Fur Color": ["gray", "cinnamon", "black", "No_Data"],
    "Count": [gray, cinnamon, black, No_Data]

}

Final_Squirrel_Count = pandas.DataFrame(squirrel_Count)

Final_Squirrel_Count.to_csv("Total_squirrel_by_color.csv")
