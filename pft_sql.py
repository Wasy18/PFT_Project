import datetime
import sqlite3
import tkinter as tk

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")


class PFT_Database:
    def __init__(self, parent, db):
        self.parent = parent
        self.database = db
        self.con = sqlite3.connect(self.database)
        self.cursor = self.con.cursor()

        self.cursor.execute("SELECT id, exercise_name FROM 'main'.'exercises'")
        self.ex = self.cursor.fetchall()
        print("CONNECT TO DATABASE")

    def get_exercises(self):
        self.cursor.execute("SELECT id, exercise_name FROM 'main'.'exercises'")
        ex = self.cursor.fetchall()
        return ex

    def generate_report(self, report, ex_type, date_start, date_end):

        if report == 1:
            self.bodyweight_report(date_start, date_end)

        if report == 2:
            self.plus_one(ex_type, date_start, date_end)

        if report == 3:
            self.whole_set(ex_type, date_start, date_end)

    def bodyweight_report(self, date_start, date_end):
        print("BODYWEIGHT")
        self.cursor.execute(
            "SELECT date, weight FROM 'main'.'body_weight' WHERE date BETWEEN " + str(int(date_start)) + " AND " + str(
                int(date_end)) + " ORDER BY date ASC")
        bw = self.cursor.fetchall()

        try:
            max_x = max(bw, key=lambda z_set: z_set[1])
        except:
            tk.messagebox.showwarning(title="Read Failure", message="Insufficient Data For Current Selection")
            return

        x = []
        y = []
        for el in bw:
            x.append(datetime.datetime.fromtimestamp(el[0] / 1000))
            y.append(el[1])

        plt.ylim(0, max_x[1] + (1 / 5) * max_x[1])
        plt.plot(x, y, marker='.')
        plt.xlabel("Date")
        plt.ylabel("Bodyweight")
        plt.title("Bodyweight Report")
        plt.show()

    def plus_one(self, ex_type, date_start, date_end):

        print("PLUS_ONE")
        self.cursor.execute(
            "SELECT date, history_exercises.exercise_id, weightlb FROM history_exercises INNER JOIN history ON "
            "history_id = history.id AND exercise_id =" + str(ex_type) + " AND reptype = 1 WHERE date BETWEEN " +
            str(int(date_start)) + " AND " + str(int(date_end)) + " ORDER BY date ASC, weightlb ASC")
        po = self.cursor.fetchall()

        try:
            max_x = max(po, key=lambda z_set: z_set[2])
        except:
            tk.messagebox.showwarning(title="Read Failure", message="Insufficient Data For Current Selection")
            return

        x = []
        y = []
        for el in po:
            print(el)
            print(el[2])
            x.append(datetime.datetime.fromtimestamp(el[0] / 1000))
            y.append(el[2])

        plt.ylim(0, max_x[2] + (1 / 5) * max_x[2])
        plt.plot(x, y, marker='.')
        plt.xlabel("Date")
        plt.ylabel("Weight")
        print(ex_type)
        print(type(self.ex))
        plt.title(self.ex[int(ex_type)-1][1] + " 1+ Report")
        plt.show()

    def whole_set(self, ex_type, date_start, date_end):
        # TODO
        print("WHOLE_SET")
        self.cursor.execute(
            "SELECT date, history_exercises.exercise_id, weightlb FROM history_exercises INNER JOIN history ON "
            "history_id = history.id AND exercise_id =" + str(ex_type) + " WHERE date BETWEEN " +
            str(int(date_start)) + " AND " + str(int(date_end)) + " ORDER BY date ASC, weightlb ASC")
        ws = self.cursor.fetchall()

        try:
            max_x = max(ws, key=lambda z_set: z_set[2])
        except:
            tk.messagebox.showwarning(title="Read Failure", message="Insufficient Data For Current Selection")
            return

        x = []
        y = []
        for el in ws:
            print(el)
            print(el[2])
            x.append(datetime.datetime.fromtimestamp(el[0] / 1000))
            y.append(el[2])

        plt.ylim(0, max_x[2] + (1 / 5) * max_x[2])
        plt.plot(x, y, marker='.')
        plt.xlabel("Date")
        plt.ylabel("Weight")
        print(ex_type)
        print(type(self.ex))
        plt.title(self.ex[int(ex_type) - 1][1] + " Whole Set Report")
        plt.show()




    def pft_sql(self, choice):
        self.cursor.execute("SELECT id, exercise_name FROM 'main'.'exercises'")
        ex = self.cursor.fetchall()

        for el in ex:
            # print(el[0], el[1])
            pass
        # ex_choice = input("Select an exercise (1-" + str(len(ex)) + ")")
        ex_choice = choice
        self.cursor.execute(
            "SELECT date, history_exercises.exercise_id, weightlb FROM history_exercises INNER JOIN history ON history_id "
            "= history.id AND exercise_id =" + str(ex_choice) + " AND max_reps < 5 AND reptype = 1")
        top_sets = self.cursor.fetchall()

        max_x = max(top_sets, key=lambda z_set: z_set[2])
        x = []
        y = []
        for el in top_sets:
            x.append(datetime.datetime.fromtimestamp(el[0] / 1000))
            print(datetime.datetime.fromtimestamp(el[0] / 1000))
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
