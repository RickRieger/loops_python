import getpass
# Python Loops Worksheet
# In Python, loops are an important tool that allow developers to execute a block of code over and over as long as a condition holds true. This worksheet will allow you to practice a for loop and while loop.
# For Loop
# A for loop is ideal in a situation where you know exactly how many times you want the loop to run or you want to iterate over a collection. 
# To iterate for a specified number of times, use the built-in Python range() function.
 
# For Loop Tasks
# 1.	Write a for loop that will run five times and print “hello!” to the console five times
for num in range(5):
  print('hello!')
# a.	Expected Output
 
# 2.	Write a for loop that counts from 0 to 10, with each number being print to the console one at a time
for num in range(11):
  print(num)
# a.	Expected Output
 
# 3.	Write a for loop that counts from 10 to 0, with each number being print to the console one at a time. HINT: When calling the range function provide three arguments 
# “range(start number, stop number, step number)”
for num in range(10,-1,-1):
  print(num)
# a.	Expected Output
 
# 4.	Write a for loop that will run as many times as a user wants, with each iteration printing “devCodeCamp” to the console. HINT: you will need to use the Python input() function to gather user input
num_of_loops = input('How many times do wou want to see "devCodeCamp" printed to the console?', )

try:
  num_of_loops = int(num_of_loops)
except:
  print('Provide only a whole number please.')
# a.	Expected Output if user chooses 4
if(num_of_loops):
  for i in range(num_of_loops):
    print('devCodeCamp')
 
# 5.	Write a for loop that will print each character of the string “Packers” to the console. 
for char in "Packers":
  print(char)
# a.	Expected Output
 
# 6.	CHALLENGE: Fizz Buzz
# a.	Write a program that prints every number from 0 to 100 to the console
for num in range(101):
  if(num % 3 == 0 & num % 5 == 0):
    print('fizzbuzz')
  elif(num % 3 == 0):
    print('fizz')
  elif(num % 5):
    print('buzz')
  
# b.	If a number is divisible by 3, print ‘fizz’ instead of the number
# c.	If a number is divisible by 5, print ‘buzz’ instead of the number
# d.	If a number is divisible by 3 and 5, print ‘fizzbuzz’ instead of the number
# While Loop
# A while loop is ideal in a situation where do you not know how many times you want the loop to run. Instead, the loop will continue to iterate as long as the condition remains to be true. Once the condition becomes false then the loop completes.
 
# HINT: if isInstructorAwesome is set equal to true, make sure to have a way to set isInstructorAwesome equal to false somewhere inside the while loop to prevent an infinite loop from occurring
# While Loop Tasks
# 1.	Write a while loop that will run five times and print “hello!” to the console five times
num = 0

while num < 5:
  print('hello!')
  num += 1
# a.	Expected Output



# 2.	Write a while loop that will prompt a user for their password and will continue to prompt the user until the typed in password is correct. If correct, print to the console “User Validated”

# a.	Expected Output

# ask user for name and password

password = input('Please provide a password: ', )

password_verify = ''

while password != password_verify:
  password_verify = input('Please verify the password entered: ')

print('User is validated!')



# # 2.	Write a while loop that will prompt a user for their password and will continue to prompt the user until the typed in password is correct. If correct, print to the console “User Validated”

# a.	Expected Output

# ask user for name and password
username = input('Please provide a username: ', )
password = input('Please provide a password: ', )

# setting database variable to object containing username and password (key value store)
database = {username: password}

# ask user for username again
username = input("Enter Your Username : ")
# ask user for password again (but it's hidden)
password = getpass.getpass("Enter Your Password : ")
# iterate through the database object keys even though there's only one/
for i in database.keys():

    # checking to see if username matches the key

    if username == i:

        # Checking to see if password matches the valuestore and will continue to ask for password if it's not correct.
        # Nesting loops is never ideal and should be avoided O(n^2)

        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break

print("User Validated")
