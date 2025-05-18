import time
import webbrowser
print("Welcome to BMI calculator.....")
time.sleep(0.5)
print("in this app, we calculator your Body Mass Index")
time.sleep(0.5)
print("So.. Lets get started")
response = input('Press "P for Pound/Foot" Or "Press K for Kilogram/meters" Or "Press A for KiloGram/Foot" Or "Press B for Pound/Meters":  ')

if response == 'p':
    Height_feet = float(input("Enter your height in foot(feet): "))
    Height_inches = float(input("Enter remaining inches: "))
    Height = Height_feet * 12 + Height_inches
    Weight_Pound = float(input("Enter your Weight in pound: "))
    if Weight_Pound == Weight_Pound and Height == Height:
        Weight_Kilo = Weight_Pound * 0.453592
        print("your weight in KiloGrams is:", Weight_Kilo)
        time.sleep(0.5)
        Height_meters = Height * 0.0254
        print("your height in Meters is:", Height_meters)

elif response == 'k':
    Height_meters = float(input("Enter your height in meters: "))
    Weight_Kilo = float(input("Enter your weight in Kilogram: "))

elif response == 'a':
    Height_feet = float(input("Enter your height in foot(feet): "))
    Height_inches = float(input("Enter remaining inches: "))
    Height = Height_feet * 12 + Height_inches
    Weight_Kilo = float(input("Enter your Weight in KiloGrams: "))
    if Weight_Kilo == Weight_Kilo and Height == Height:
        print("your weight in KiloGrams is:", Weight_Kilo)
        time.sleep(0.5)
        Height_meters = Height * 0.0254
        print("your height in Meters is:", Height_meters)

elif response == 'b':
    Weight_Pound = float(input("Enter your weight in Pounds: "))
    Height_meters = float(input("Enter your height in meters: "))
    if Weight_Pound == Weight_Pound and Height_meters == Height_meters:
        Weight_Pound = Weight_Pound * 0.453592
        print("your weight in KiloGrams is:", Weight_Pound)
        time.sleep(0.5)
        print("your height in Meters is:", Height_meters)

BMI = Weight_Kilo / (Height_meters ** 2)
print("your BMI score is:", BMI)

if BMI < 16:
    category = "Severely Underweight"
    print("redirecting you to the required website for weight gain:   .....")
    webbrowser.open("https://www.betterhealth.vic.gov.au/health/healthyliving/weight-and-muscle-gain")
elif 16 <= BMI < 17:
    category = "Very Underweight"
    print("redirecting you to the required website for weight gain:   .....")
    webbrowser.open("https://www.betterhealth.vic.gov.au/health/healthyliving/weight-and-muscle-gain")
elif 17 <= BMI < 18.5:
    category = "Underweight"
    print("redirecting you to the required website for weight gain:   .....")
    webbrowser.open("https://www.betterhealth.vic.gov.au/health/healthyliving/weight-and-muscle-gain")
elif 18.5 <= BMI < 25:
    category = "Normal (Healthy)"
    print("you are good to go... ")
elif 25 <= BMI < 30:
    category = "Overweight"
    print("redirecting you to the required weight loss link")
    webbrowser.open("https://www.medparkhospital.com/en-US/lifestyles/7-best-weight-loss-exercises")
elif 30 <= BMI < 35:
    category = "Obese Class I (Moderate)"
    print("redirecting you to the required weight loss link")
    webbrowser.open("https://www.medparkhospital.com/en-US/lifestyles/7-best-weight-loss-exercises")
elif 35 <= BMI < 40:
    category = "Obese Class II (Severe)"
    print("redirecting you to the required link")
    webbrowser("https://www.medparkhospital.com/en-US/lifestyles/7-best-weight-loss-exercises")
else:
    category = "Obese Class III (Very Severe)"
    print("you are very much obese... kindly consult doctor...")
    time.sleep(1)
    print("OR............")
    print("Redirecting you to required link")
    webbrowser.open("https://www.medparkhospital.com/en-US/lifestyles/7-best-weight-loss-exercises")

print("According to your BMI, you are:", category)
print("Take Care......")
