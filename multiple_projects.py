import pandas as pd

# TASK 1: Quiz Application 
questions = [
    {"question": "What is the capital of France?", "answer": "Paris", "marks": 5, "penalty": -2},
    {"question": "What is 2 + 2?", "answer": "4", "marks": 5, "penalty": -2},
    {"question": "What is the color of the sky on a clear day?", "answer": "Blue", "marks": 5, "penalty": -2},
]
total_score = 0
current_question = 1
total_questions = len(questions)

for q in questions:
    print(f"\nQuestion {current_question}/{total_questions}: {q['question']}")
    user_answer = input("Your Answer: ").strip()
    if user_answer.lower() == q["answer"].lower():
        total_score += q["marks"]
        print("Correct! +", q["marks"], "marks")
    else:
        total_score += q["penalty"]
        print("Wrong! ", q["penalty"], "penalty")
    current_question += 1

print("\nQuiz Completed!")
print("Your Total Score is:", total_score)

if total_score >= 12:
    print("Excellent work!")
elif total_score >= 5:
    print("Good job, you passed!")
else:
    print("Better luck next time!")

# TASK 2: Swap Variables Using Arithmetic
a = int(input("\nEnter value of a: "))
b = int(input("Enter value of b: "))

print(f"Before swapping: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")

# TASK 3: Save User Details to Excel 
try:
    name = input("\nEnter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email address: ")

    user_data = {
        "Name": [name],
        "Age": [age],
        "Email": [email]
    }
    df = pd.DataFrame(user_data)
    df.to_excel("user_details.xlsx", index=False)
    print("User details saved successfully to 'user_details.xlsx'.")
    
except ValueError:
    print("Invalid input. Age must be a number.")
except Exception as e:
    print("An error occurred:", e)