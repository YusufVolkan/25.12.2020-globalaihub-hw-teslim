first_name = input("please enter your first name:")
last_name = input("please enter your last name:")
Age = int(input("Enter your age:"))
date_birthday = input("just year:")

information = [first_name, last_name, Age, date_birthday]
print(information)

for i in information:
    print(i)

if Age < 18:
    print("You cant go out because it's too dangerous")
else:
    print("You can go out to the street")