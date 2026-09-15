Question 1 : How to check whether the string is palindrome or not 

Answer:

s = "madam"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

""" Explain : 

 The Instructions: [start : stop : step]
Whenever you use the square brackets with colons [ : : ], Python looks for three instructions:

Start: Which address do I start at?

Stop: Which address do I stop at?

Step: Which direction do I walk, and how many houses do I jump?

Why [::-1] reverses the string
In the instruction [::-1], we left the start and stop completely blank.

start is blank.

stop is blank.

step is -1.

Because the step is -1 (a negative number), Python says: "Ah, we are walking backward. Since you didn't tell me where to start or stop, I will just start at the very last house, and walk backward all the way to the very first house."

So, Python looks at the backward addresses:

It starts at -1 (gets the letter n)

Takes a step backward to -2 (gets the letter o)

Takes a step backward to -3 (gets the letter h)

...and keeps going until it runs out of letters."""
