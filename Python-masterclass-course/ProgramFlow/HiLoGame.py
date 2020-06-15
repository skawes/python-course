low = 1
high = 1000
guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input(
        "My guess is {},should I guess higher or lower,press h for higher,l for lower or c for correct".format(guess))
    if high_low=="h":
        low=guess+1
    elif high_low=="l":
        high=guess-1
    elif high_low=="c":
        print("No of guesses it took is {}".format(guesses-1))
        break
    else:
        print("Please enter h,l or c")
    guesses=guesses+1


