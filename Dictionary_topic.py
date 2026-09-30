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
==>
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
==>
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
6. Sort Dictionary by Multiple Conditions
==>
employees = {
"Amit": {"salary": 70000, "age": 30},
"Rahul": {"salary": 85000, "age": 28},
"Priya": {"salary": 85000, "age": 32},
"Sneha": {"salary": 70000, "age": 25}
}

result=sorted(
    employees.items(),
    key=lambda item:(-item[1]["salary"],item[1]["age"])
)

for name,item in result :
    print(name,item)


 """ 
 Notes :
 
 1) employees.items() -->It actually convert the dictionary to tuple so that python can access the entire Amit": {"salary": 70000, "age": 30}
     
 2) This kind of hidden format is creating inside the logic for sorting 
            [
    ( (-85000, 28), ("Rahul", {"salary": 85000, "age": 28}) ),
    ( (-70000, 30), ("Amit", {"salary": 70000, "age": 30}) )
]
"""

===========================================================
7. Find Duplicate Values and Their Keys
==>
data = {
"a": 10,
"b": 20,
"c": 10,
"d": 30,
"e": 20,
"f": 40
}

group={}


for k,v in data.items():
    group.setdefault(v,[]).append(k)

result ={key:value
         for key,value in group.items()
         if len(value)>1
         }

print(result)

+++++++++++++++++++++++++++OR+++++++++++++++++++++++++++++++

The Interview Follow-Up: Fully Implemented
--------------------------------------------

In Python, dictionary keys must be immutable (hashable) types like strings, integers, or tuples. Lists are mutable, so attempting to use them as a key throws a TypeError: unhashable type: 'list'.
Here is the complete implementation of the tuple conversion workaround mentioned in your snippet:

data = {

    "a": [1, 2],

    "b": [3, 4],

    "c": [1, 2]

}

grouped = {}

for key, value in data.items():

    # Convert list to tuple to make it hashable
    hashable_value = tuple(value) 
    grouped.setdefault(hashable_value, []).append(key)

result = {

    val: keys
     for val, keys in grouped.items()
     if len(keys) > 1
}


print(result)

===========================================================
8.Find Differences Between Dictionaries
    
==>
    
old = {
    "name": "John",
    "age": 30,
    "city": "Kolkata",
    "salary": 70000
}

new = {
    "name": "John",
    "age": 31,
    "city": "Bangalore",
    "salary": 70000
}


all_keys =old.keys()|new.keys()

result ={}

for key in all_keys:
    old_val=old.get(key)
    new_val=new.get(key)
    
    if old_val!=new_val :
        result[key]={"old":old_val,
                       "new":new_val
                       }
print(result)


===========================================================
9. Aggregate Transaction Data
    
==>

transactions = [
    {"customer": "A", "amount": 100},
    {"customer": "B", "amount": 200},
    {"customer": "A", "amount": 300},
    {"customer": "C", "amount": 150},
    {"customer": "B", "amount": 100},
    {"customer": "A", "amount": 50}
]

result ={}

for transaction in transactions :
    customer=transaction["customer"]
    amount=transaction["amount"]

    if customer not in result :
        result[customer]={"total":0,"Count":0}

    result[customer]["total"]+=amount
    result[customer]["Count"]+=1

print(result)

for customer in result:
    total =result[customer]["total"]
    count=result[customer]["Count"]
    result[customer]["average"] =total/count
print(result)

===========================================================

