# Create a text file and write topics

topics = [
    "Python Basics",
    "Variables",
    "Data Types",
    "Operators",
    "Conditional Statements",
    "Loops",
    "Functions",
    "Lists",
    "Tuples",
    "Sets",
    "Dictionaries",
    "File Handling"
]

file = open("topics.txt", "w")

for topic in topics:
    file.write(topic + "\n")

file.close()

print("topics.txt file created successfully.")
