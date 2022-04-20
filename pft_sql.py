import datetime
import sqlite3

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

# con = sqlite3.connect('MyApp.db')
# cursor = con.cursor()


def connect_to_database(db):
    con = sqlite3.connect(db)
    cursor = con.cursor()


def get_exercises():
    cursor.execute("SELECT id, exercise_name FROM 'main'.'exercises'")
    ex = cursor.fetchall()
    return ex


def pft_sql(choice):
    cursor.execute("SELECT id, exercise_name FROM 'main'.'exercises'")
    ex = cursor.fetchall()

    for el in ex:
        # print(el[0], el[1])
        pass
    # ex_choice = input("Select an exercise (1-" + str(len(ex)) + ")")
    ex_choice = choice
    cursor.execute(
        "SELECT date, history_exercises.exercise_id, weightlb FROM history_exercises INNER JOIN history ON history_id "
        "= history.id AND exercise_id =" + str(ex_choice) + " AND max_reps < 5 AND reptype = 1")
    top_sets = cursor.fetchall()

    max_x = max(top_sets, key=lambda z_set: z_set[2])
    x = []
    y = []
    for el in top_sets:
        x.append(datetime.datetime.fromtimestamp(el[0] / 1000))
        y.append(el[2])
        x_line = datetime.datetime.fromtimestamp(el[0] / 1000)

        plt.vlines(x_line, ymin=0, ymax=el[2])

    # print(datetime.date.fromtimestamp(el[0] / 1000), el[2])
    plt.axhline(0, color='black')
    plt.ylim(0, max_x[2] + (1 / 5) * max_x[2])
    plt.style.use("seaborn-darkgrid")
    plt.plot_date(x, y)
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    plt.title(ex[el[1] - 1][1])
    plt.show()
    # print(cursor.fetchall())
