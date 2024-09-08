# While Loop in python

count = 0
while (count<=5):
    print(count)
    count=count+1

# example
num = 5
while (num>=0):
    print(num)
    num= num-1
print("Done with the loop")



#while loop using user input
i= int(input("Enter any number between 1-10: "))
while(i<=10):
    # if we do not ask for user input inside the loop it goes into infinite loop
    i= int(input("Enter any number between 1-10: "))
    print(i)
print("program is over")



# printing from 100 to 98 using while loop using decrement

number=100
while (number>=90):
    print(number)
    number=number-1
# it goes to else step after getting false result in while loop    
else:
    print("Hello, how are you?")