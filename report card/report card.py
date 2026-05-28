#This program asks for the important infos of the student from the teacher and make the report card in a .csv file i.e., "report card.csv"
#Asking the infos
name = input("Enter the student's name: ")
cl = input("Enter the student's class: ")
roll = input("Enter the student's roll number: ")
math = input("Enter the student's total marks in Maths: ")
phy = input("Enter the student's total marks in Physics: ")
chem = input("Enter the student's total marks in Chemistry: ")
bio = input("Enter the student's total marks in Biology: ")
his = input("Enter the student's total marks in History and Civics: ")
geo = input("Enter the student's total marks in Geography: ")
#Creating the file
file_path = r"C:\Python\report card\report card.csv"
with open(file_path, "w") as f:
    #writing in the file
    f.write("Name: ," + name + "\n")
    f.write("Class: ," + cl + "\n")
    f.write("Roll Number: ," + roll + "\n")
    f.write(" \n")
    f.write("Subject, Total Marks\n")
    f.write("Mathematics," + math + "\n")
    f.write("Physics," + phy + "\n")
    f.write("Chemistry," + chem + "\n")
    f.write("Biology," + bio + "\n")
    f.write("History," + his + "\n")
    f.write("Geography," + geo + "\n")
'''The .csv file which is conatining the report card will change everytime when the program is ran till ln11 but if the program is not ran till
ln11 there will be no change in the file and if there will be no file created beforehand, the program will not be able to create it also.'''
