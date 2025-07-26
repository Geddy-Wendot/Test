banned_words = ["idiot", "stupid", "dumb", "foolish" ]

while True:
    user_input = input("Enter a sentence: ")
    if user_input == "exit":
        print("Exiting the program.")
        break

    if any(word in user_input for word in banned_words):
        print("Your input contains banned words. Please try again.")
        continue
    else:
        print("Your input is clean.")


    print("message sent!  " ,user_input)
    
