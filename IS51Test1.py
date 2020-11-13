
"""
Create a program that will determine which option results in more money.
Option one is $100 a for ten days. Option 2 starts at $1 day but doubles
each day for ten days. One function will determine the amount of pay for
Option 1. The second function will determine the amount of pay for Option 2. 

Function 1 will return 100 * 10 days
Function 2 will return a loop consisting of 10 times and each time it will double

It will then evaluate the results of Option 1 and Option 2. If they are equal 
it will tell the user "Option 1 and Option 2 pay the same"
if Option 1 is more it will say "Option 1 is better"
if Option 2 is more it will say "Option 2 is better"
"""

"""
# option 1
return 100 * 10

# option 2
amount = 1
list1 = []
loop 10 times
    add looped amount to list
    amount *= 2
return amount

#main
answer = ""
var1 = option1() #1000
var2 = option2() #1023
if var1 == var2
    "Option 1 and Option 2 pay the same"
if var1 < var2  
    "Option 2 is better"
else 
    "Option 1 is better"

Main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *= 2
    total = sum(list1)
    return total

def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer = "Option 1 and Option 2 pays the same"
    if var1 < var2:
        answer = "Option 2 is better"
    else:
        answer = "Option 1 is better"
    print(answer)

main()