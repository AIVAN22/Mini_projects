import tkinter as tk
import datetime as dt
import time
from ID_ATM import passwords

print(passwords)


def pin_id():
    e_c = int(e_EnterCard.get())
    e_p = int(e_EnterPIN.get())
    CreditCardAmount = float(1500)
    DebitCardAmount = float(500)
    window_list = []
    deposit_list = []
    debit_deposit = []
    draw_deposit = []

    if e_c == 1:  # Dictonery ID & PIN
        if e_p == 1:
            new_window = tk.Tk()
            new_window.config(bg="#6b6e74")
            new_window.resizable(False, False)
            new_window.geometry("750x300")
            window.destroy()

            def Deposit_History():
                deposit_history = tk.Tk()
                deposit_history.config(bg="#6b6e74")
                deposit_history.resizable(False, False)
                deposit_history.geometry("750x300")

                frame_deposit = tk.Frame(
                    deposit_history,
                    bg="white",
                    bd=5,
                    padx=10,
                    pady=10,
                    relief=tk.SUNKEN,
                )
                frame_deposit.place()
                frame_deposit.pack()

                list_depo = tk.Listbox(frame_deposit, width=30)
                list_depo.insert(1, *deposit_list)
                list_depo.pack()

            def Windraw_History():
                windraw_history = tk.Tk()
                windraw_history.config(bg="#6b6e74")
                windraw_history.resizable(False, False)
                windraw_history.geometry("750x300")

                frame_wind = tk.Frame(
                    windraw_history,
                    bg="white",
                    bd=5,
                    padx=10,
                    pady=10,
                    relief=tk.SUNKEN,
                )
                frame_wind.place()
                frame_wind.pack()

                list_draw = tk.Listbox(frame_wind, width=30)
                list_draw.insert(1, *window_list)
                list_draw.pack()

            def Transfer_B():

                trans_window = tk.Tk()
                trans_window.config(bg="#6b6e74")
                trans_window.resizable(False, False)
                trans_window.geometry("750x300")

                frame = tk.Frame(
                    trans_window, bg="white", bd=5, padx=30, pady=30, relief=tk.SUNKEN
                )
                frame.place()
                frame.pack(ipadx=3, ipady=10, expand=True)

                List_Trans = tk.Listbox(frame, width=30)
                List_Trans.insert(1, "2012-01-02  ATM  Brazilia")
                List_Trans.insert(1, "2012-03-12  ATM  Londion")
                List_Trans.insert(1, "2022-11-07  ATM  New York")

                List_Trans.pack()

            def Deposit_BB():
                deposit_window = tk.Tk()
                deposit_window.config(bg="#6b6e74")
                deposit_window.resizable(False, False)
                deposit_window.geometry("750x300")
                # new_window.destroy()

                def More_DB():
                    def click_0(int):
                        more_entry.insert(tk.END, 0)

                    def click_1(int):
                        more_entry.insert(tk.END, 1)

                    def click_2(int):
                        more_entry.insert(tk.END, 2)

                    def click_3(int):
                        more_entry.insert(tk.END, 3)

                    def click_4(int):
                        more_entry.insert(tk.END, 4)

                    def click_5(int):
                        more_entry.insert(tk.END, 5)

                    def click_6(int):
                        more_entry.insert(tk.END, 6)

                    def click_7(int):
                        more_entry.insert(tk.END, 7)

                    def click_8(int):
                        more_entry.insert(tk.END, 8)

                    def click_9(int):
                        more_entry.insert(tk.END, 9)

                    def click_C():
                        more_entry.delete(0, tk.END)

                    def click_Done():

                        date = dt.datetime.now()
                        result = more_entry.get()
                        list_1 = [
                            result,
                            CreditCardAmount + float(result),
                            f"{date:%d,%m,%Y}",
                            time.strftime("%H:%M:%S"),
                        ]
                        deposit_list.append(list_1)
                        NCA = CreditCardAmount + float(result)
                        print(NCA)
                        print(list_1)

                        message_ = tk.Tk()
                        message_.resizable(False, False)
                        message_.geometry("750x300")

                        frame_message = tk.Frame(message_, bd=3, relief=tk.SUNKEN)
                        frame_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

                        message_label = tk.Label(
                            frame_message,
                            text="Operation is complete.\nThank you for using our ATM.",
                            font="Times 13",
                            padx=10,
                            pady=10,
                        )
                        message_label.place()
                        message_label.pack()

                    more_window = tk.Tk()
                    more_window.resizable(False, False)
                    more_window.geometry("750x300")
                    deposit_window.destroy()

                    Frame_entry = tk.Frame(
                        more_window, bd=5, relief=tk.SUNKEN, height=30
                    )
                    Frame_entry.place()
                    Frame_entry.pack(side=tk.TOP)

                    more_entry = tk.Entry(more_window, width=10, font=("Arial", 25))
                    more_entry.place()
                    more_entry.pack(side=tk.TOP)

                    Frame_numbers_0 = tk.Frame(
                        more_window, bg="white", bd=5, relief=tk.SUNKEN
                    )
                    Frame_numbers_0.place()
                    Frame_numbers_0.pack(side=tk.BOTTOM)

                    button_C = tk.Button(
                        Frame_numbers_0,
                        text="C",
                        width=4,
                        height=2,
                        command=lambda: click_C(),
                    )
                    button_C.pack(side=tk.LEFT)

                    button_0 = tk.Button(
                        Frame_numbers_0,
                        text="0",
                        width=4,
                        height=2,
                        command=lambda: click_0("0"),
                    )
                    button_0.pack(side=tk.LEFT)

                    button_Done = tk.Button(
                        Frame_numbers_0,
                        text="Done",
                        width=4,
                        height=2,
                        command=click_Done,
                    )
                    button_Done.pack(side=tk.RIGHT)

                    Frame_numbers = tk.Frame(
                        more_window, bg="white", bd=5, relief=tk.SUNKEN
                    )
                    Frame_numbers.place()
                    Frame_numbers.pack(side=tk.BOTTOM)

                    button_1 = tk.Button(
                        Frame_numbers,
                        text="1",
                        width=4,
                        height=2,
                        command=lambda: click_1("1"),
                    )
                    button_1.pack(side=tk.LEFT)

                    button_2 = tk.Button(
                        Frame_numbers,
                        text="2",
                        width=4,
                        height=2,
                        command=lambda: click_2("2"),
                    )
                    button_2.pack(side=tk.LEFT)

                    button_3 = tk.Button(
                        Frame_numbers,
                        text="3",
                        width=4,
                        height=2,
                        command=lambda: click_3("3"),
                    )
                    button_3.pack(side=tk.LEFT)

                    Frame_numbers_2 = tk.Frame(
                        more_window, bg="white", bd=5, relief=tk.SUNKEN
                    )
                    Frame_numbers_2.place()
                    Frame_numbers_2.pack(side=tk.BOTTOM)

                    button_4 = tk.Button(
                        Frame_numbers_2,
                        text="4",
                        width=4,
                        height=2,
                        command=lambda: click_4("4"),
                    )
                    button_4.pack(side=tk.LEFT)

                    button_5 = tk.Button(
                        Frame_numbers_2,
                        text="5",
                        width=4,
                        height=2,
                        command=lambda: click_5("5"),
                    )
                    button_5.pack(side=tk.LEFT)

                    button_6 = tk.Button(
                        Frame_numbers_2,
                        text="6",
                        width=4,
                        height=2,
                        command=lambda: click_6("6"),
                    )
                    button_6.pack(side=tk.LEFT)

                    Frame_numbers_3 = tk.Frame(
                        more_window, bg="white", bd=5, relief=tk.SUNKEN
                    )
                    Frame_numbers_3.place()
                    Frame_numbers_3.pack(side=tk.BOTTOM)

                    button_7 = tk.Button(
                        Frame_numbers_3,
                        text="7",
                        width=4,
                        height=2,
                        command=lambda: click_7("7"),
                    )
                    button_7.pack(side=tk.LEFT)

                    button_8 = tk.Button(
                        Frame_numbers_3,
                        text="8",
                        width=4,
                        height=2,
                        command=lambda: click_8("8"),
                    )
                    button_8.pack(side=tk.LEFT)

                    button_9 = tk.Button(
                        Frame_numbers_3,
                        text="9",
                        width=4,
                        height=2,
                        command=lambda: click_9("9"),
                    )
                    button_9.pack(side=tk.LEFT)

                def on_click50(int):
                    D_E.delete(0, tk.END)
                    D_E.insert(0, 50)

                def on_click100(int):
                    D_E.delete(0, tk.END)
                    D_E.insert(0, 100)

                def on_click150(int):
                    D_E.delete(0, tk.END)
                    D_E.insert(0, 150)

                def on_click200(int):
                    D_E.delete(0, tk.END)
                    D_E.insert(0, 200)

                def on_click250(int):
                    D_E.delete(0, tk.END)
                    D_E.insert(0, 250)

                def on_click300(int):
                    D_E.delete(0, tk.END)
                    D_E.insert(0, 300)

                def on_click350(int):
                    D_E.delete(0, tk.END)
                    D_E.insert(0, 350)

                def Enter_D():
                    date = dt.datetime.now()
                    result = D_E.get()
                    list_1 = [
                        result,
                        CreditCardAmount + float(result),
                        f"{date:%d,%m,%Y}",
                        time.strftime("%H:%M:%S"),
                    ]
                    deposit_list.append(list_1)
                    print(list_1)

                    message_ = tk.Tk()
                    message_.resizable(False, False)
                    message_.geometry("750x300")

                    frame_message = tk.Frame(message_, bd=3, relief=tk.SUNKEN)
                    frame_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

                    message_label = tk.Label(
                        frame_message,
                        text="Operation is complete.\nThank you for using our ATM.",
                        font="Times 13",
                        padx=10,
                        pady=10,
                    )
                    message_label.place()
                    message_label.pack()

                def Cancle_():
                    D_E.delete(0, tk.END)

                D_L = tk.Label(
                    deposit_window,
                    text="Amount you would like to deposit :",
                    font="Time 11 bold",
                )
                D_L.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
                D_L.config(bg="#6b6e74")

                D_E = tk.Entry(deposit_window, width=10, font=("Arial", 30))
                D_E.place(x=260, y=135)

                frame_L_B = tk.Frame(deposit_window, bd=5, relief=tk.SUNKEN)
                frame_L_B.place()
                frame_L_B.pack(side=tk.LEFT)

                Enter_DB = tk.Button(
                    frame_L_B,
                    text="Enter",
                    width=20,
                    height=4,
                    command=Enter_D,
                )
                Enter_DB.place(x=0, y=230)
                Enter_DB.pack(side=tk.BOTTOM)

                DB_200 = tk.Button(
                    frame_L_B,
                    text="200",
                    width=20,
                    height=3,
                    command=lambda: on_click200("200"),
                )
                DB_200.place(x=0, y=180)
                DB_200.pack(side=tk.BOTTOM)

                DB_150 = tk.Button(
                    frame_L_B,
                    text="150",
                    width=20,
                    height=3,
                    command=lambda: on_click150("150"),
                )
                DB_150.place(x=0, y=130)
                DB_150.pack(side=tk.BOTTOM)

                DB_100 = tk.Button(
                    frame_L_B,
                    text="100",
                    width=20,
                    height=3,
                    command=lambda: on_click100("100"),
                )
                DB_100.place(x=0, y=80)
                DB_100.pack(side=tk.BOTTOM)

                DB_50 = tk.Button(
                    frame_L_B,
                    text="50",
                    width=20,
                    height=3,
                    command=lambda: on_click50("50"),
                )
                DB_50.place(x=0, y=30)
                DB_50.pack(side=tk.BOTTOM)

                frame_R_B = tk.Frame(deposit_window, bd=5, relief=tk.SUNKEN)
                frame_R_B.place()
                frame_R_B.pack(side=tk.RIGHT)

                DB_C = tk.Button(
                    frame_R_B,
                    text="Cancle",
                    width=20,
                    height=4,
                    command=Cancle_,
                )
                DB_C.place(x=550, y=230)
                DB_C.pack(side=tk.BOTTOM)

                DB_MORE = tk.Button(
                    frame_R_B, text="More", width=20, height=3, command=More_DB
                )
                DB_MORE.place(x=550, y=180)
                DB_MORE.pack(side=tk.BOTTOM)

                DB_350 = tk.Button(
                    frame_R_B,
                    text="350",
                    width=20,
                    height=3,
                    command=lambda: on_click350("350"),
                )
                DB_350.place(x=550, y=130)
                DB_350.pack(side=tk.BOTTOM)

                DB_300 = tk.Button(
                    frame_R_B,
                    text="300",
                    width=20,
                    height=3,
                    command=lambda: on_click300("300"),
                )
                DB_300.place(x=550, y=80)
                DB_300.pack(side=tk.BOTTOM)

                DB_250 = tk.Button(
                    frame_R_B,
                    text="250",
                    width=20,
                    height=3,
                    command=lambda: on_click250("250"),
                )
                DB_250.place(x=550, y=30)
                DB_250.pack(side=tk.BOTTOM)

            def Wintdrow_BB():

                windraw_window = tk.Tk()
                windraw_window.config(bg="#6b6e74")
                windraw_window.resizable(False, False)
                windraw_window.geometry("750x300")
                # new_window.destroy()

                def w_on_click50(int):
                    W_E.delete(0, tk.END)
                    W_E.insert(0, 50)

                def w_on_click100(int):
                    W_E.delete(0, tk.END)
                    W_E.insert(0, 100)

                def w_on_click150(int):
                    W_E.delete(0, tk.END)
                    W_E.insert(0, 150)

                def w_on_click200(int):
                    W_E.delete(0, tk.END)
                    W_E.insert(0, 200)

                def w_on_click250(int):
                    W_E.delete(0, tk.END)
                    W_E.insert(0, 250)

                def w_on_click300(int):
                    W_E.delete(0, tk.END)
                    W_E.insert(0, 300)

                def w_on_click350(int):
                    W_E.delete(0, tk.END)
                    W_E.insert(0, 350)

                def Cancle():
                    W_E.delete(0, tk.END)

                def Enter_b():

                    date = dt.datetime.now()
                    result = W_E.get()
                    list_1 = [
                        result,
                        CreditCardAmount - float(result),
                        f"{date:%d,%m,%Y}",
                        time.strftime("%H:%M:%S"),
                    ]
                    window_list.append(list_1)

                    NCA = CreditCardAmount - float(result)
                    print(NCA)
                    print(list_1)

                    if int(W_E) > CreditCardAmount:
                        message_ = tk.Tk()
                        message_.resizable(False, False)
                        message_.geometry("750x300")

                        frame_message = tk.Frame(message_, bd=3, relief=tk.SUNKEN)
                        frame_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

                        message_label = tk.Label(
                            frame_message,
                            text="Operation is not complete.\nNot enough amount.",
                            font="Times 13",
                            padx=10,
                            pady=10,
                        )
                        message_label.place()
                        message_label.pack()

                    message_ = tk.Tk()
                    message_.resizable(False, False)
                    message_.geometry("750x300")

                    frame_message = tk.Frame(message_, bd=3, relief=tk.SUNKEN)
                    frame_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

                    message_label = tk.Label(
                        frame_message,
                        text="Operation is complete.\nThank you for using our ATM.",
                        font="Times 13",
                        padx=10,
                        pady=10,
                    )
                    message_label.place()
                    message_label.pack()

                def More_B():

                    more_window = tk.Tk()
                    more_window.resizable(False, False)
                    more_window.geometry("750x300")
                    windraw_window.destroy()

                    def click_0(int):
                        more_entry.insert(tk.END, 0)

                    def click_1(int):
                        more_entry.insert(tk.END, 1)

                    def click_2(int):
                        more_entry.insert(tk.END, 2)

                    def click_3(int):
                        more_entry.insert(tk.END, 3)

                    def click_4(int):
                        more_entry.insert(tk.END, 4)

                    def click_5(int):
                        more_entry.insert(tk.END, 5)

                    def click_6(int):
                        more_entry.insert(tk.END, 6)

                    def click_7(int):
                        more_entry.insert(tk.END, 7)

                    def click_8(int):
                        more_entry.insert(tk.END, 8)

                    def click_9(int):
                        more_entry.insert(tk.END, 9)

                    def click_C():
                        more_entry.delete(0, tk.END)

                    def click_Done():

                        date = dt.datetime.now()
                        result = more_entry.get()
                        list_ = [
                            result,
                            CreditCardAmount - float(result),
                            f"{date:%d,%m,%Y}",
                            time.strftime("%H:%M:%S"),
                        ]
                        window_list.append(list_)

                        print(list_)

                        message_ = tk.Tk()
                        message_.resizable(False, False)
                        message_.geometry("750x300")

                        frame_message = tk.Frame(message_, bd=3, relief=tk.SUNKEN)
                        frame_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

                        message_label = tk.Label(
                            frame_message,
                            text="Operation is complete.\nThank you for using our ATM.",
                            font="Times 13",
                            padx=10,
                            pady=10,
                        )
                        message_label.place()
                        message_label.pack()

                    Frame_entry = tk.Frame(
                        more_window, bd=5, relief=tk.SUNKEN, height=30
                    )
                    Frame_entry.place()
                    Frame_entry.pack(side=tk.TOP)

                    more_entry = tk.Entry(more_window, width=10, font=("Arial", 25))
                    more_entry.place()
                    more_entry.pack(side=tk.TOP)
                    # frame
                    Frame_numbers_0 = tk.Frame(
                        more_window, bg="white", bd=5, relief=tk.SUNKEN
                    )
                    Frame_numbers_0.place()
                    Frame_numbers_0.pack(side=tk.BOTTOM)

                    button_C = tk.Button(
                        Frame_numbers_0, text="C", width=4, height=2, command=click_C
                    )
                    button_C.pack(side=tk.LEFT)

                    button_0 = tk.Button(
                        Frame_numbers_0,
                        text="0",
                        width=4,
                        height=2,
                        command=lambda: click_0("0"),
                    )
                    button_0.pack(side=tk.LEFT)

                    button_Done = tk.Button(
                        Frame_numbers_0,
                        text="Done",
                        width=4,
                        height=2,
                        command=click_Done,
                    )
                    button_Done.pack(side=tk.RIGHT)
                    # frame
                    Frame_numbers = tk.Frame(
                        more_window, bg="white", bd=5, relief=tk.SUNKEN
                    )
                    Frame_numbers.place()
                    Frame_numbers.pack(side=tk.BOTTOM)

                    button_1 = tk.Button(
                        Frame_numbers,
                        text="1",
                        width=4,
                        height=2,
                        command=lambda: click_1("1"),
                    )
                    button_1.pack(side=tk.LEFT)

                    button_2 = tk.Button(
                        Frame_numbers,
                        text="2",
                        width=4,
                        height=2,
                        command=lambda: click_2("2"),
                    )
                    button_2.pack(side=tk.LEFT)

                    button_3 = tk.Button(
                        Frame_numbers,
                        text="3",
                        width=4,
                        height=2,
                        command=lambda: click_3("3"),
                    )
                    button_3.pack(side=tk.LEFT)

                    Frame_numbers_2 = tk.Frame(
                        more_window, bg="white", bd=5, relief=tk.SUNKEN
                    )
                    Frame_numbers_2.place()
                    Frame_numbers_2.pack(side=tk.BOTTOM)

                    button_4 = tk.Button(
                        Frame_numbers_2,
                        text="4",
                        width=4,
                        height=2,
                        command=lambda: click_4("4"),
                    )
                    button_4.pack(side=tk.LEFT)

                    button_5 = tk.Button(
                        Frame_numbers_2,
                        text="5",
                        width=4,
                        height=2,
                        command=lambda: click_5("5"),
                    )
                    button_5.pack(side=tk.LEFT)

                    button_6 = tk.Button(
                        Frame_numbers_2,
                        text="6",
                        width=4,
                        height=2,
                        command=lambda: click_6("6"),
                    )
                    button_6.pack(side=tk.LEFT)

                    Frame_numbers_3 = tk.Frame(
                        more_window, bg="white", bd=5, relief=tk.SUNKEN
                    )
                    Frame_numbers_3.place()
                    Frame_numbers_3.pack(side=tk.BOTTOM)

                    button_7 = tk.Button(
                        Frame_numbers_3,
                        text="7",
                        width=4,
                        height=2,
                        command=lambda: click_7("7"),
                    )
                    button_7.pack(side=tk.LEFT)

                    button_8 = tk.Button(
                        Frame_numbers_3,
                        text="8",
                        width=4,
                        height=2,
                        command=lambda: click_8("8"),
                    )
                    button_8.pack(side=tk.LEFT)

                    button_9 = tk.Button(
                        Frame_numbers_3,
                        text="9",
                        width=4,
                        height=2,
                        command=lambda: click_9("9"),
                    )
                    button_9.pack(side=tk.LEFT)

                W_L = tk.Label(
                    windraw_window,
                    text="Amount you would like to draw :",
                    font="Time 11 bold",
                )
                W_L.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
                W_L.config(bg="#6b6e74")

                W_E = tk.Entry(windraw_window, width=10, font=("Arial", 30))
                W_E.place(x=260, y=135)

                Frame_L_WB = tk.Frame(windraw_window, bd=5, relief=tk.SUNKEN)
                Frame_L_WB.place()
                Frame_L_WB.pack(side=tk.LEFT)

                WB_Enter = tk.Button(
                    Frame_L_WB,
                    text="Enter",
                    width=20,
                    height=4,
                    command=Enter_b,
                )
                WB_Enter.place(x=0, y=230)
                WB_Enter.pack(side=tk.BOTTOM)

                WB_200 = tk.Button(
                    Frame_L_WB,
                    text="200",
                    command=lambda: w_on_click200("200"),
                    width=20,
                    height=3,
                )
                WB_200.place(x=0, y=180)
                WB_200.pack(side=tk.BOTTOM)

                WB_150 = tk.Button(
                    Frame_L_WB,
                    text="150",
                    command=lambda: w_on_click150("150"),
                    width=20,
                    height=3,
                )
                WB_150.place(x=0, y=130)
                WB_150.pack(side=tk.BOTTOM)

                WB_100 = tk.Button(
                    Frame_L_WB,
                    text="100",
                    command=lambda: w_on_click100("100"),
                    width=20,
                    height=3,
                )
                WB_100.place(x=0, y=80)
                WB_100.pack(side=tk.BOTTOM)

                WB_50 = tk.Button(
                    Frame_L_WB,
                    text="50",
                    command=lambda: w_on_click50("50"),
                    width=20,
                    height=3,
                )
                WB_50.place(x=0, y=30)
                WB_50.pack(side=tk.BOTTOM)

                # Frame for the Right Buttons does not working ?! WHY

                frame_R_WB = tk.Frame(windraw_window, bd=5, relief=tk.SUNKEN)
                frame_R_WB.place()
                frame_R_WB.pack(side=tk.RIGHT)

                WB_C = tk.Button(
                    frame_R_WB, text="Cancle", width=20, height=4, command=Cancle
                )
                WB_C.place(x=550, y=230)
                WB_C.pack(side=tk.BOTTOM)

                WB_MORE = tk.Button(
                    frame_R_WB, text="More", width=20, height=3, command=More_B
                )
                WB_MORE.place(x=550, y=180)
                WB_MORE.pack(side=tk.BOTTOM)

                WB_350 = tk.Button(
                    frame_R_WB,
                    text="350",
                    width=20,
                    height=3,
                    command=lambda: w_on_click350("350"),
                )
                WB_350.place(x=550, y=130)
                WB_350.pack(side=tk.BOTTOM)

                WB_300 = tk.Button(
                    frame_R_WB,
                    text="300",
                    width=20,
                    height=3,
                    command=lambda: w_on_click300("300"),
                )
                WB_300.place(x=550, y=80)
                WB_300.pack(side=tk.BOTTOM)

                WB_250 = tk.Button(
                    frame_R_WB,
                    text="250",
                    width=20,
                    height=3,
                    command=lambda: w_on_click250("250"),
                )
                WB_250.place(x=550, y=30)
                WB_250.pack(side=tk.BOTTOM)

            frame = tk.Frame(
                new_window, bg="white", bd=2, relief=tk.SUNKEN, padx=10, pady=40
            )
            frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

            greet = tk.Label(
                frame,
                text="Welcome to you Credit account!\n You have: "
                + str(CreditCardAmount),
                bg="white",
                font="Times",
            )
            greet.place()
            greet.pack()

            def Cancel():
                new_window.destroy()

            # FRAME
            frame_LB = tk.Frame(new_window, bd=3, relief=tk.SUNKEN)
            frame_LB.place()
            frame_LB.pack(side=tk.LEFT)

            C_B = tk.Button(frame_LB, text="Cancle", command=Cancel, width=30, height=4)
            C_B.place()
            C_B.pack(side=tk.BOTTOM)

            D_B = tk.Button(
                frame_LB, text="Deposit", command=Deposit_BB, width=30, height=3
            )
            D_B.place()
            D_B.pack(side=tk.BOTTOM)

            W_B = tk.Button(
                frame_LB, text="Windraw", command=Wintdrow_BB, width=30, height=3
            )
            W_B.place()
            W_B.pack(side=tk.BOTTOM)

            frame_RB = tk.Frame(new_window, bd=3, relief=tk.SUNKEN)
            frame_RB.place()
            frame_RB.pack(side=tk.RIGHT)

            WH_B = tk.Button(
                frame_RB,
                text="Windraw History",
                command=Windraw_History,
                width=30,
                height=4,
            )

            WH_B.place()
            WH_B.pack(side=tk.BOTTOM)

            TH_B = tk.Button(
                frame_RB,
                text="Transfer History",
                command=Transfer_B,
                width=30,
                height=3,
            )
            TH_B.place()
            TH_B.pack(side=tk.BOTTOM)

            DH_B = tk.Button(
                frame_RB,
                text="Deposit History",
                command=Deposit_History,
                width=30,
                height=3,
            )
            DH_B.place()
            DH_B.pack(side=tk.BOTTOM)

        else:
            window.destroy()
    elif e_c == 2:
        if e_p == 2:
            new_debit_window = tk.Tk()
            new_debit_window.config(bg="#6b6e74")
            new_debit_window.resizable(False, False)
            new_debit_window.geometry("750x300")
            # window.destroy()

            def deposit_history_B():
                deposit_history_2 = tk.Tk()
                deposit_history_2.config(bg="#6b6e74")
                deposit_history_2.resizable(False, False)
                deposit_history_2.geometry("750x300")

                frame_wind = tk.Frame(
                    deposit_history_2,
                    bg="white",
                    bd=5,
                    padx=10,
                    pady=10,
                    relief=tk.SUNKEN,
                )
                frame_wind.place()
                frame_wind.pack()

                list_draw = tk.Listbox(frame_wind, width=30)
                list_draw.insert(1, *debit_deposit)
                list_draw.pack()

            def windraw_history_B():
                windraw_history_2 = tk.Tk()
                windraw_history_2.config(bg="#6b6e74")
                windraw_history_2.resizable(False, False)
                windraw_history_2.geometry("750x300")

                frame_wind = tk.Frame(
                    windraw_history_2,
                    bg="white",
                    bd=5,
                    padx=10,
                    pady=10,
                    relief=tk.SUNKEN,
                )
                frame_wind.place()
                frame_wind.pack()

                list_draw = tk.Listbox(frame_wind, width=30)
                list_draw.insert(1, *draw_deposit)
                list_draw.pack()

            def windraw_button():
                new_windraw_window = tk.Tk()
                new_windraw_window.config(bg="#6b6e74")
                new_windraw_window.resizable(False, False)
                new_windraw_window.geometry("750x300")
                # new_debit_window.destroy()

                def click_Enter():
                    date = dt.datetime.now()
                    result = Entry_windraw.get()
                    list_1 = [
                        result,
                        DebitCardAmount - float(result),
                        f"{date:%d,%m,%Y}",
                        time.strftime("%H:%M:%S"),
                    ]
                    draw_deposit.append(list_1)
                    NCA = DebitCardAmount - float(result)
                    print(NCA)
                    print(list_1)

                    message_ = tk.Tk()
                    message_.resizable(False, False)
                    message_.geometry("750x300")

                    frame_message = tk.Frame(message_, bd=3, relief=tk.SUNKEN)
                    frame_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

                    message_label = tk.Label(
                        frame_message,
                        text="Operation is complete.\nThank you for using our ATM.",
                        font="Times 13",
                        padx=10,
                        pady=10,
                    )
                    message_label.place()
                    message_label.pack()

                def click_50(int):
                    Entry_windraw.delete(0, tk.END)
                    Entry_windraw.insert(0, 50)

                def click_100(int):
                    Entry_windraw.delete(0, tk.END)
                    Entry_windraw.insert(0, 100)

                def click_150(int):
                    Entry_windraw.delete(0, tk.END)
                    Entry_windraw.insert(0, 150)

                def click_200(int):
                    Entry_windraw.delete(0, tk.END)
                    Entry_windraw.insert(0, 200)

                def click_250(int):
                    Entry_windraw.delete(0, tk.END)
                    Entry_windraw.insert(0, 250)

                def click_300(int):
                    Entry_windraw.delete(0, tk.END)
                    Entry_windraw.insert(0, 300)

                def click_350(int):
                    Entry_windraw.delete(0, tk.END)
                    Entry_windraw.insert(0, 350)

                def click_more():
                    more_draw = tk.Tk()
                    more_draw.config(bg="#6b6e74")
                    more_draw.resizable(False, False)
                    more_draw.geometry("750x300")

                    def click_on_done():
                        date = dt.datetime.now()
                        result = more_draw_entry.get()
                        list_ = [
                            result,
                            DebitCardAmount - float(result),
                            f"{date:%d,%m,%Y}",
                            time.strftime("%H:%M:%S"),
                        ]
                        draw_deposit.append(list_)
                        print(list_)

                        message_ = tk.Tk()
                        message_.resizable(False, False)
                        message_.geometry("750x300")

                        frame_message = tk.Frame(message_, bd=3, relief=tk.SUNKEN)
                        frame_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

                        message_label = tk.Label(
                            frame_message,
                            text="Operation is complete.\nThank you for using our ATM.",
                            font="Times 13",
                            padx=10,
                            pady=10,
                        )
                        message_label.place()
                        message_label.pack()

                    def click_on0(int):
                        more_draw_entry.insert(tk.END, 0)

                    def click_on1(int):
                        more_draw_entry.insert(tk.END, 1)

                    def click_on2(int):
                        more_draw_entry.insert(tk.END, 2)

                    def click_on3(int):
                        more_draw_entry.insert(tk.END, 3)

                    def click_on4(int):
                        more_draw_entry.insert(tk.END, 4)

                    def click_on5(int):
                        more_draw_entry.insert(tk.END, 5)

                    def click_on6(int):
                        more_draw_entry.insert(tk.END, 6)

                    def click_on7(int):
                        more_draw_entry.insert(tk.END, 7)

                    def click_on8(int):
                        more_draw_entry.insert(tk.END, 8)

                    def click_on9(int):
                        more_draw_entry.insert(tk.END, 9)

                    def click_onC():
                        more_draw_entry.delete(0, tk.END)

                    # FRAME
                    frame_entry = tk.Frame(more_draw, bd=3, relief=tk.SUNKEN)
                    frame_entry.place()
                    frame_entry.pack(side=tk.TOP)

                    more_draw_entry = tk.Entry(frame_entry, width=13, font="Times 13")
                    more_draw_entry.place()
                    more_draw_entry.pack(side=tk.BOTTOM)

                    frame_0 = tk.Frame(more_draw, bd=3, relief=tk.SUNKEN)
                    frame_0.place()
                    frame_0.pack(side=tk.BOTTOM)

                    button_c_draw = tk.Button(
                        frame_0, width=4, height=2, text="C", command=click_onC
                    )
                    button_c_draw.place()
                    button_c_draw.pack(side=tk.LEFT)

                    button_0_draw = tk.Button(
                        frame_0,
                        width=4,
                        height=2,
                        text="0",
                        command=lambda: click_on0("0"),
                    )
                    button_0_draw.place()
                    button_0_draw.pack(side=tk.LEFT)

                    button_done_draw = tk.Button(
                        frame_0,
                        width=4,
                        height=2,
                        text="Done",
                        command=click_on_done,
                    )
                    button_done_draw.place()
                    button_done_draw.pack(side=tk.LEFT)
                    # FRAME      !!! Not Finished
                    frame_1_draw = tk.Frame(more_draw, bd=3, relief=tk.SUNKEN)
                    frame_1_draw.place()
                    frame_1_draw.pack(side=tk.BOTTOM)

                    button_1_draw = tk.Button(
                        frame_1_draw,
                        width=4,
                        height=2,
                        text="1",
                        command=lambda: click_on1("1"),
                    )
                    button_1_draw.place()
                    button_1_draw.pack(side=tk.LEFT)

                    button_2_draw = tk.Button(
                        frame_1_draw,
                        width=4,
                        height=2,
                        text="2",
                        command=lambda: click_on2("2"),
                    )
                    button_2_draw.place()
                    button_2_draw.pack(side=tk.LEFT)

                    button_3_draw = tk.Button(
                        frame_1_draw,
                        width=4,
                        height=2,
                        text="3",
                        command=lambda: click_on3("3"),
                    )
                    button_3_draw.place()
                    button_3_draw.pack(side=tk.LEFT)
                    # FRAME
                    frame_2_draw = tk.Frame(more_draw, bd=3, relief=tk.SUNKEN)
                    frame_2_draw.place()
                    frame_2_draw.pack(side=tk.BOTTOM)

                    button_4_draw = tk.Button(
                        frame_2_draw,
                        width=4,
                        height=2,
                        text="4",
                        command=lambda: click_on4("4"),
                    )
                    button_4_draw.place()
                    button_4_draw.pack(side=tk.LEFT)

                    button_5_draw = tk.Button(
                        frame_2_draw,
                        width=4,
                        height=2,
                        text="5",
                        command=lambda: click_on5("5"),
                    )
                    button_5_draw.place()
                    button_5_draw.pack(side=tk.LEFT)

                    button_6_draw = tk.Button(
                        frame_2_draw,
                        width=4,
                        height=2,
                        text="6",
                        command=lambda: click_on6("6"),
                    )
                    button_6_draw.place()
                    button_6_draw.pack(side=tk.LEFT)
                    # FRAME
                    frame_3_draw = tk.Frame(more_draw, bd=3, relief=tk.SUNKEN)
                    frame_3_draw.place()
                    frame_3_draw.pack(side=tk.BOTTOM)

                    button_7_draw = tk.Button(
                        frame_3_draw,
                        width=4,
                        height=2,
                        text="7",
                        command=lambda: click_on7("7"),
                    )
                    button_7_draw.place()
                    button_7_draw.pack(side=tk.LEFT)

                    button_8_draw = tk.Button(
                        frame_3_draw,
                        width=4,
                        height=2,
                        text="8",
                        command=lambda: click_on8("8"),
                    )
                    button_8_draw.place()
                    button_8_draw.pack(side=tk.LEFT)

                    button_9_draw = tk.Button(
                        frame_3_draw,
                        width=4,
                        height=2,
                        text="9",
                        command=lambda: click_on9("9"),
                    )
                    button_9_draw.place()
                    button_9_draw.pack(side=tk.LEFT)

                Label_windraw = tk.Label(
                    new_windraw_window,
                    text="Amount you want to draw :",
                    font="Time 11 bold",
                )
                Label_windraw.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
                Label_windraw.config(bg="#6b6e74")

                Entry_windraw = tk.Entry(
                    new_windraw_window, width=10, font=("Arial", 30)
                )
                Entry_windraw.place(x=260, y=135)

                frame_l_b = tk.Frame(new_windraw_window, bd=3, relief=tk.SUNKEN)
                frame_l_b.place()
                frame_l_b.pack(side=tk.LEFT)

                frame_l_b = tk.Frame(new_windraw_window, bd=3, relief=tk.SUNKEN)
                frame_l_b.place()
                frame_l_b.pack(side=tk.LEFT)

                button_enter = tk.Button(
                    frame_l_b,
                    text="Enter",
                    width=20,
                    height=3,
                    command=click_Enter,
                )
                button_enter.place()
                button_enter.pack(side=tk.BOTTOM)

                button_200 = tk.Button(
                    frame_l_b,
                    text="200",
                    width=20,
                    height=3,
                    command=lambda: click_200("200"),
                )
                button_200.place()
                button_200.pack(side=tk.BOTTOM)

                button_150 = tk.Button(
                    frame_l_b,
                    text="150",
                    width=20,
                    height=3,
                    command=lambda: click_150("150"),
                )
                button_150.place()
                button_150.pack(side=tk.BOTTOM)

                button_100 = tk.Button(
                    frame_l_b,
                    text="100",
                    width=20,
                    height=3,
                    command=lambda: click_100("100"),
                )
                button_100.place()
                button_100.pack(side=tk.BOTTOM)

                button_50 = tk.Button(
                    frame_l_b,
                    text="50",
                    width=20,
                    height=3,
                    command=lambda: click_50("50"),
                )
                button_50.place()
                button_50.pack(side=tk.BOTTOM)

                frame_r_b = tk.Frame(new_windraw_window, bd=3, relief=tk.SUNKEN)
                frame_r_b.place()
                frame_r_b.pack(side=tk.RIGHT)

                button_cancel = tk.Button(frame_r_b, text="Cancel", width=20, height=3)
                button_cancel.place()
                button_cancel.pack(side=tk.BOTTOM)

                button_more = tk.Button(
                    frame_r_b,
                    text="More",
                    width=20,
                    height=3,
                    command=click_more,
                )
                button_more.place()
                button_more.pack(side=tk.BOTTOM)

                button_350 = tk.Button(
                    frame_r_b,
                    text="350",
                    width=20,
                    height=3,
                    command=lambda: click_350("350"),
                )
                button_350.place()
                button_350.pack(side=tk.BOTTOM)

                button_300 = tk.Button(
                    frame_r_b,
                    text="300",
                    width=20,
                    height=3,
                    command=lambda: click_300("300"),
                )
                button_300.place()
                button_300.pack(side=tk.BOTTOM)

                button_250 = tk.Button(
                    frame_r_b,
                    text="250",
                    width=20,
                    height=3,
                    command=lambda: click_250("250"),
                )
                button_250.place()
                button_250.pack(side=tk.BOTTOM)

            def deposit_button():
                new_deposit_window = tk.Tk()
                new_deposit_window.config(bg="#6b6e74")
                new_deposit_window.resizable(False, False)
                new_deposit_window.geometry("750x300")
                # new_debit_window.destroy()

                def click_50(int):
                    Entry_deposit.delete(0, tk.END)
                    Entry_deposit.insert(0, 50)

                def click_100(int):
                    Entry_deposit.delete(0, tk.END)
                    Entry_deposit.insert(0, 100)

                def click_150(int):
                    Entry_deposit.delete(0, tk.END)
                    Entry_deposit.insert(0, 150)

                def click_200(int):
                    Entry_deposit.delete(0, tk.END)
                    Entry_deposit.insert(0, 200)

                def click_250(int):
                    Entry_deposit.delete(0, tk.END)
                    Entry_deposit.insert(0, 250)

                def click_300(int):
                    Entry_deposit.delete(0, tk.END)
                    Entry_deposit.insert(0, 300)

                def click_350(int):
                    Entry_deposit.delete(0, tk.END)
                    Entry_deposit.insert(0, 350)

                def click_More():
                    more_deposit_window = tk.Tk()
                    more_deposit_window.config(bg="#6b6e74")
                    more_deposit_window.resizable(False, False)
                    more_deposit_window.geometry("750x300")
                    # FRAME

                    def click_on_0(int):
                        more_deposit_entry.insert(tk.END, 0)

                    def click_on_1(int):
                        more_deposit_entry.insert(tk.END, 1)

                    def click_on_2(int):
                        more_deposit_entry.insert(tk.END, 2)

                    def click_on_3(int):
                        more_deposit_entry.insert(tk.END, 3)

                    def click_on_4(int):
                        more_deposit_entry.insert(tk.END, 4)

                    def click_on_5(int):
                        more_deposit_entry.insert(tk.END, 5)

                    def click_on_6(int):
                        more_deposit_entry.insert(tk.END, 6)

                    def click_on_7(int):
                        more_deposit_entry.insert(tk.END, 7)

                    def click_on_8(int):
                        more_deposit_entry.insert(tk.END, 8)

                    def click_on_9(int):
                        more_deposit_entry.insert(tk.END, 9)

                    def click_on_C():
                        more_deposit_entry.delete(0, tk.END)

                    def click_on_Done():
                        date = dt.datetime.now()
                        result = more_deposit_entry.get()
                        list_ = [
                            result,
                            DebitCardAmount + float(result),
                            f"{date:%d,%m,%Y}",
                            time.strftime("%H:%M:%S"),
                        ]
                        debit_deposit.append(list_)
                        print(list_)

                        message_ = tk.Tk()
                        message_.resizable(False, False)
                        message_.geometry("750x300")

                        frame_message = tk.Frame(message_, bd=3, relief=tk.SUNKEN)
                        frame_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

                        message_label = tk.Label(
                            frame_message,
                            text="Operation is complete.\nThank you for using our ATM.",
                            font="Times 13",
                            padx=10,
                            pady=10,
                        )
                        message_label.place()
                        message_label.pack()

                    frame_deposit_entry = tk.Frame(
                        more_deposit_window, bd=5, relief=tk.SUNKEN
                    )
                    frame_deposit_entry.place()
                    frame_deposit_entry.pack(side=tk.TOP)

                    more_deposit_entry = tk.Entry(
                        more_deposit_window, width=13, font="Times 13"
                    )
                    more_deposit_entry.place()
                    more_deposit_entry.pack(side=tk.TOP)

                    frame_deposit_ = tk.Frame(
                        more_deposit_window, bd=5, relief=tk.SUNKEN
                    )
                    frame_deposit_.place()
                    frame_deposit_.pack(side=tk.BOTTOM)

                    button_c_deposit = tk.Button(
                        frame_deposit_,
                        width=4,
                        height=2,
                        text="C",
                        command=lambda: click_on_C("C"),
                    )
                    button_c_deposit.place()
                    button_c_deposit.pack(side=tk.LEFT)

                    button_0_deposit = tk.Button(
                        frame_deposit_,
                        width=4,
                        height=2,
                        text="0",
                        command=lambda: click_on_0("0"),
                    )
                    button_0_deposit.place()
                    button_0_deposit.pack(side=tk.LEFT)

                    button_Done_deposit = tk.Button(
                        frame_deposit_,
                        width=4,
                        height=2,
                        text="Done",
                        command=click_on_Done,
                    )
                    button_Done_deposit.place()
                    button_Done_deposit.pack(side=tk.LEFT)
                    # FRAME
                    frame_deposit_1 = tk.Frame(
                        more_deposit_window, bd=5, relief=tk.SUNKEN
                    )
                    frame_deposit_1.place()
                    frame_deposit_1.pack(side=tk.BOTTOM)

                    button_1_deposit = tk.Button(
                        frame_deposit_1,
                        width=4,
                        height=2,
                        text="1",
                        command=lambda: click_on_1("1"),
                    )
                    button_1_deposit.place()
                    button_1_deposit.pack(side=tk.LEFT)

                    button_2_deposit = tk.Button(
                        frame_deposit_1,
                        width=4,
                        height=2,
                        text="2",
                        command=lambda: click_on_2("2"),
                    )
                    button_2_deposit.place()
                    button_2_deposit.pack(side=tk.LEFT)

                    button_3_deposit = tk.Button(
                        frame_deposit_1,
                        width=4,
                        height=2,
                        text="3",
                        command=lambda: click_on_3("3"),
                    )
                    button_3_deposit.place()
                    button_3_deposit.pack(side=tk.LEFT)

                    frame_deposit_2 = tk.Frame(
                        more_deposit_window, bd=5, relief=tk.SUNKEN
                    )
                    frame_deposit_2.place()
                    frame_deposit_2.pack(side=tk.BOTTOM)

                    button_4_deposit = tk.Button(
                        frame_deposit_2,
                        width=4,
                        height=2,
                        text="4",
                        command=lambda: click_on_4("4"),
                    )
                    button_4_deposit.place()
                    button_4_deposit.pack(side=tk.LEFT)

                    button_5_deposit = tk.Button(
                        frame_deposit_2,
                        width=4,
                        height=2,
                        text="5",
                        command=lambda: click_on_5("5"),
                    )
                    button_5_deposit.place()
                    button_5_deposit.pack(side=tk.LEFT)

                    button_6_deposit = tk.Button(
                        frame_deposit_2,
                        width=4,
                        height=2,
                        text="6",
                        command=lambda: click_on_6("6"),
                    )
                    button_6_deposit.place()
                    button_6_deposit.pack(side=tk.LEFT)

                    frame_deposit_3 = tk.Frame(
                        more_deposit_window, bd=5, relief=tk.SUNKEN
                    )
                    frame_deposit_3.place()
                    frame_deposit_3.pack(side=tk.BOTTOM)

                    button_7_deposit = tk.Button(
                        frame_deposit_3,
                        width=4,
                        height=2,
                        text="7",
                        command=lambda: click_on_7("7"),
                    )
                    button_7_deposit.place()
                    button_7_deposit.pack(side=tk.LEFT)

                    button_8_deposit = tk.Button(
                        frame_deposit_3,
                        width=4,
                        height=2,
                        text="8",
                        command=lambda: click_on_8("8"),
                    )
                    button_8_deposit.place()
                    button_8_deposit.pack(side=tk.LEFT)

                    button_9_deposit = tk.Button(
                        frame_deposit_3,
                        width=4,
                        height=2,
                        text="9",
                        command=lambda: click_on_9("9"),
                    )
                    button_9_deposit.place()
                    button_9_deposit.pack(side=tk.LEFT)

                def click_Enter():
                    date = dt.datetime.now()
                    result = Entry_deposit.get()
                    list_1 = [
                        result,
                        DebitCardAmount + float(result),
                        f"{date:%d,%m,%Y}",
                        time.strftime("%H:%M:%S"),
                    ]
                    debit_deposit.append(list_1)
                    NCA = DebitCardAmount + float(result)
                    print(NCA)
                    print(list_1)

                    message_ = tk.Tk()
                    message_.resizable(False, False)
                    message_.geometry("750x300")

                    frame_message = tk.Frame(message_, bd=3, relief=tk.SUNKEN)
                    frame_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

                    message_label = tk.Label(
                        frame_message,
                        text="Operation is complete.\nThank you for using our ATM.",
                        font="Times 13",
                        padx=10,
                        pady=10,
                    )
                    message_label.place()
                    message_label.pack()

                Label_deposit = tk.Label(
                    new_deposit_window,
                    text="Amount you want to deposit :",
                    font="Time 11 bold",
                )
                Label_deposit.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
                Label_deposit.config(bg="#6b6e74")

                Entry_deposit = tk.Entry(
                    new_deposit_window, width=10, font=("Arial", 30)
                )
                Entry_deposit.place(x=260, y=135)

                frame_l_b = tk.Frame(new_deposit_window, bd=3, relief=tk.SUNKEN)
                frame_l_b.place()
                frame_l_b.pack(side=tk.LEFT)

                button_enter = tk.Button(
                    frame_l_b,
                    text="Enter",
                    width=20,
                    height=3,
                    command=click_Enter,
                )
                button_enter.place()
                button_enter.pack(side=tk.BOTTOM)

                button_200 = tk.Button(
                    frame_l_b,
                    text="200",
                    width=20,
                    height=3,
                    command=lambda: click_200("200"),
                )
                button_200.place()
                button_200.pack(side=tk.BOTTOM)

                button_150 = tk.Button(
                    frame_l_b,
                    text="150",
                    width=20,
                    height=3,
                    command=lambda: click_150("150"),
                )
                button_150.place()
                button_150.pack(side=tk.BOTTOM)

                button_100 = tk.Button(
                    frame_l_b,
                    text="100",
                    width=20,
                    height=3,
                    command=lambda: click_100("100"),
                )
                button_100.place()
                button_100.pack(side=tk.BOTTOM)

                button_50 = tk.Button(
                    frame_l_b,
                    text="50",
                    width=20,
                    height=3,
                    command=lambda: click_50("50"),
                )
                button_50.place()
                button_50.pack(side=tk.BOTTOM)

                frame_r_b = tk.Frame(new_deposit_window, bd=3, relief=tk.SUNKEN)
                frame_r_b.place()
                frame_r_b.pack(side=tk.RIGHT)

                button_cancel = tk.Button(frame_r_b, text="Cancel", width=20, height=3)
                button_cancel.place()
                button_cancel.pack(side=tk.BOTTOM)

                button_more = tk.Button(
                    frame_r_b, text="More", width=20, height=3, command=click_More
                )
                button_more.place()
                button_more.pack(side=tk.BOTTOM)

                button_350 = tk.Button(
                    frame_r_b,
                    text="350",
                    width=20,
                    height=3,
                    command=lambda: click_350("350"),
                )
                button_350.place()
                button_350.pack(side=tk.BOTTOM)

                button_300 = tk.Button(
                    frame_r_b,
                    text="300",
                    width=20,
                    height=3,
                    command=lambda: click_300("300"),
                )
                button_300.place()
                button_300.pack(side=tk.BOTTOM)

                button_250 = tk.Button(
                    frame_r_b,
                    text="250",
                    width=20,
                    height=3,
                    command=lambda: click_250("250"),
                )
                button_250.place()
                button_250.pack(side=tk.BOTTOM)

            def cancle_button():
                pass

            # def

            frame = tk.Frame(
                new_debit_window, bg="white", bd=3, relief=tk.SUNKEN, padx=10, pady=40
            )
            frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

            greet = tk.Label(
                frame,
                text="Welcome to you Debit account!\n You have: "
                + str(DebitCardAmount),
                bg="white",
                font="Times",
            )
            greet.place()
            greet.pack()

            frame_2LB = tk.Frame(new_debit_window, bd=3, relief=tk.SUNKEN)
            frame_2LB.place()
            frame_2LB.pack(side=tk.LEFT)

            C_C_B = tk.Button(frame_2LB, text="Cancle", command="", width=30, height=4)
            C_C_B.place()
            C_C_B.pack(side=tk.BOTTOM)

            C_D_B = tk.Button(
                frame_2LB, text="Deposit", command=deposit_button, width=30, height=3
            )
            C_D_B.place()
            C_D_B.pack(side=tk.BOTTOM)

            C_W_B = tk.Button(
                frame_2LB, text="Windraw", width=30, height=3, command=windraw_button
            )

            C_W_B.place()
            C_W_B.pack(side=tk.BOTTOM)

            frame_2RB = tk.Frame(new_debit_window, bd=3, relief=tk.SUNKEN)
            frame_2RB.place()
            frame_2RB.pack(side=tk.RIGHT)

            C_TH_B = tk.Button(
                frame_2RB, text="Transfer History", command="", width=30, height=4
            )
            C_TH_B.place()
            C_TH_B.pack(side=tk.BOTTOM)

            C_DH_B = tk.Button(
                frame_2RB,
                text="Deposit History",
                command=deposit_history_B,
                width=30,
                height=3,
            )
            C_DH_B.place()
            C_DH_B.pack(side=tk.BOTTOM)

            C_WH_B = tk.Button(
                frame_2RB,
                text="Windraw History",
                command=windraw_history_B,
                width=30,
                height=3,
            )
            C_WH_B.place()
            C_WH_B.pack(side=tk.BOTTOM)

        else:
            window.destroy()
    else:
        window.destroy()


def Exit():
    window.destroy()


window = tk.Tk()
window.resizable(False, False)
window.geometry("300x300")

l_EnterCard = tk.Label(window, text=" Enter Card 1/2 : \n [1.Debit 2.Credit]")
l_EnterCard.place(x=0, y=100)
e_EnterCard = tk.Entry(window, width=15, font="time 13")
e_EnterCard.place(x=140, y=100)

l_PIN = tk.Label(window, text="PIN :")
l_PIN.place(x=00, y=150)

e_EnterPIN = tk.Entry(window, width=15, show="*", font="time 13")
e_EnterPIN.place(x=140, y=150)

B1 = tk.Button(window, text="Enter", command=pin_id, width=30)
B1.place(x=40, y=220)

B2 = tk.Button(window, text="Exit", command=Exit, width=30)
B2.place(x=40, y=260)


window.mainloop()
