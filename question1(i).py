#question1(i)
def temperature_classifier():
    temperature =float(print("Enter the temperature value in c: "))
    if temperature < 0:
        print("freezing")

    elif 0<= temperature<= 10:
        print("cold")

    elif  11<=temperature<=20:
        print("moderate")

    elif 21<=temperature<=30:
       print("warm")

    else:
        print("hot")