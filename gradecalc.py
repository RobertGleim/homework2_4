def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def get_score(prompt):
    while True:
        try:
            entered_score = float(input(prompt))
            if 0 <= entered_score <= 100:
                return entered_score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric score.")


print("=== Grade Report ===")
num_scores = get_number("How many test scores would you like to enter? ")

scores = []
count = 0
while count < num_scores:
    score = get_score(f"Enter score #{count + 1}: ")
    scores.append(score)
    count += 1

average = calculate_average(scores)
letter_grade = get_letter_grade(average)

print("\n=== Your Grade based on test scores added2"
 ===")
print(f"Scores entered: {scores}")
print(f"Average score: {average:.2f}")
print(f"Letter grade: {letter_grade}")
