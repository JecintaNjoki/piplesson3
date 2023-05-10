# Write a Python program that takes a list of strings as input and outputs the number of times each string appears in the list, using a dictionary and conditional statements.

# Write a Python program that takes a list of numbers as input and outputs the median of the numbers 
def median_number(list):
    sortList=sorted(list)

    listLength=len(list)
    index =(listLength-1)//2

    if(listLength % 2):
        return sortList[index]
    else:
        return (sortList[index] + sortList[index+1])/2.0

median_number([14,20,55,23,43,87])

# Write a Python program that takes a list of numbers as input and outputs the second largest number in the list using conditional statements and a for loop.
def max_number(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    return max
print(max_number([26,36,46,56,66,76,89]))

# Write a Python program that takes a year as input and determines if it is a leap year.
def leap_year(year):
    year=2000
    if (year%400==0) and (year%100==00):
          print("is leap year")
    elif (year%4==0) and (year%100!=0):
        print("is leap year")
    else :
        print("is not a leap year")
        leap_year()



# Write a Python program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards), ignoring spaces and punctuation.
def  isPalindrome(word):
     return word == word[::-1]
  
word = "civic"
string = isPalindrome(word)
  
if string:
    print("is a palindrome")
else:
    print("is not a palindrome")