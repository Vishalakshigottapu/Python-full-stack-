print("------> BMI CALCULATOR <------")
name = input("Enter your name: ")
weight = float(input("Enter your weight in kgs: "))
print("\nChoose height unit:")
print("1. Centimeters")
print("2. Feet")
print("3. Meters")
choice = int(input("Enter your choice (1/2/3): "))
if choice == 1:
    height_cm = float(input("Enter your height in centimeters: "))
    if height_cm > 0 and height_cm < 200:
        height = height_cm / 100
    else:
        height = 0
elif choice == 2:
    feet = float(input("Enter your height in feet: "))
    if feet > 0:
        height = feet * 12 * 2.54 / 100  # 1 foot = 12 inches
                                        # 1 inch = 2.54 cm
    else:
        height = 0
elif choice == 3:
    height = float(input("Enter your height in meters: "))
else:
    height = 0
    print("Invalid choice!")
if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    print(f"\nName: {name}")
    print(f"Weight: {weight} kgs")
    print(f"Height: {height:.2f} meters")
    print(f"BMI: {bmi:.2f}")
    if bmi < 18.5:
        print("Category: Underweight -> Eat well")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("Category: Healthy -> Keep consistent")
    elif bmi >= 25 and bmi <= 29.9:
        print("Category: Overweight -> Start exercising")
    else:
        print("Category: Obesity")
else:
    print("Please enter only positive values greater than 0")


