# Placement Readiness Tracker (Tasks 1, 2 & 3) - tracker.py

students = [
    {"name": "Aarav Sharma", "roll_no": "CSE001", "aptitude": 85.0, "verbal": 78.0, "coding": 92.0},
    {"name": "Diya Patel",   "roll_no": "CSE002", "aptitude": 45.0, "verbal": 55.0, "coding": 38.0},
    {"name": "Kabir Verma",  "roll_no": "CSE003", "aptitude": 72.0, "verbal": 65.0, "coding": 80.0},
    {"name": "Ananya Gupta", "roll_no": "CSE004", "aptitude": 30.0, "verbal": 40.0, "coding": 35.0},
    {"name": "Rohan Iyer",   "roll_no": "CSE005", "aptitude": 90.0, "verbal": 88.0, "coding": 95.0}
]

def get_valid_score(subject):
    while True:
        try:
            score = float(input(f"Enter {subject} score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100. Try again.")
        except ValueError:
            print("Please enter a valid number.")

print("=== Add New Student ===")
name = input("Enter student name: ").strip()
roll = input("Enter roll number: ").strip()
apt = get_valid_score("Aptitude")
verb = get_valid_score("Verbal")
code = get_valid_score("Coding")

students.append({
    "name": name,
    "roll_no": roll,
    "aptitude": apt,
    "verbal": verb,
    "coding": code
})

def average(student):
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3.0

def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"

def top_scorer(student_list):
    return max(student_list, key=average)

def needs_practice(student_list, limit=40):
    return [s for s in student_list if average(s) < limit]

print("\n" + "=" * 82)
print(f"{'Roll No':<10} | {'Name':<16} | {'Aptitude':<8} | {'Verbal':<8} | {'Coding':<8} | {'Average':<8} | {'Grade':<14}")
print("-" * 82)

for s in students:
    avg = average(s)
    print(f"{s['roll_no']:<10} | {s['name']:<16} | {s['aptitude']:<8.1f} | {s['verbal']:<8.1f} | {s['coding']:<8.1f} | {avg:<8.2f} | {grade(avg):<14}")

print("=" * 82)

best = top_scorer(students)
print(f"\nTop Scorer: {best['name']} ({best['roll_no']}) - Average: {average(best):.2f}")

low_scorers = needs_practice(students)
print("Students Needing Extra Practice (Average < 40):")
for s in low_scorers:
    print(f" - {s['name']} ({s['roll_no']}): Average = {average(s):.2f}")

def runner_up():
    print("\n=== Task 3: Runner-Up Score ===")
    n = int(input().strip())
    scores = list(map(int, input().strip().split()))
    unique_scores = sorted(set(scores), reverse=True)
    print(unique_scores[1])

if __name__ == "__main__":
    runner_up()
  "Add tracker.py implementation"
