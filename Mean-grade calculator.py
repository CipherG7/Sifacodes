def input_subjects_scores():
    subjects = {}
    num_subjects = int(input("Enter the number of subjects: "))
    for _ in range(num_subjects):
        subject = input("Enter the subject name: ")
        score = float(input(f"Enter the score for {subject}: "))
        subjects[subject] = score
    
    print("Subjects and scores:")
    for subject, score in subjects.items():
        print(f"{subject}: {score}")
    
    return subjects

def compute_mean_grade(subjects):
    total_score = sum(subjects.values())
    mean_grade = total_score / len(subjects)
    return mean_grade

def main():
    yearly_grades = []
    for year in range(1, 5):
        print(f"***********Year {year}***********")
        subjects_scores = input_subjects_scores()
        mean_grade = compute_mean_grade(subjects_scores)
        yearly_grades.append(mean_grade)
        print(f"Mean grade for Year {year}: {mean_grade:.2f}\n")

    overall_mean_grade = sum(yearly_grades) / len(yearly_grades)
    print(f"Overall mean grade for the 4 years: {overall_mean_grade:.2f}\n")

if __name__ == "__main__":
    main()
