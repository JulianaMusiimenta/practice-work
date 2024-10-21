#question2(i)
Weight =int(input("Enter the weight of a persion in kilograms: "))
Height =int(input("Enter the height of a persion in meters: "))

BMI =Weight/Height

if BMI < 18.5:
    print("Under Weight")

elif 18.5<=BMI <=24.9:
    print("Normal Weight")

elif 25<= BMI<=29.9:
    print("Over Weight")

else:
    print("Obese")