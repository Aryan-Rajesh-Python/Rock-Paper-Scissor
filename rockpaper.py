import random
def game():
    a=int(input("Enter a number for rock or paper or scissor: "))
    b=random.randint(0,2)
    if(a==0 and b==0):
        print("Draw")
    elif(a==0 and b==1):
        print("Computer Won")
    elif(a==0 and b==2):
        print("You won")
    elif(a==1 and b==0):
        print("You won")
    elif(a==1 and b==1):
        print("Draw")
    elif(a==1 and b==2):
        print("Computer won")
    elif(a==2 and b==0):
        print("Computer won")
    elif(a==2 and a==1):
        print("You won")
    elif(a==2 and b==2):
        print("Draw")
    elif(a<0 and a>2):
        print("Please give the correct input!")
game()
while(True):
    opinion=input("Do you want to play the game or you want to exit the game: ")
    if(opinion=="yes" or opinion=="Yes" or opinion=="YES"):
        game()
    else:
        print("Thank you for playing our game!!")
        break
        
