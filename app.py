def calc_bmi():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    bmi = weight / (height**2)
    round_bmi = round(bmi, 2)

    if round_bmi > 0:
        if round_bmi <= 18.5:
            result = ("You're underweight")
        elif round_bmi > 18.5 and round_bmi <= 24.9:
            result = ("You're normal weight")
        elif round_bmi > 24.9 and round_bmi <= 29.9:
            result = ("You're overweight")
        elif round_bmi > 29.9 and round_bmi <= 34.9:
            result = ("You're obese")
        elif round_bmi > 34.9 and round_bmi <= 39.9:
            result = ("You're severely obese")
        elif round_bmi > 40:
            result = ("You're morbidly obese")
    else: print("Invalid inputs")
    
    
    print(f"Your BMI is {round_bmi}")
    print(result)

calc_bmi()
