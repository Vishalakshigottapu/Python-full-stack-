'''
students = ["Vishala", "Swpana", "Samitha", "Madhu"]

branches = ["Vizag", "Hyderabad", "Vijayawada"]

courses = ["DA", "PFS", "JFS", "Data Science"]
students.append("sai")
students.extend(["Ravi", "Sita"])
students.insert(1, "Priya")
print( students)
print( students[0])
print(students[-1])
print(students[:3])
print( students[::2])
print(students.index("Vishala"))
print( students.count("Vishala"))
print( len(students))
students.remove("Priya")
print(students)
removed = students.pop()
print( removed)
codegnan = {
    "Branches": branches,
    "Daily Exam": "7 PM to 11 PM",
    "Weekly Exam": "Tuesday",
    "Weekly Interview": "Sunday"
}

codegnan.update({
    "Courses": courses,
    "Monthly Event": "Hackathon",
    "Students": students
})

print("Codegnan:", codegnan)

events = {"Exam", "Interview"}
events.add("Hackathon")

print("Events:", events)

