#REQUIRED iNPUTS

name=input("enter your name:")
weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
age=int(input("enter your age:"))

print("Gender(M/F)")
gender=input("enter your gender:")
days=int(input("how many days did you exercised in last 30 days?:"))                                                                                   
duration=int(input("Average exercise duration per session (minutes):"))
push_ups=int(input("how many push ups in one set:"))
squats=int(input("how many squats in one set:"))
weight_loss=float(input("how many weight you loss:"))
muscle_gain=int(input("How much muscle you gain:"))
fitnes_goal = int(input( "Fitness Goal (1=Weight loss' 2=Muscle gain, 3=General fitness): "))
print("\n")

#CALCULATIONS

bmi=weight/height**2
is_male = gender.upper() == "M"
is_female = gender.upper() == "F"
bmr_male = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
bmr_female = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
bmr = (is_male * bmr_male) + (is_female * bmr_female)
secondary_tdee= bmr*1.2
Active_tdee= bmr*1.375
exercise_frequency= (days / 30*100)
total_exercise= days * duration
fitnes_score= (push_ups*2) + (squats*1.5)
weighth_loss_target= Active_tdee - 500
muscle_gain_target= Active_tdee + 300
maintenance_target = Active_tdee
# Select goal target using boolem arithmetic

calorie_target = (fitnes_goal==1) * weighth_loss_target + (fitnes_goal==2) * muscle_gain_target + (fitnes_goal==3)* maintenance_target


print("\n")

#BEGINNER PROCCESS INDICATORS (TRUE/FALSE)
bmi_ok = 18.5 <= bmi <30
exercise_good = exercise_frequency >=60
exercise_excellent= exercise_frequency >= 80
exercise_duration_ok = duration >= 30
push_up_ok = push_ups >=6
squat_ok = squats >= 10

# ------DISPLAY RESULTS------
print("\n=== FITNES BEGINNER PROGRESS SUMMARY ===")
print(f"Name: {name}")
print(f"bmi: {bmi:.2f}")
print(f"BMR: {bmr:.2F} kcal/day")
print(f"Secondary Tdee: {secondary_tdee:.2f}")
print(f" Active Tdee: {Active_tdee:.2f}")
print(f"Exercise Frequency: {exercise_frequency:.1f}%")
print(f" Total Monthly Exercise Minutes: {total_exercise:1f}")
print(f"Fitnes Score:{fitnes_score:.1f}")
print(f"Calorie Target (based on goal): {calorie_target:.1f} kcal/day" )

print(f"n\--- Beginner Progress Indicators---")
print(f"BMI Ok: {bmi_ok}")
print(f"Frequency: {exercise_good}")
print(f"Exercise excellent: {exercise_excellent}")
print(f"Exercise Duration: {exercise_duration_ok}")
print(f"Push up: {push_up_ok}")
print(f"Squat: {squat_ok}") 
