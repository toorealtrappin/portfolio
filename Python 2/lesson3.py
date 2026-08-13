# =====================================================================
# LESSON 3: Automating Repetition with Loops (Loops)
# =====================================================================

courses = ["Business Math", "Macroeconomics", "Commercial Law", "Financial Accounting", "African Studies"]

# 1. FOR LOOP: Print each item in a list individually
print("=== My Enrolled Courses ===")
for course in courses:
    print(f". {course}")


# 2. FOR LOOP WITH ENUMERATE: Get index numbers automatically
print("\n=== Courses Schedule ===")
for index, course in enumerate(courses, start=1):
    print(f"Course {index}: {course}")


# 3. WHILE LOOP: Run on code until user decides to exit
print("\n=== Simple Counter Demo ===")
count = 1
while count <= 3:
    print(f"Counting: {count}")
    count += 1 # Adds 1 to the count in each iteration