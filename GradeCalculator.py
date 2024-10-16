math = float(input("Enter the score for Math: "))
science = float(input("Enter the score for Science: "))
english = float(input("Enter the score for English: "))
history = float(input("Enter the score for History: "))
art = float(input("Enter the score for Art: "))

# Calculate the average score
total_score = math + science + english + history + art
average_score = total_score / 5

# Assign a grade based on the average score
if  average_score >= 80  and average_score <= 100:
    grade = 'A'
    feedback = "Excellent work!"
elif (average_score  >= 70  and  average_score < 80):
    grade = 'B'
    feedback = "Good job! Keep it up."
elif (average_score  >= 60  and  average_score < 70):
    grade = 'C'
    feedback = "Fair performance, but there's room for improvement."
elif (average_score  >= 50  and  average_score < 60):
    grade = 'D'
    feedback = "You need to work harder."
else:
    grade = 'F'
    feedback = "Failing grade. It's important to study more."

# Display the average score, grade, and feedback
print(f"\nAverage Score: {average_score:.2f}")
print(f"Grade: {grade}")
print(f"Feedback: {feedback}")