from random import shuffle

questions =[{
    """ What is a correct syntax to output "Hello World" in Python?:
    a. p("Hello World")
    b. print("Hello World")
    c. echo("hello World")
    """: "b"},

    {""" How do you insert COMMENTS in Python code?:
    a. /* This is a comment */
    b. // This is comment
    c. # This is a comment
    """: "a"},

    {""" Which one is NOT a legal variable name?
    a. _myVar
    b. my_var
    c. Myvar
    """: "c"},

    {""" How do you create a variable with the numeric value 5?:
    a. x= int(5)
    b. x= 5
    c. Both answers are correct
    """: "c"},

    {""" What is the correct file extension for Python files?:
    a. .py
    b. .pthy
    c. .pt
    """: "a"}
    ]

#shuffleList
shuffle(questions)

#Score tracking
highest_score = 0

# Flag to control loop
should_continue = True


#Quiz Functiom
def quiz():
    current_score = 0
    global highest_score, should_continue

    for question_number,  question in enumerate(questions, start=1):
        current_question = list(question.keys())[0]
        current_answer = list(question.values())[0]
        print(f"{question_number}. {current_question}")
        

        user_response  = input("Choose the correct answer: " ).lower()
        if user_response == current_answer:
            current_score += 1
        else:
            print(f"Your answer was wrong. the correct answer is {current_answer}\n")

    highest_score = max(current_score, highest_score)
    print(f"Your current score is {current_score} and your highest score so far is {highest_score}")

    choice = input("Do you want try again?. please type yes/no: ").lower()
    if choice == "yes":
        quiz()
    else:
        should_continue = False
        print("Thanks for attempting our quiz ")

#Run the main code
while should_continue:
    quiz()