

class InterviewError (Exception):
    pass

class ApplicantAlreadyRegisteredError (InterviewError):
    def __init__ (self,name):
        self.name = name
        self.message = f"Applicant already registered: {name}"
        super().__init__(self.message)

class ApplicantNotRegisteredError(InterviewError):
    def __init__(self, name):
        self.name = name
        error_text = f"applicant not registered: {name}"
        super().__init__(error_text)
    

class InvalidCategoryError(InterviewError):
    def __init__(self,category,valid_categories):
        self.category = category
        self.valid_categories = valid_categories
        error_message = f"invalid category {category}. valid categories: {valid_categories}"
        super().__init__(error_message)


class InterviewScorer:
    def __init__(self, max_scores):
        self.max_scores = max_scores
        self.applicants = {}

    def register_applicant(self, name):
        if name in self.applicants:
            raise ApplicantAlreadyRegisteredError(name)
        self.applicants[name] = {}

    def record_score(self, name, category, score):
        try:
            applicant_scores = self.applicants[name]
        except KeyError:
            raise ApplicantNotRegisteredError(name) from None
        
        if category not in self.max_scores:
            raise InvalidCategoryError(category, list(self.max_scores.keys()))

        applicant_scores[category] = score
    
    def evaluate(self, name):
        try:
            scores = self.applicants[name]
        except KeyError:
            raise ApplicantNotRegisteredError(name) from None
        
        if not scores:
            return 0
        
        total_earned = sum(scores.values())
        total_possible = sum(self.max_scores.values())

        
        return (total_earned *100) // total_possible


categories = {"python": 20, "sql": 15, "communication": 10, "problem_solving": 25}
scorer = InterviewScorer(categories)

scorer.register_applicant("Nodira")
scorer.register_applicant("Rustam")

scorer.record_score("Nodira", "python", 18)
scorer.record_score("Nodira", "sql", 12)
scorer.record_score("Nodira", "communication", 9)
scorer.record_score("Nodira", "problem_solving", 20)

scorer.record_score("Rustam", "python", 10)
scorer.record_score("Rustam", "sql", 5)

print(f"Nodira: {scorer.evaluate('Nodira')}%")
print(f"Rustam: {scorer.evaluate('Rustam')}%")

tests = [
    lambda: scorer.register_applicant("Nodira"),
    lambda: scorer.record_score("Temur", "python", 15),
    lambda: scorer.record_score("Rustam", "java", 10),
]

for test in tests:
    try:
        test()
    except InterviewError as e:
        print(e)



