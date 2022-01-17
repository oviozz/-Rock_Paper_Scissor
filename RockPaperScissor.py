import random
you_Score = 0
bot_Score = 0
print("********************************")
print(" WELCOME TO ROCK,PAPER,SCISSORS")

number = random.randint(0,3)
list = ["Rock","Paper","Scissor"]
print("Choose One:",", ".join(list))
answer = ['yes','no']

Playagain = "yes"
while Playagain == "yes":
    bot = random.choice(list)
    user = input("Pick One: ").capitalize()

    while user not in list:
        print("Invalid Response")
        user = input("Pick One: ").capitalize()

    #if user and bot ties
    if user == bot:
        print("You Both Tied")
        print("Bot Picked:", bot)
        you_Score+=1
        bot_Score+=1
        print("___________________________")
        print("Your Score:",you_Score)
        print("Bot Score:", bot_Score)
        print("___________________________")

    #if user win win
    elif user == "Rock" and bot == "Scissor":
        print("You Won")
        print("Bot Picked:", bot)
        you_Score+=1
        print("___________________________")
        print("Your Score:", you_Score)
        print("Bot Score:", bot_Score)
        print("___________________________")


    elif user == "Paper" and bot == "Rock":
        print("You Won")
        print("Bot Picked:", bot)
        you_Score+=1
        print("___________________________")
        print("Your Score:", you_Score)
        print("Bot Score:", bot_Score)
        print("___________________________")


    elif user == "Scissor" and bot == "Paper":
        print("You Won")
        print("Bot Picked:", bot)
        you_Score+=1
        print("___________________________")
        print("Your Score:", you_Score)
        print("Bot Score:", bot_Score)
        print("___________________________")


    #if bot wins

    elif user == "Scissor" and bot == "Rock":
        print("You Lost")
        print("Bot Picked:", bot)
        bot_Score+=1
        print("___________________________")
        print("Your Score:", you_Score)
        print("Bot Score:", bot_Score)
        print("___________________________")


    elif user == "Rock" and bot == "Paper":
        print("You Lost")
        print("Bot Picked:", bot)
        bot_Score+=1
        print("___________________________")
        print("Your Score:", you_Score)
        print("Bot Score:", bot_Score)
        print("___________________________")


    elif user == "Paper" and bot == "Scissor":
        print("You Lost")
        print("Bot Picked:", bot)
        bot_Score+=1
        print("___________________________")
        print("Your Score:", you_Score)
        print("Bot Score:", bot_Score)
        print("___________________________")

    Playagain = input("Do you want to play again: yes/no: ").lower()

    #ask user input to play (if not yes or no) return not a valid response
    while Playagain not in answer:
        print("Not a Valid Response")
        Playagain = input("Do you want to play again: yes/no: ").lower()

    if Playagain == "no":
        if you_Score == bot_Score:
            print("****************You Tied!****************")
        if you_Score > bot_Score:
            print("****************You Win!****************")
        if you_Score < bot_Score:
            print("****************Bot Win!****************")

        print("**********Thanks for playing!***********")
        print("**********Created by Prazwal************")
        exit()
