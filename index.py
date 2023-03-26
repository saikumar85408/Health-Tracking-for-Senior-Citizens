import datetime

def calculate_bmi(weight, height):
    # Get BMI
    return weight / (height ** 2)

def check_bmi(bmi):
   # Checks BMI(Body mass index)
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "healthy"
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def check_vital_signs(blood_pressure, pulse):
   # It checks the blood_pressure,pulse
    
    if blood_pressure[0] >= 140 or blood_pressure[1] >= 90:
        return "High blood pressure"
    elif pulse < 60 or pulse > 100:
        return "Irregular pulse"
    else:
        return "Normal"

def calculate_age(birthdate):
    # Calculte the age of the preson 
    
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)) # Get the age by comparing with today date
    return age

def main():
    # user needs to enter name,birthdate, weigth,height,blood_pressure,pulse
    
    print("Welcome to the Health Tracker!")
    name = input()
    birthdate = input()
    weight = float(input())
    height = float(input())
    blood_pressure = input().split("/")
    pulse = int(input())

    age = calculate_age(datetime.datetime.strptime(birthdate, "%Y-%m-%d").date())
    bmi = calculate_bmi(weight, height)
    bmi_status = check_bmi(bmi)
    vital_signs_status = check_vital_signs(blood_pressure, pulse)

    print(f"Hello {name}! You are {age} years old.")
    print(f"Your BMI is {bmi:.2f}, which is {bmi_status}.")
    print(f"Your blood pressure and pulse rate are {blood_pressure[0]}/{blood_pressure[1]} mmHg and {pulse} bpm, respectively.")
    print(f"Your vital signs are {vital_signs_status}.")

if __name__ == "__main__":
    main()
