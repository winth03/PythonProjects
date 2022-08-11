w = int(input("Input weigth(kg): "))
h = int(input("Input height(cm): "))

print("Your BMI is " + str(w / (h / 100) ** 2))
