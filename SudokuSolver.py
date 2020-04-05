# -*- coding: iso-8859-1 -*-
import time
from tkinter import *

window = Tk()
window.title("SudokuSolver")

default_args = {"master":window,"width":8, "background":"grey"}

############################################
# ROWS 1 - 3
############################################
Input1_1 = Entry(**default_args); Input1_2 = Entry(**default_args); Input1_3 = Entry(**default_args)
Label1_1 = Label(window, text="")
Input1_4 = Entry(**default_args); Input1_5 = Entry(**default_args); Input1_6 = Entry(**default_args)
Label1_2 = Label(window, text="")
Input1_7 = Entry(**default_args); Input1_8 = Entry(**default_args); Input1_9 = Entry(**default_args)


Input2_1 = Entry(**default_args); Input2_2 = Entry(**default_args); Input2_3 = Entry(**default_args)
Label2_1 = Label(window, text="")
Input2_4 = Entry(**default_args); Input2_5 = Entry(**default_args); Input2_6 = Entry(**default_args)
Label2_2 = Label(window, text="")
Input2_7 = Entry(**default_args); Input2_8 = Entry(**default_args); Input2_9 = Entry(**default_args)


Input3_1 = Entry(**default_args); Input3_2 = Entry(**default_args); Input3_3 = Entry(**default_args)
Label3_1 = Label(window, text="", font =("Helvetica", 1))
Input3_4 = Entry(**default_args); Input3_5 = Entry(**default_args); Input3_6 = Entry(**default_args)
Label3_2 = Label(window, text="")
Input3_7 = Entry(**default_args); Input3_8 = Entry(**default_args); Input3_9 = Entry(**default_args)
############################################
# ROWS 4 - 6
############################################
Input4_1 = Entry(**default_args); Input4_2 = Entry(**default_args); Input4_3 = Entry(**default_args)
Label4_1 = Label(window, text="")
Input4_4 = Entry(**default_args); Input4_5 = Entry(**default_args); Input4_6 = Entry(**default_args)
Label4_2 = Label(window, text="")
Input4_7 = Entry(**default_args); Input4_8 = Entry(**default_args); Input4_9 = Entry(**default_args)

Input5_1 = Entry(**default_args); Input5_2 = Entry(**default_args); Input5_3 = Entry(**default_args)
Label5_1 = Label(window, text="")
Input5_4 = Entry(**default_args); Input5_5 = Entry(**default_args); Input5_6 = Entry(**default_args)
Label5_2 = Label(window, text="")
Input5_7 = Entry(**default_args); Input5_8 = Entry(**default_args); Input5_9 = Entry(**default_args)


Input6_1 = Entry(**default_args); Input6_2 = Entry(**default_args); Input6_3 = Entry(**default_args)
Label6_1 = Label(window, text="", font=("Helvetica", 1))
Input6_4 = Entry(**default_args); Input6_5 = Entry(**default_args); Input6_6 = Entry(**default_args)
Label6_2 = Label(window, text="")
Input6_7 = Entry(**default_args); Input6_8 = Entry(**default_args); Input6_9 = Entry(**default_args)
############################################
# ROWS 7 - 9
############################################
Input7_1 = Entry(**default_args); Input7_2 = Entry(**default_args); Input7_3 = Entry(**default_args)
Label7_1 = Label(window, text="")
Input7_4 = Entry(**default_args); Input7_5 = Entry(**default_args); Input7_6 = Entry(**default_args)
Label7_2 = Label(window, text="")
Input7_7 = Entry(**default_args); Input7_8 = Entry(**default_args); Input7_9 = Entry(**default_args)


Input8_1 = Entry(**default_args); Input8_2 = Entry(**default_args); Input8_3 = Entry(**default_args)
Label8_1 = Label(window, text="")
Input8_4 = Entry(**default_args); Input8_5 = Entry(**default_args); Input8_6 = Entry(**default_args)
Label8_2 = Label(window, text="")
Input8_7 = Entry(**default_args); Input8_8 = Entry(**default_args); Input8_9 = Entry(**default_args)


Input9_1 = Entry(**default_args); Input9_2 = Entry(**default_args); Input9_3 = Entry(**default_args)
Label9_1 = Label(window, text="")
Input9_4 = Entry(**default_args); Input9_5 = Entry(**default_args); Input9_6 = Entry(**default_args)
Label9_2 = Label(window, text="")
Input9_7 = Entry(**default_args); Input9_8 = Entry(**default_args); Input9_9 = Entry(**default_args)
############################################


