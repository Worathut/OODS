def BMI(h,w):
    return w/(h**2)

h, w = [float(x) for x in input("Enter your High and Weight : ").split()]
bmi = BMI(h,w)

if bmi < 18.5:
    print("Less Weight")
elif 18.5 <= bmi < 23:
    print("Normal Weight")
elif 23 <= bmi < 25:
    print("More than Normal Weight")
elif 25 <= bmi < 30:
    print("Getting Fat")
elif bmi >= 30:
    print("Fat")