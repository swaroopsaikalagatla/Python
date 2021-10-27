user1=input("What's your name?")
user2=input("What's your name?")
user1_answer=input("%s,do yo want to choose rock,paper or scissors?"% user1)
user2_answer=input("%s,do you want to choose rock,paper or scissors?"% user2)
def compare(u1,u2):
    if u1==u2:
        return("It's a tie!")
    elif u1=='rock':
        if u2=='scissors':
            return("Rock Wins!")
        else:
            return("Paper wins!")
    elif u1 == 'Scissors':
        if u2=='paper':
            return("Scissors Wins!")
        else:
            return("Rock Wins!")
    elif u1 == 'paper':
        if u2 =='rock':
            return("Paper wins!")
        else:
            return("Scissors Wins!")
    else:
        return("Invalid Input! You are not entered rock,paper or scissors,try again.")
        sys.exit()
print(compare(user1_answer, user2_answer))