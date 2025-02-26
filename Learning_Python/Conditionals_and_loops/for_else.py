#example 1 using for else loop

nums = [10, 15, 16, 18, 20]

for num in nums:
    if num%5 ==0:
        print(f"{num} is divisible by 5")
        break
else:
    print("No number is divisible by 5")

#example 2

list = [1, 2, 3, 4,]

for i in list:
    if i%5 == 0:
        print(f"{i} is divisible by 5")
        break
else:
    print("No number is divisible by 5")


#Here break statement is used to break the loop when the condition is met and is compulsory to use in for else loop