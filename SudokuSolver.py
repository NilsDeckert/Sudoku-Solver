from tkinter import *

window = Tk()
window.title("GUI Test")

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


Num_y = []                                                              # Liste mit 9 Listen, enhält mögliche Zahlen für jede Zeile
Num_x = []                                                              # Liste mit 9 Listen, enhält mögliche Zahlen für jede Spalte

for p in range(9):
    Num_y.append([str(i) for i in range(1,10)])                         # Fügt 9 Listen mit den Zahlen 1 bis 9 hinzu
    Num_x.append([str(i) for i in range(1,10)])                         # Fügt 9 Listen mit den Zahlen 1 bis 9 hinzu
    #Num_y.append(["1","2","3","4","5","6","7","8","9"])
    #Num_x.append(["1","2","3","4","5","6","7","8","9"])

Fields_y = [[],[],[],[],[],[],[],[],[]]                                 # Liste mit 9 Listen der Zahlen pro Zeile
Fields_x = [[],[],[],[],[],[],[],[],[]]                                 # Liste mit 9 Listen der Zahlen pro Spalte
Fields_y2 = []
# for n in range(9):
#     if n <= 9:
#         Fields_y1.append(Num_x[n])
#     elif 9 > n <= 18:
#         Fields_y2.append(Num_x[n])

#p4rint(Fields_y1)

def printSudoku():
    for il in range(len(Inputs)+1):
        i = il-1                                        # 81 mal
        FieldInput = Inputs[i].get()                                    # Inhalt des Feldes
        FieldInputField = InputsStrings[i]                              # Name des Feldes
        FieldInputField = FieldInputField.split("Input")                # FieldInputField wird zu einer Liste
        FieldInputField.remove("")
        FieldInputField = FieldInputField[0].split("_")
        FieldInputField_y = FieldInputField[0]                          # y-Koordninate des Feldes
        FieldInputField_x = FieldInputField[1]                          # x-Koordninate des Feldes
        FieldInputField_list_y = int(FieldInputField_y)-1
        FieldInputField_list_x = int(FieldInputField_x)-1
        #print("x:" + FieldInputField_x + " y:" + FieldInputField_y)

        if not Inputs[i].get():                                         # Wenn das Feld leer ist
            #if len(Fields_y[FieldInputField_list_y]) < 8:
            Fields_y[FieldInputField_list_y].append("")                 # In der Liste der vorhandenen Werte Platzhalter einfügen
            #if len(Fields_x[FieldInputField_list_x]) < 8:
            Fields_x[FieldInputField_list_x].append("")                 # In der Liste der vorhandenen Werte Platzhalter einfügen
        else:                                                           # Wenn das Feld nicht leer ist
            try:
                Num_y[FieldInputField_list_y].remove(FieldInput)            # Entfernt Inhalt des Felds aus Liste möglicher Zahlen für diese Reihe
                Num_x[FieldInputField_list_x].remove(FieldInput)            # Entfernt Inhalt des Felds aus Liste möglicher Zahlen für diese Spalte

                Fields_y[FieldInputField_list_y].append(FieldInput)         # Fügt Inhalt des Feldes in die Liste der Zahlen für diese Zeile ein
                Fields_x[FieldInputField_list_x].append(FieldInput)         # Fügt Inhalt des Feldes in die Liste der Zahlen für diese Spalte ein
            except:
                return
            print(Num_y[FieldInputField_list_y])
            for n in range(8):                                          # 9 mal -> geht alle Zeile und Spalten durch
                if len(Num_y[n]) == 1:                                  # Wenn nur noch eine Zahl in dieser Zeile möglich ist
                    print("ALERT Y: " + str(n+1))
                    print("Letzte mögliche Zahl: " + str(Num_y[n]))
                    if len(Fields_y[int(FieldInputField_list_y)]) == 9:
                        for a, b in enumerate(Fields_y[int(FieldInputField_list_y)]):
                            # print("a: " + str(a))
                            # print("b: "+ str(b))
                            if b == "":
                                print("x-Koordinate: " + str(a+1))
                                Fields_y[int(FieldInputField_list_y)][a] = Num_y[n][0]
                        # Fields_y[int(FieldInputField_list_y)].append(Num_y[n][0])   # Letze mögliche Zahl hinten anhängen
                    elif len(Fields_y[FieldInputField_list_y]) == 8:
                        Fields_y[int(FieldInputField_list_y)].append(Num_y[n][0])   # Letze mögliche Zahl hinten anhängen
                        #Fields_y[FieldInputField_list_y] = [''.join(Num_y[n][0]) if x=="" else x for x in Fields_y[FieldInputField_list_y]] #Ersetzt Platzhalter mit letzer möglichen Zahl
                    Num_y[n].clear()                                    # Leert Liste mit möglichen Zahlen, da die letzte nun auch vergeben wurde
                if len(Num_x[n]) == 1:
                    print("ALERT X: " + str(n+1))
                    print(Num_x[n])
                    if len(Fields_x[FieldInputField_list_x]) == 8:
                        Fields_x[int(FieldInputField_list_x)].append(Num_x[n][0])
                    else:
                        Fields_x[FieldInputField_list_x] = [''.join(Num_x[n][0]) if x=="" else x for x in Fields_x[FieldInputField_list_x]] #Ersetzt Platzhalter mit letzer möglichen Zahl
                    Num_x[n].clear()




        print(Fields_y)
        # print(Fields_x)
    for z in range(len(Inputs)):
        try:
            Inputs[z].delete(0, END)
            if z <= 8:
                Inputs[z].insert(0, Fields_y[0][z])
            if 8 < z <= 17:
                Inputs[z].insert(0, Fields_y[1][z-9])
        except:
            return

        # if z <= 8:
        #     Inputs[z].delete(0, END)
        #     Inputs[z].insert(0, Fields_y[z])
        # z1.delete(0, END)
        # z1.insert(0, z)

