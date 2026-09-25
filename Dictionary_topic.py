1. Merge Dictionaries and Sum Common Keys

==>
dict_list = [
    {"A": 10, "B": 20},
    {"A": 30, "C": 40},
    {"B": 10, "C": 20}
]
result = {}
for d in dict_list:
    for key, value in d.items():
        result[key] = result.get(key, 0) + value
print(result)


===========================================================

2. Find the Second Highest Distinct Value
==>
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}
unique_scores = sorted(set(scores.values()), reverse=True)
if len(unique_scores) < 2:
    result = []
else:
    second_highest = unique_scores[1]
    result = [
        name
        for name, score in scores.items()
        if score == second_highest
    ]
print(result)


===========================================================
3. Character Frequency Without Counter
==>
text = "programming"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)


===========================================================
4. Group Employees by Department

employees = [
    {"name": "Amit", "dept": "IT"},
    {"name": "Rahul", "dept": "HR"},
    {"name": "Priya", "dept": "IT"},
    {"name": "Sneha", "dept": "Finance"},
    {"name": "Arjun", "dept": "HR"}
]

result = {}
for employee in employees:
    dept = employee["dept"]
    name = employee["name"]
    result.setdefault(dept, []).append(name)
print(result)


===========================================================

5. Filter a Nested Dictionary
employees = {
    101: {"name": "Amit", "salary": 70000, "dept": "IT"},
    102: {"name": "Rahul", "salary": 50000, "dept": "HR"},
    103: {"name": "Priya", "salary": 85000, "dept": "IT"},
    104: {"name": "Sneha", "salary": 65000, "dept": "Finance"},
    105: {"name": "Arjun", "salary": 90000, "dept": "IT"}
}

result = {
    emp_id: details
    for emp_id, details in employees.items()
    if details["dept"] == "IT"
    and details["salary"] > 75000
}
print(result)

===========================================================
