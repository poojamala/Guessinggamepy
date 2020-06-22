n=18
i=1
# print("Number of guesses is limited to only 9 times: ")
while (i<=9):
    n = int(input("Guess the number :\n"))
    if n<18:
        print("you enter less number please input greater number.\n")
    elif n>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(i,"no.of guesses he took to finish.")
        break
    print(9-i,"no. of guesses left")
    i = i + 1
if(n>9):
    print("Game Over")



