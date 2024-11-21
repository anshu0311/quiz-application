file_name = "users.txt"
def load_users():
    try:
        with open(file_name, "r") as file:
            return dict(line.strip().split(":") for line in file)
    except FileNotFoundError:
        return {}

# Save new user to the file
def save_user(username, password):
    with open(file_name, "a") as file:
        file.write(f"{username}:{password}\n")

# Initialize users from file
users = load_users()

# Sign Up
print("***** Sign Up Page *****")
username = input("Please enter a username: ")
password = input("Please enter a password: ")

if username in users:
    print("Username already exists. Please use a different username.")
else:
    users[username] = password
    save_user(username, password)
    print("Registration successful!")

# Login
print("***** Login Page *****")
while True:
    login_username = input("Enter your registered username: ")
    login_password = input("Enter your password: ")
    
    if login_username in users and users[login_username] == login_password:
        print("Login Successful!")
        break
    else:
        print("Incorrect username or password. Please try again.")

# Quiz Section
print("Welcome to the Quiz!")
print("")
print("Data Structures and Algorithms (DSA) Quiz")

score = 0

dsa_questions = {
    1: ["Which data structure follows the LIFO (Last In, First Out) principle?", 
        "A. Queue", "B. Stack", "C. Array", "D. Linked List", "B"],
    
    2: ["Which algorithm is known for having the worst-case time complexity of O(n^2)?", 
        "A. Merge Sort", "B. Bubble Sort", "C. Quick Sort", "D. Heap Sort", "B"],
    
    3: ["What is the space complexity of the Quick Sort algorithm in its best case?", 
        "A. O(n)", "B. O(log n)", "C. O(1)", "D. O(n log n)", "B"],
    
    4: ["What is the time complexity for inserting an element into a linked list?", 
        "A. O(1)", "B. O(n)", "C. O(log n)", "D. O(n^2)", "A"],
    
    5: ["Which of the following is a balanced binary search tree?", 
        "A. AVL Tree", "B. Binary Heap", "C. B-tree", "D. Trie", "A"]
}

for q_num in range(1, 6):
    print(dsa_questions[q_num][0])
    for option_num in range(1, 5):
        print(dsa_questions[q_num][option_num])

    answer = input("Please select your answer (A, B, C, or D): ").upper()
    if dsa_questions[q_num][5] == answer:
        score += 1

print("Database Management Systems (DBMS) Quiz")

dbms_questions = {
    1: ["What does DBMS stand for?", 
        "A. DataBase Management System", "B. DataBase Multiple Systems", "C. Digital Backup Management System", "D. Dynamic Base Management System", "A"],
    
    2: ["Which SQL command is used to add data to a table?", 
        "A. UPDATE", "B. INSERT", "C. SELECT", "D. DELETE", "B"],
    
    3: ["Which of the following is a type of database constraint?", 
        "A. UNIQUE", "B. PRIMARY", "C. NOT NULL", "D. All of the above", "D"],
    
    4: ["What is a 'view' in SQL?", 
        "A. A type of table", "B. A stored procedure", "C. A virtual table", "D. A database index", "C"],
    
    5: ["Which of the following is a feature of a relational database?", 
        "A. Tables", "B. No schema", "C. No relationships", "D. JSON support", "A"]
}

for q_num in range(1, 6):
    print(dbms_questions[q_num][0])
    for option_num in range(1, 5):
        print(dbms_questions[q_num][option_num])

    answer = input("Select your answer (A, B, C, or D): ").upper()
    if dbms_questions[q_num][5] == answer:
        score += 1


print("Python Programming Quiz")

python_questions = {
    1: ["How do you comment a single line in Python?", 
        "A. // comment", "B. <!-- comment -->", "C. # comment", "D. /* comment */", "C"],
    
    2: ["What is the output of the following code: print('Python'[-1])?", 
        "A. P", "B. n", "C. o", "D. Error", "B"],
    
    3: ["Which of the following is not a valid data type in Python?", 
        "A. int", "B. float", "C. decimal", "D. complex", "C"],
    
    4: ["Which method is used to remove whitespace from the beginning and end of a string?", 
        "A. strip()", "B. trim()", "C. cut()", "D. remove()", "A"],
    
    5: ["Which of the following is used for creating a set in Python?", 
        "A. set()", "B. []", "C. {}", "D. ()", "A"]
}

for q_num in range(1, 6):
    print(python_questions[q_num][0])
    for option_num in range(1, 5):
        print(python_questions[q_num][option_num])

    answer = input("Select your answer (A, B, C, or D): ").upper()
    if python_questions[q_num][5] == answer:
        score += 1


print("Your final score is:", score)