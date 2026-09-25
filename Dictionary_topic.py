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