# List of input fields:
Inputs = [Input1_1, Input1_2, Input1_3, Input1_4, Input1_5, Input1_6, Input1_7, Input1_8, Input1_9,
 Input2_1, Input2_2, Input2_3, Input2_4, Input2_5, Input2_6, Input2_7, Input2_8, Input2_9,
 Input3_1, Input3_2, Input3_3, Input3_4, Input3_5, Input3_6, Input3_7, Input3_8, Input3_9,
 Input4_1, Input4_2, Input4_3, Input4_4, Input4_5, Input4_6, Input4_7, Input4_8, Input4_9,
 Input5_1, Input5_2, Input5_3, Input5_4, Input5_5, Input5_6, Input5_7, Input5_8, Input5_9,
 Input6_1, Input6_2, Input6_3, Input6_4, Input6_5, Input6_6, Input6_7, Input6_8, Input6_9,
 Input7_1, Input7_2, Input7_3, Input7_4, Input7_5, Input7_6, Input7_7, Input7_8, Input7_9,
 Input8_1, Input8_2, Input8_3, Input8_4, Input8_5, Input8_6, Input8_7, Input8_8, Input8_9,
 Input9_1, Input9_2, Input9_3, Input9_4, Input9_5, Input9_6, Input9_7, Input9_8, Input9_9]


InputsStrings = ['Input1_1', 'Input1_2', 'Input1_3', 'Input1_4', 'Input1_5', 'Input1_6', 'Input1_7', 'Input1_8', 'Input1_9',
 'Input2_1', 'Input2_2', 'Input2_3', 'Input2_4', 'Input2_5', 'Input2_6', 'Input2_7', 'Input2_8', 'Input2_9',
 'Input3_1', 'Input3_2', 'Input3_3', 'Input3_4', 'Input3_5', 'Input3_6', 'Input3_7', 'Input3_8', 'Input3_9',
 'Input4_1', 'Input4_2', 'Input4_3', 'Input4_4', 'Input4_5', 'Input4_6', 'Input4_7', 'Input4_8', 'Input4_9',
 'Input5_1', 'Input5_2', 'Input5_3', 'Input5_4', 'Input5_5', 'Input5_6', 'Input5_7', 'Input5_8', 'Input5_9',
 'Input6_1', 'Input6_2', 'Input6_3', 'Input6_4', 'Input6_5', 'Input6_6', 'Input6_7', 'Input6_8', 'Input6_9',
 'Input7_1', 'Input7_2', 'Input7_3', 'Input7_4', 'Input7_5', 'Input7_6', 'Input7_7', 'Input7_8', 'Input7_9',
 'Input8_1', 'Input8_2', 'Input8_3', 'Input8_4', 'Input8_5', 'Input8_6', 'Input8_7', 'Input8_8', 'Input8_9',
 'Input9_1', 'Input9_2', 'Input9_3', 'Input9_4', 'Input9_5', 'Input9_6', 'Input9_7', 'Input9_8', 'Input9_9']


Num_y = []                                                                              # Liste mit 9 Listen, enhält mögliche Zahlen für jede Zeile
Num_x = []                                                                              # Liste mit 9 Listen, enhält mögliche Zahlen für jede Spalte
Fields_y = []                                                                           # Liste mit 9 Listen der Zahlen pro Zeile
Fields_x = []                                                                           # Liste mit 9 Listen der Zahlen pro Spalte
Fields = []

for p in range(9):
    Num_y.append([str(i) for i in range(1,10)])                                         # Fügt 9 Listen mit den Zahlen 1 bis 9 hinzu
    Num_x.append([str(i) for i in range(1,10)])                                         # Fügt 9 Listen mit den Zahlen 1 bis 9 hinzu
    Fields_y.append(["" for i in range(9)])                                             # Liste mit 9 Listen der Zahlen pro Zeile
    Fields_x.append(["" for i in range(9)])                                             # Liste mit 9 Listen der Zahlen pro Spalte


Fields_y2 = []

