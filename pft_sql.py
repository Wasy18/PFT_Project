import datetime
import sqlite3

import matplotlib.pyplot as plt

con = sqlite3.connect('MyApp.db')
cursor = con.cursor()


def get_exercises():
    cursor.execute("SELECT id, exercise_name FROM 'main'.'exercises'")
    ex = cursor.fetchall()
    return ex


def pft_sql():
    cursor.execute("SELECT id, exercise_name FROM 'main'.'exercises'")
    ex = cursor.fetchall()
    for el in ex:
        print(el[0], el[1])
    ex_choice = input("Select an exercise (1-" + str(len(ex)) + ")")

    cursor.execute(
        "SELECT date, history_exercises.exercise_id, weightlb FROM history_exercises INNER JOIN history ON history_id "
        "= history.id AND exercise_id =" + str(ex_choice) + " AND max_reps < 5 AND reptype = 1")
    top_sets = cursor.fetchall()

    x = []
    y = []
    for el in top_sets:
        x.append(datetime.datetime.fromtimestamp(el[0] / 1000))
        y.append(el[2])
        print(datetime.date.fromtimestamp(el[0] / 1000), el[2])
    plt.style.use("seaborn-darkgrid")
    plt.plot_date(x, y, linestyle="solid")
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    plt.title(ex[el[1] - 1][1])
    plt.show()
    # print(cursor.fetchall())

    input("Press Enter to Exit")
