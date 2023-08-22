import tkinter as tk
import random

def load_data(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            country, capital = line.strip().split('-')
            data[country] = capital
    return data

def save_data(filename, data):
    with open(filename, 'w') as file:
        for country, capital in data.items():
            file.write(f"{country}-{capital}\n")

def show_capital_or_country():
    input_text = input_entry.get().strip().title()
    if input_text in country_capital_dict:
        result_label.config(text=f"Столица: {country_capital_dict[input_text]}")
    elif input_text in country_capital_dict.values():
        result_label.config(text=f"Страна: {list(country_capital_dict.keys())[list(country_capital_dict.values()).index(input_text)]}")
    else:
        result_label.config(text="Нет информации о введенном значении")

def add_to_dict():
    new_country = new_country_entry.get().strip().title()
    new_capital = new_capital_entry.get().strip().title()
    country_capital_dict[new_country] = new_capital
    save_data("countries.txt", country_capital_dict)
    new_country_entry.delete(0, tk.END)
    new_capital_entry.delete(0, tk.END)

def start_quiz():
    global quiz_data, total_questions, current_question, correct_answers, wins, losses
    total_questions = int(rounds_entry.get() or 5)  # Если не выбрано, по умолчанию 5 раундов
    quiz_data = list(country_capital_dict.items())
    random.shuffle(quiz_data)
    current_question = 0
    correct_answers = 0
    wins = 0
    losses = 0
    next_question()

def next_question():
    global current_question
    if current_question < total_questions:
        question_country, correct_answer = quiz_data[current_question]
        question_label.config(text=f"Название столицы страны: {question_country}")
        current_question += 1
        submit_button.config(state=tk.NORMAL)
    else:
        calculate_quiz_result()

def check_answer():
    global correct_answers, wins, losses
    user_answer = answer_entry.get().strip().title()
    correct_answer = quiz_data[current_question - 1][1]
    if user_answer == correct_answer:
        correct_answers += 1
        wins += 1
    else:
        losses += 1
    next_question()

def calculate_quiz_result():
    percentage = (correct_answers / total_questions) * 100
    result_label.config(text=f"Результат: {percentage:.2f}% правильных ответов")
    wins_label.config(text=f"Побед: {wins}")
    losses_label.config(text=f"Поражений: {losses}")
    question_label.config(text="")
    submit_button.config(state=tk.DISABLED)

country_capital_dict = load_data("countries.txt")
quiz_data = []
total_questions = 0
current_question = 0
correct_answers = 0
wins = 0
losses = 0

window = tk.Tk()
window.title("Страны и столицы")

input_label = tk.Label(window, text="Введите название страны или столицы:")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

show_button = tk.Button(window, text="Показать", command=show_capital_or_country)
show_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

add_label = tk.Label(window, text="Добавить новую пару страна-столица:")
add_label.pack()

new_country_label = tk.Label(window, text="Страна:")
new_country_label.pack()

new_country_entry = tk.Entry(window)
new_country_entry.pack()

new_capital_label = tk.Label(window, text="Столица:")
new_capital_label.pack()

new_capital_entry = tk.Entry(window)
new_capital_entry.pack()

add_button = tk.Button(window, text="Добавить", command=add_to_dict)
add_button.pack()

quiz_label = tk.Label(window, text="Проверка знаний:")
quiz_label.pack()

rounds_label = tk.Label(window, text="Количество раундов:")
rounds_label.pack()

rounds_entry = tk.Entry(window)
rounds_entry.pack()

start_quiz_button = tk.Button(window, text="Начать проверку знаний", command=start_quiz)
start_quiz_button.pack()

question_label = tk.Label(window, text="")
question_label.pack()

answer_entry = tk.Entry(window)
answer_entry.pack()

submit_button = tk.Button(window, text="Проверить", command=check_answer, state=tk.DISABLED)
submit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

wins_label = tk.Label(window, text="Побед: 0")
wins_label.pack()

losses_label = tk.Label(window, text="Поражений: 0")
losses_label.pack()

window.mainloop()
