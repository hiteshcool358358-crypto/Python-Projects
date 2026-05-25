#This program accepts tasks from the user and gives a to do list made to him
#Asking his task
ans="YES"
ToDoList=[]
while ans=="YES":
    task=input("Enter your task= ")
    ToDoList.append(task)
    ans=input("Do you want to add more tasks? (YES/NO)= ")
#Displaying the to do list
print("Your To Do List is:")
for task in ToDoList:
    print("- ", task)