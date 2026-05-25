'''This program will display a question to the user and ask for a guess and if the answr will match to the answers 
stored in the list, the user will get a point and it will also tell the score and percentage in the end of the 
execution.'''
#Preparing the set of questions and answer key.
countries = ["China", "India", "USA", "Russia", "Spain"]
capitals = ["Beijing", "New Delhi", "Washington D.C.", "Moscow", "Madrid"]
print ("What is the capital of the following countries:")
item = 0
score = 0
for x in countries:
    print(x)
    answer = input("Your answer: ")
    if answer == capitals[item]:
        score += 1
    item += 1
print(f"You made a score of {score}/5.")
print(f"It makes a percentage of {(score/5)*100}%.")