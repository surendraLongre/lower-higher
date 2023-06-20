#import art and game_data
from art import logo, vs
from game_data import data
import random

# make functions here
def num_gen():
        return random.randint(0,50)


correct=True
score=0
while correct:
    num1=num_gen()
    num2=num_gen()
    while num1==num2:
        num2=num_gen()
    comp1=data[num1]
    comp2=data[num2]

    #get followers data
    if comp1['follower_count']>comp2['follower_count']:
        winner='A'
    else:
        winner='B'
    #print competitor1
    #print main logo
    print(logo)
    print(f"Compare A: {comp1['name']}, a {comp1['description']}, from {comp1['country']}.")

    #print vs logo
    print(vs)

    #print competitor 2
    print(f"Against B: {comp2['name']}, a {comp2['description']}, from {comp2['country']}.\n\n")

    #get user input
    user_input=input("Who has more followers? Type 'A' or 'B': ")
    if user_input==winner:
        score+=1
    else:
        correct=False
        print(f"Sorry, that's wrong. Final score: {score}")

    #update index and data
#    print("________________________________________________________________________________\n\n")



