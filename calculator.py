#making a calculator out of python
#print intro for computer
print("Hello I am a calculator ")
#make two variables and store input

num1=float(input("Enter your first number here : "))

num2=float(input("Enter your second number here : "))

#make a next variable to store user command

user_command=input('''Enter the operation you want the computer to do
                            We have +,-,/ and *  : ''')
if user_command=="+":
    print(num1+num2)

elif user_command=="-":
    print(num1-num2)

elif user_command=="/":
    print(num1/num2)

elif user_command=="*":
    print(num1*num2)

else:
    print("invalid syntax")
