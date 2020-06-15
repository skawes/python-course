locations = {0: "you are sitting in front of comp game",
             1: "you are at the end of a road ",
             2: "you are sitting at the top of hill",
             3: "you ae in the building",
             4: "you are in the valley",
             5: "you are in the forest"}
exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]
print(locations[0].split(" "))
loc = 1
while True:

    available_direction = ",".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        print("Exited")
        break
    print(available_direction)
    path = input("Enter your direction")
    if path in exits[loc]:
        loc = exits[loc][path]
    else:
        print("You cannot go in that direction")
