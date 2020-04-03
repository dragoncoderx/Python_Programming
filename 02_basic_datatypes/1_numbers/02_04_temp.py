'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"

'''

F = int(input("Enter a temperature in Farenheit: "))
C = (F - 32) * (5/9)
print(str(F) + "degrees in fahrenheit = " + str(C) + " degrees celsius") #BOOM

#print str() + string + str() + string etc.
#done

