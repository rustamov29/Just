def calculate_study_points(subject_type, hours_studied, difficulty_level):
    subject_type=subject_type.lower ()
    difficulty_level=difficulty_level.lower ()

    if subject_type=="mathematics":
        if difficulty_level == "low":
            rate=12
        elif difficulty_level== "medium" :
            rate=18
        else :
            rate=25

    if subject_type== "scienes" :
        if difficulty_level == "low":
            rate= 10
        elif difficulty_level== "medium" :
            rate= 15
        else:     
            rate=20

    if subject_type == "languages" :  
        if difficulty_level== "low":
            rate= 8
        elif difficulty_level== "medium":
            rate=12
        else:
            rate=16

def calculate_mastery_index(semester_count, baseline_score, current_score) :
    expected_score=1000 + (semester_count * 100)           
    score_range= expected_score - baseline_score
    mastery_pecantage = (current_score - baseline_score) / score_range * 100
    return mastery_pecantage

def determine_progress_tier(mastery_percent):
    if mastery_percent > 50:
        return "Foundation Tier"
    elif 50<= mastery_percent <60:
        return "Development Tier"
    elif 60<= mastery_percent <70:
        return "Proficiency Tier"
    elif 70<= mastery_percent < 85:
        return "Excellence Tier"
    else :
        return "Mastery Tier"
    
def calculate_achievement_score(points, hours, tier_modifier):
    Base_score = points * 0.05 + hours * 2
    if tier_modifier == "Foundation Tier":
       tier_multiplier = 0.5
    elif tier_modifier == "Development Tier":
       tier_multiplier = 1.0
    elif tier_modifier == "Proficiency Tier":
       tier_multiplier = 1.2
    elif tier_modifier == "Excellence Tier":
        tier_multiplier = 1.5
    elif tier_modifier == "Mastery Tier":
        tier_multiplier = 1.8
    Base_score * tier_multiplier     
    return  round((Base_score * tier_multiplier), 1) 

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