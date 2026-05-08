import json

with open('Questions.json', 'r') as file:    
    content = file.read()

data = json.loads(content)

score = 0

for question in data:
    print(question['question'])
    for index, answer in enumerate(question['answers']):
        print(f" {index + 1}. {answer}")
    user_choice = int(input("Enter  your answer: "))
    if user_choice == question['correct_answer']:
        print("Correct!")
        score += 1  
    else:
        print("Incorrect.")
print(f"Your final score is: {score}/{len(data)}")