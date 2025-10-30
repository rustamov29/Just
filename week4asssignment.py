def calculate_study_points(subject_type, hours_studied, difficulty_level):
    subject_type=subject_type.lower ()
    difficulty_level=difficulty_level.lower ()
    rate = 0

    if subject_type=="mathematics":
        if difficulty_level == "high":
            rate=25
        elif difficulty_level== "medium" :
            rate=14
        elif difficulty_level== "low" :
            rate=12
        else:
            rate=0

    elif subject_type== "scienes" :
        if difficulty_level == "high":
            rate= 20
        elif difficulty_level== "medium" :
            rate= 15
        elif difficulty_level== "low" :
            rate= 10
        else:     
            rate=0

    elif subject_type == "languages" :  
        if difficulty_level== "high":
            rate= 16
        elif difficulty_level== "medium":
            rate=12
        elif difficulty_level== "low":
            rate=8
        else:
            rate=0
    else:
        return 0
    return rate * hours_studied

def calculate_mastery_index(semester_count, baseline_score, current_score) :
    expected_score=1000 + (semester_count * 100)           
    score_range= expected_score - baseline_score
    if score_range <= 0:
        return 0
    mastery_pecantage = (current_score - baseline_score) / score_range * 100
    return mastery_pecantage

def determine_progress_tier(mastery_percent):
    if 0 <= mastery_percent < 50:
        return "Foundation Tier"
    elif 50<= mastery_percent <60:
        return "Development Tier"
    elif 60<= mastery_percent <70:
        return "Proficiency Tier"
    elif 70<= mastery_percent < 85:
        return "Excellence Tier"
    elif mastery_percent < 100:
        return "Mastery Tier"
    else :
        return "Error"
    
def calculate_achievement_score(points, hours, tier_modifier):
    Base_score = points * 0.05 + hours * 2
    # if tier_modifier == "Foundation Tier":
    #    tier_multiplier = 0.5
    # elif tier_modifier == "Development Tier":
    #    tier_multiplier = 1.0
    # elif tier_modifier == "Proficiency Tier":
    #    tier_multiplier = 1.2
    # elif tier_modifier == "Excellence Tier":
    #     tier_multiplier = 1.5
    # elif tier_modifier == "Mastery Tier":
    #     tier_multiplier = 1.8
    # Base_score * tier_multiplier     
    return  round((Base_score * tier_modifier), 1) 

def needs_tutoring(study_weeks, total_hours, avg_mastery):
    if study_weeks >= 6 and avg_mastery < 50:
        return True
    elif  total_hours < 100 and avg_mastery < 60:
        return True
    elif study_weeks >= 4 and avg_mastery < 40:
        return True
    else:
        return False

def generate_progress_report(student, subject_type, hours, difficulty_level, semester_count, baseline_score, current_score, study_weeks):
    mastery_percentage = calculate_mastery_index(semester_count, baseline_score, current_score)
    tier = determine_progress_tier(mastery_percentage)
    points = calculate_study_points(subject_type, hours, difficulty_level)
    if tier == "Foundation Tier":
        tier_modifier = 0.5
    elif tier == "Development Tier":
        tier_modifier = 1.0
    elif tier == "Proficiency Tier":
        tier_modifier = 1.2
    elif tier == "Excellence Tier":
        tier_modifier = 1.5
    elif tier == "Mastery Tier":
        tier_modifier = 1.8
    else:
        return "Error"
    achievement_score = calculate_achievement_score(points, hours, tier_modifier)
    tutoring = needs_tutoring(study_weeks, hours, mastery_percentage)
    print("=" * 40 )
    print(f"Progress Report for: {student}")
    print("-" * 40)
    print(f"Subject Type: {subject_type}")
    print(f"Hours Studied: {hours}")
    print(f"Difficulty Level: {difficulty_level}")
    print(f"Study Points: {points}")
    print("Mastery Analysis:")
    print(f"  Semesters: {semester_count}, Baseline: {baseline_score}, Current Score: {current_score}")
    print(f"  Mastery: {mastery_percentage:.1f}%")
    print(f"  Progress Tier: {tier}")
    print(f"Achievement Score: {achievement_score}")
    print(f"Study Weeks: {study_weeks}")
    print(f"Tutoring Needed: {tutoring}\n")

generate_progress_report("Parker", "mathematics",45, "high", 3 , 800, 1150, 3)
generate_progress_report("Riley", "science",60, "medium", 5 , 900 , 1300, 5)
generate_progress_report("Cameron", "languages",30, "low", 8 , 850, 950 , 7)