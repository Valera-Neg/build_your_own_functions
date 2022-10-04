def computpay(hours, rate) :
    print("In computpay")
    if hours > 40 :
        reg = floatRate * floatHour
        over = (floatHour - 40) * (floatRate * 0.5)
        overtime = floatHour - 40
        pay = reg + over
        print("Overtime", overtime)
    else:
      pay = hours * rate
      print("Regular", pay)
    return pay  
    
strHours = input("Enter Hours: ")
strRate = input("Enter Rate: ")
try:
  floatHour = float(strHours)
  floatRate = float(strRate)
  xPay = computpay(floatHour, floatRate)
except:
  print("Error, please enter numeric input")
  quit()
  # xPay = computpay(floatHour, floatRate)
print ("Pay:", xPay) 