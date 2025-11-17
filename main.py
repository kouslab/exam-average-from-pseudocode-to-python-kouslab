"""
Kou Yang
IS-250-01
Pycharm and Github
Submission date: 11/16/2025
"""
"""
    Pseudocode: 
Ask user to enter first number as num1:
Ask user to enter second number as num2:
Ask user to enter third number as num3:

function average to calculate average of num1 and num2 and num3:
    Display first number:
    Display second number:
    Display third number:
    Calculate the sum of num1 and num2 and num3 and then divide by 3
    Display the result
    
Call the function average to display the result.

"""

#This program calculate the average of three exam scores

#Define the function to calculate the average of the three exam scores.
def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3)/3

#Define the main function
def main():
    #Ask the user to enter the first score
    num1 = int(input("Enter first score: "))

    #Ask the user to enter the second score
    num2 = int(input("Enter second score: "))

    #Ask the user to enter the third score
    num3 = int(input("Enter third score: "))

    #Call the calculate_average function and assign the result to a variable named "result"
    result = calculate_average(num1, num2, num3)

    #Display the first score that the user entered
    print(f"First score: {num1}")

    #Display the second score that the user entered
    print(f"Second score: {num2}")

    #Display the third score that the user entered
    print(f"Third score: {num3}")

    #Display the result for the average of the three exam score and round to 2 decimal places
    print(f"The average score is: {result:.2f}")

#Call the main function to execute the program
main()




  
