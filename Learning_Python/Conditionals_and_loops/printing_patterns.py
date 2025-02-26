#Here is a simple pattern printing program

print ("# # # #")
print ("# # # #")
print ("# # # #")
print ("# # # #")


#Here is a simple pattern printing program using loops
for i in range(4):
    for j in range(4):
        print("#", end=" ")
    print()


#Here is another simple pattern printing program using loops
for i in range(0, 4):
    for j in range(i+1):
        print("#", end=" ")
    print()



#Here is another simple pattern printing program using loops
for i in range(5):                                 #number of rows
    for j in range(i-1):                           #number of columns
        print("#", end=" ")
    print()




for i in range(4):
    for j in range(4-i):
        print("#", end=" ")
    print()


#test programs

for i in range(5 , 0, -1):
    for j in range(i-1):
        print("1", end="")
    print()



for i in range(4):
    for j in range(i, 4):
        print(j + 1, end="")
    print()


# Print APQR, ABQR, ABCR, ABCD
for i in range(4):
    for j in range(4):
        if j <= i:
            print(chr(65 + j), end="")
        else:
            print(chr(79 + j - i), end="")
    print()



