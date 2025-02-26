#Here we are going to see the difference between break, continue and pass statements in python

#break statement

print("Using break to stop the loop:")
for i in range(10):
    if i == 5:                                     #Here we are breaking the loop when i is 5
        break
    print(i)
print("\n")


#continue statement

print("Using continue to skip even numbers:")
for i in range(10):
    if i % 2 == 0:                                #Here we are skipping even numbers and printing odd numbers only.
        continue
    print(i)
print("\n")



#pass statement
#ww nornally use pass when we have a condition that we want to do nothing or if we want to skip the block.
print("Using pass as a placeholder:")
for i in range(10):
    if i % 2 == 0:                              #Here we are using pass to do nothing for even numbers and print odd numbers only.
        pass
    else:
        print(i)
print("\n")


#another example of pass statement
print("Using pass:")
for i in range(10):
    if i == 5:                                  #Here we are using pass to do nothing when i is 5 and print all other numbers.
        pass
    else:
        print(i)


#In summary:
#break: Exits the loop entirely.
#continue: Skips the current iteration and continues with the next.
#pass: Does nothing and is used as a placeholder.
#These statements help control the flow of loops in Python.