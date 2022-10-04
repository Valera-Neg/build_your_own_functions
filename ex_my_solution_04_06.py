# Rewrite your pay computation with time-and-a-half for 
# ovetrime and create a function caled computepay 
# which takes two parameters (hours, and rate)
def computepay(hours, rate) :
    # hours = input("enter hours num: ")
    # rate = input("enter your rate: ")
    
    try:
      validNum = float(hours)
      validRate = float(rate)
    except:
      print("Error, please enter numeric input")
      quit()
    if validNum <= 40: 
      print("Regular")
      print ("Pay", validNum * validRate)
    else:  
      print("Overtime")
      print(((validNum - 40) * (validRate * 1.5)) + (40 * validRate))  
computepay(input("Enter Hours: "), input("Enter Rate: "))