myButton = Button(window, text="Button", command=printSudoku)

#Input1 = Entry(window)

Input1_1.grid(row="1", column="1")
Input1_2.grid(row="1", column="2")
Input1_3.grid(row="1", column="3")
#Label1_1.grid(row="1", column="4") #
Input1_4.grid(row="1", column="5")
Input1_5.grid(row="1", column="6")
Input1_6.grid(row="1", column="7")
#Label1_2.grid(row="1", column="8") #
Input1_7.grid(row="1", column="9")
Input1_8.grid(row="1", column="10")
Input1_9.grid(row="1", column="11")

Input2_1.grid(row="2", column="1")
Input2_2.grid(row="2", column="2")
Input2_3.grid(row="2", column="3")
Input2_4.grid(row="2", column="5")
Input2_5.grid(row="2", column="6")
Input2_6.grid(row="2", column="7")
Input2_7.grid(row="2", column="9")
Input2_8.grid(row="2", column="10")
Input2_9.grid(row="2", column="11")

Input3_1.grid(row="3", column="1")
Input3_2.grid(row="3", column="2")
Input3_3.grid(row="3", column="3")
Input3_4.grid(row="3", column="5")
Input3_5.grid(row="3", column="6")
Input3_6.grid(row="3", column="7")
Input3_7.grid(row="3", column="9")
Input3_8.grid(row="3", column="10")
Input3_9.grid(row="3", column="11")

Label3_1.grid(row="4", column="4")

Input4_1.grid(row="5", column="1")
Input4_2.grid(row="5", column="2")
Input4_3.grid(row="5", column="3")
Input4_4.grid(row="5", column="5")
Input4_5.grid(row="5", column="6")
Input4_6.grid(row="5", column="7")
Input4_7.grid(row="5", column="9")
Input4_8.grid(row="5", column="10")
Input4_9.grid(row="5", column="11")

Input5_1.grid(row="6", column="1")
Input5_2.grid(row="6", column="2")
Input5_3.grid(row="6", column="3")
Input5_4.grid(row="6", column="5")
Input5_5.grid(row="6", column="6")
Input5_6.grid(row="6", column="7")
Input5_7.grid(row="6", column="9")
Input5_8.grid(row="6", column="10")
Input5_9.grid(row="6", column="11")

Input6_1.grid(row="7", column="1")
Input6_2.grid(row="7", column="2")
Input6_3.grid(row="7", column="3")
Input6_4.grid(row="7", column="5")
Input6_5.grid(row="7", column="6")
Input6_6.grid(row="7", column="7")
Input6_7.grid(row="7", column="9")
Input6_8.grid(row="7", column="10")
Input6_9.grid(row="7", column="11")

Label6_1.grid(row="8", column="8")

Input7_1.grid(row="9", column="1")
Input7_2.grid(row="9", column="2")
Input7_3.grid(row="9", column="3")
Input7_4.grid(row="9", column="5")
Input7_5.grid(row="9", column="6")
Input7_6.grid(row="9", column="7")
Input7_7.grid(row="9", column="9")
Input7_8.grid(row="9", column="10")
Input7_9.grid(row="9", column="11")

Input8_1.grid(row="10", column="1")
Input8_2.grid(row="10", column="2")
Input8_3.grid(row="10", column="3")
Input8_4.grid(row="10", column="5")
Input8_5.grid(row="10", column="6")
Input8_6.grid(row="10", column="7")
Input8_7.grid(row="10", column="9")
Input8_8.grid(row="10", column="10")
Input8_9.grid(row="10", column="11")

Input9_1.grid(row="11", column="1")
Input9_2.grid(row="11", column="2")
Input9_3.grid(row="11", column="3")
Input9_4.grid(row="11", column="5")
Input9_5.grid(row="11", column="6")
Input9_6.grid(row="11", column="7")
Input9_7.grid(row="11", column="9")
Input9_8.grid(row="11", column="10")
Input9_9.grid(row="11", column="11")

myButton.grid(row="12", column="6")
#Input1.grid(row="5", column="2")
window.mainloop()