def printSudoku():
    for i in range(len(Inputs)):                                                        # 81 mal
        FieldInput = Inputs[i].get()                                                    # Inhalt des Feldes
        FieldInputField = InputsStrings[i]                                              # Name des Feldes
        FieldInputField = FieldInputField.split("Input")                                # FieldInputField wird zu einer Liste
        FieldInputField.remove("")
        FieldInputField = FieldInputField[0].split("_")
        FieldInputField_y = FieldInputField[0]                                          # y-Koordninate des Feldes
        FieldInputField_x = FieldInputField[1]                                          # x-Koordninate des Feldes
        FieldInputField_list_y = int(FieldInputField_y)-1
        FieldInputField_list_x = int(FieldInputField_x)-1

        if FieldInput:
            Fields_y[FieldInputField_list_y][FieldInputField_list_x] = FieldInput       # Füllt die Zahl im Feld an die Stelle des x-Werts in der Liste
            Fields_x[FieldInputField_list_x][FieldInputField_list_y] = FieldInput       # Füllt die Zahl im Feld an die Stelle des y-Werts in der Liste
            Num_y[FieldInputField_list_y].remove(FieldInput)
            print("y:" + str(FieldInputField_list_y) + " " + str(Num_y[FieldInputField_list_y]))
            Num_x[FieldInputField_list_x].remove(FieldInput)
            print("x:" + str(FieldInputField_list_x) + " " + str(Num_x[FieldInputField_list_x]))

    for i in range(len(Inputs)):
        #i = il-1                                                                       # 81 mal
        FieldInput = Inputs[i].get()                                                    # Inhalt des Feldes
        FieldInputField = InputsStrings[i]                                              # Name des Feldes
        FieldInputField = FieldInputField.split("Input")                                # FieldInputField wird zu einer Liste
        FieldInputField.remove("")
        FieldInputField = FieldInputField[0].split("_")
        FieldInputField_y = FieldInputField[0]                                          # y-Koordninate des Feldes
        FieldInputField_x = FieldInputField[1]                                          # x-Koordninate des Feldes
        FieldInputField_list_y = int(FieldInputField_y)-1
        FieldInputField_list_x = int(FieldInputField_x)-1
        for rep in range(9):                                                            ### Nötig? ###
            for n in range(9):
                if len(Num_y[n]) == 1:                                                  # Geht alle Zeilen ab, prüft ob irgendwo nur noch eine Zahl möglich ist
                    print("y: " + str(n))
                    missing_number = Num_y[n][0]
                    print("Nur noch eine mögliche Zahl: " + missing_number)
                    for x_value, content in enumerate(Fields_y[n]):                     # Geht jedes Feld in der gefundenen Zeile ab, überprüft Inhalt
                        if content == "":                                               # wenn das Feld noch nicht ausgefüllt wurde
                            print("Trage " + missing_number + " in Liste für y=" + str(n) + " an der Stelle " + str(x_value) + " ein...")
                            Fields_y[n][x_value] = missing_number
                            print("y=" + str(n) + " " + str(Fields_y[n]))               # Eintragen der letztmöglichen Zahl dieser Zeile #Num_y[n][0]
                            print("Trage " + missing_number + " auch in Liste für x=" + str(x_value) + " an der Stelle " + str(n) + " ein...")
                            Fields_x[x_value][n] = missing_number                       # Gleiche Zahl wird auch in Spalte eingetragen
                            print("x=" + str(x_value) + " " + str(Fields_x[x_value]))
                            print("Entferne " + missing_number + " aus Liste für x=" + str(x_value) + " ...")
                            Num_x[x_value].remove(missing_number)                       # Entfernt eingefügte Zahl aus Liste möglicher Zahlen für Spalte
                            print("übrig bleiben: x=" + str(x_value) + " " + str(Num_x[x_value]))
                            print("Leere Liste für y=" + str(n) + " ...")
                            Num_y[n].clear()                                            # Leert Liste möglicher Zahlen für Zeile -> Entfernt eingefügte Zahl
                            print("#########")

                if len(Num_x[n]) == 1:                                                  # Geht alle Spalten ab, prüft ob irgendwo nur noch eine Zahl möglich ist
                    print("x: " + str(n))
                    missing_number = Num_x[n][0]
                    print("nur noch eine mögliche Zahl: " + missing_number)
                    for y_value, content in enumerate(Fields_x[n]):                     # Geht jedes Feld in der gefundenen Spalte ab, überprüft Inhalt
                        if content == "":                                               # wenn das Feld noch nicht ausgefüllt wurde
                            print("Trage " + missing_number + " in die Liste für x=" + str(n) + " an der Stelle " + str(y_value) + " ein...")
                            Fields_x[n][y_value] = missing_number                       # Eintragen der letztmöglichen Zahl dieser Spalte
                            print("x=" + str(n) + " " + str(Fields_x[n]))
                            print("Trage " + missing_number + " auch in die Liste für y=" + str(y_value) + " an der Stelle " + str(n) + " ein...")
                            Fields_y[y_value][n] = missing_number                       # Gleiche Zahl wird auch in Zeile eingetragen
                            print("y=" + str(y_value) + " " + str(Fields_y[y_value]))
                            print("Entferne " + missing_number + " aus Liste für y=" + str(y_value) + " ...")
                            Num_y[y_value].remove(missing_number)                       # Entfernt eingefügte Zahl aus Liste möglicher Zahlen für Zeile
                            print("übrig bleiben: y= " + str(y_value) + " " + str(Num_y[y_value]))
                            print("Leere Liste für x= " + str(n) + " ...")
                            Num_x[n].clear()                                            # Leert Liste möglicher Zahlen für Spalte -> Entfernt eingefügte Zahl
                            print("#########")


    for List_num in range(9):
        for num in range(9):
            Fields.append(Fields_y[List_num][num])

    for content in range(len(Fields)):
        Inputs[content].delete(0, END)
        Inputs[content].insert(0, Fields[content])

myButton = Button(window, text="Solve", command=printSudoku)


columns = ["1", "2", "3", "5", "6", "7", "9", "10", "11"]
counter = 0

for row in range(1, 12):
    if row != 4 and row != 8:
        for column_n in range(len(columns)):
            Inputs[counter].grid(row=row, column=columns[column_n])
            counter += 1
    elif row == 4:
        Label3_1.grid(row=4, column=4)
    elif row == 8:
        Label6_1.grid(row=8, column=8)

myButton.grid(row="12", column="6")
window.mainloop()
