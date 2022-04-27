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

        if report == 4:
            self.top_set(ex_type, date_start, date_end)

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
        plt.title(self.ex[int(ex_type)-1][1] + " 1+ Set Report")
        plt.show()

    def top_set(self, ex_type, date_start, date_end):

        print("TOP_SET")
        self.cursor.execute(
            "SELECT date, history_exercises.exercise_id, weightlb FROM history_exercises INNER JOIN history ON "
            "history_id = history.id AND exercise_id =" + str(ex_type) + " WHERE date BETWEEN " +
            str(int(date_start)) + " AND " + str(int(date_end)) + " ORDER BY date ASC, weightlb DESC")
        po = self.cursor.fetchall()

        try:
            max_x = max(po, key=lambda z_set: z_set[2])
        except:
            tk.messagebox.showwarning(title="Read Failure", message="Insufficient Data For Current Selection")
            return
        x = []
        y = []
        prev_date = None

        for el in po:
            if prev_date == datetime.datetime.fromtimestamp(el[0] / 1000):
                continue
            else:
                prev_date = datetime.datetime.fromtimestamp(el[0] / 1000)

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
        plt.title(self.ex[int(ex_type)-1][1] + " Top Set Report")
        plt.show()
        pass

    def whole_set(self, ex_type, date_start, date_end):

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
