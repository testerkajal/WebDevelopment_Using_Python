import json

with open("questions.json", 'r') as file:
    content = file.read()
    data  = json.loads(content)

score =0
for question in data:
    print(question["question_text"])

    for index, option in enumerate(question["options"]):
        print(f"{index+1} - {option}")
    user_choice = int(input("Please choose correct answer: \n"))
    if user_choice == question["correct_ans"]:
          print("Your guess is correct")
          score +=1
    else:
        print(f"Incorrect answer, correct Answer is: {question["correct_ans"]}")
    print(f"Your final score is: {score}/{len(data)}")
        