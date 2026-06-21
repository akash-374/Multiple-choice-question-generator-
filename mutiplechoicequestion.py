question={"""1.Which data structure is 
used to store tasks in the project?""":
["A) Tuple",
"B) Dictionary",
"C) List",
"D) Set"],
"2. What happens when a task is moved to the Processing stage?":
["A) It is deleted permanently",
"B) It is copied to Completed Tasks",
"C) It is removed from Pending Tasks and added to Processing Tasks",
"D) Nothing happens"],
"""3. Which Python statement is used 
to make decisions based on user input?""":
["A) for",
"B) if-elif-else",
"C) while",
"D) import"],
"4. What is the purpose of the display() function?":
["A) Add a task",
"B) Delete a task",
"C) Show all tasks and their current status",
"D) Exit the program"],
"""5. Which loop is used to keep the application
 running until the user chooses to exit?""":
["A) for loop",
"B) do-while loop",
"C) while loop",
"D) nested loop"]
}
answer=[3,3,2,3,3]
a=0
score=0
for i,j in question.items():
    print(i)
    for k in j:
        print(k)
    choice=int(input("enter choice :"))
    if choice==answer[a]:
        score+=1
        a+=1
print("correct answers :",score)    