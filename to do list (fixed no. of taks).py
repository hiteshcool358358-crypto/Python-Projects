#This program accepts tasks from the user and gives a to do list made to him
#Asking his task
print("How many tasks will you be entering? ")
n=int(input(""))
ToDoList=[]
for i in range(1,(n+1)):
    task=input("Enter your task= ")
    ToDoList.append(task)
#Displaying the to do list
print("Your To Do List is:")
for task in ToDoList:
    print("- ", task)