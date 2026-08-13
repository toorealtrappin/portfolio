# =====================================================================
# LESSON 4: FUNCTIONS (`def`)
# =====================================================================

# 1. Defining a basic function
def greet_student(name):
    """Prints a customized welcome messeage."""
    print(f"Welcome back, {name}!")


# 2. Function with parameters and a return value
def calculate_total_credits(course_count, credit_per_course=3):
    """Calculates total academic credits."""
    total = course_count * credit_per_course
    return total

# 3. Function combining lists and logic
def display_course_summary(student_name, course_list):
    print(f"\n--- Academic Summary for {student_name} ---")
    print(f"Total Courses: {len(course_list)}")
    for i, course in enumerate(course_list, start=1):
        print(f" {i}: {course}")

    total_credits = calculate_total_credits(len(course_list))
    print(f"Total Estimated Credits: {total_credits}")


# --- CALLING THE FUNCTIONS ---
greet_student("Caleb Obeng")

my_courses = ["Business Math", "Macroeconomics", "Financial Accounting", "African Studies"]
display_course_summary("Caleb Obeng", my_courses)