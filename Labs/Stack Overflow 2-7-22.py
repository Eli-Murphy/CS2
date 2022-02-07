mdrl = [
    ["Munich: The Edge of War", "Christian Schwochow", "4.1"],
    ["Avengers:Endgame", "Anthony Russo, Joe Russo and Joss Whedon", "4.8"],
    ["Tombstone", "Cosmatos and Kevin Jarre", "4.1"],
    ["Waterloo", "George P. and Sergei Bondarchuk", "4.0"],
    ["Iron Man", "Jon Favreau", "4.9"]
]

movieChoice = input("Which movie would you like to get data from?: ")

for i in range(len(mdrl)):
    if mdrl[i][0] == movieChoice:
        print(mdrl[i][0], "Was directed by", mdrl[i][1], "and had a rating of ", mdrl[i][2])