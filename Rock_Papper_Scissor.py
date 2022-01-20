import random
print("Welcome To The Rock_Paper_Scissor Game By Soumil_Dureja!")
user=input("Enter Your Action:")
possible=["rock","paper","scissors"]
computer=random.choices(possible)
print(f"You Chose {user}, Computer Chose {computer[0]}")

if user==computer[0]:
    print(f"Its A Tie, You Both Chose{user}")
elif user=='paper':
    if computer[0]=='scissors':
        print("scissors Cuts paper, you lost")
    else:
        print("paper catches rock, you win")

elif user=='scissors':
    if computer[0]=='paper':
        print("scissors Cuts paper, you win")
    else:
        print("rock smaches scissors, you lose")

elif user=='rock':
    if computer[0]=='paper':
        print("paper catches rock, you lose")
    else:
        print("rock smashes scissors, you win!!")



