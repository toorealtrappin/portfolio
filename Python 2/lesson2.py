# =====================================================================
# LESSION 2: DATA STRUCTURES
# =====================================================================
# 1. LIST (Ordered collections of items)
courses = ["Business Math", "Macroeconomics", "Commercial Law", "Financial Accounting"]

print("=== Working with Lists ===")
#Python starts counting items at index 0.
print(f"First course: {courses[0]}")
print(f"Total courses: {len(courses)}")

# Adding a new course using .append()
courses.append("African Studies")
print(f"Updated course list: {courses}\n")


# 2. DICTIONARIES (Key-value paris for structureed data)
student = {
    "name": "Caleb Obeng",
    "level": 200,
    "program": "Business Administration",
    "skills": ["Python", "Problem Solving"]
}

print("=== Working with Dictionaries ===")
# Accessing data using keys instead of index numbers 
print (f"Student Name: {student['name']}")
print (f"Current Level: {student['level']}")
print (f"First Skill: {student['skills'][0]}")

# Adding a new key-value pair
student["status"] = "Active"
print(f"Updated Student Profile: {student}") 