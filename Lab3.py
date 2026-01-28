# Student database
students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}


alice_ai_grade = students["S001"]["courses"]["AI301"]["grade"]
print("Alice AI301 grade:", alice_ai_grade)


bob_courses = students["S002"]["courses"]

total_points = 0
total_credits = 0

for course in bob_courses.values():
    total_points += course["grade"] * course["credits"]
    total_credits += course["credits"]

bob_gpa = total_points / total_credits
print("Bob GPA:", bob_gpa)


cs101_students = []

for student in students.values():
    if "CS101" in student["courses"]:
        cs101_students.append(student["name"])

print("Students in CS101:", cs101_students)


total_grades = 0
course_count = 0

for student in students.values():
    for course in student["courses"].values():
        total_grades += course["grade"]
        course_count += 1

average_grade = total_grades / course_count
print("Average grade across all courses:", average_grade)


highest_gpa = 0
top_student = ""

for student in students.values():
    total_points = 0
    total_credits = 0

    for course in student["courses"].values():
        total_points += course["grade"] * course["credits"]
        total_credits += course["credits"]

    gpa = total_points / total_credits

    if gpa > highest_gpa:
        highest_gpa = gpa
        top_student = student["name"]

print("Top student:", top_student)
print("Highest GPA:", highest_gpa)
