from tkinter import *
import tkinter as tk
import math

LENGHT = 800
WIDTH = 700


def SUM():  # расчитывает на 96% верно
    new_window = tk.Toplevel(frame)
    new_window.title("Расчёт Конечной Суммы")

    title = Label(new_window, text="Расчёт конечной суммы\n Период реинвестирования - раз в год").pack()

    label1 = Label(new_window, text="Стартовый капитал(руб):").pack()
    label1_entry = tk.Entry(new_window)
    label1_entry.pack()

    label2 = tk.Label(new_window, text="Срок инвестирования(лет):").pack()
    label2_entry = tk.Entry(new_window)
    label2_entry.pack()

    label3 = tk.Label(new_window, text="Процент (годовой):").pack()
    label3_entry = tk.Entry(new_window)
    label3_entry.pack()

    attachments = tk.Label(new_window, text="Дополнительные вложения:").pack()
    attachments_entry = tk.Entry(new_window)
    attachments_entry.pack()

    period = tk.Label(new_window, text="Период").pack()
    period_var = tk.StringVar(new_window)
    period_var.set("Месяц")
    period_options = ["Месяц", "Квартал", "Год"]
    period_menu = tk.OptionMenu(new_window, period_var, *period_options)
    period_menu.pack()

    def calculate_sum():
        capital = float(label1_entry.get())
        year = int(label2_entry.get())
        procent = float(label3_entry.get())
        dop = float(attachments_entry.get())
        period = 0
        if period_var.get() == "Год":
            period = 1
        elif period_var.get() == "Квартал":
            period = 4
        else:
            period = 12

        sum = capital
        temp = dop * period
        for i in range(0, year):
            sum += sum * procent / 100 + temp

        # final_sum = capital * ((1 + procent/100)**year)# Формула с сайта
        sum = round(sum)
        result_label.config(text=f"Конечная сумма: {sum} рублей")

    calculate_button = tk.Button(new_window, text="Рассчитать", command=calculate_sum).pack()
    result_label = tk.Label(new_window, text="")
    result_label.pack(pady=10)
    return_button = tk.Button(new_window, text="Вернуться назад", command=new_window.destroy).pack()


def PROCENT():  # Рассчитывает на 98% правильно
    new_window = tk.Toplevel(frame)
    new_window.title("Расчёт Процентной ставки")

    title = Label(new_window, text="Расчёт процентной ставки\n Период реинвестирования - раз в год").pack()

    label1 = Label(new_window, text="Ваша цель(руб):").pack()
    label1_entry = tk.Entry(new_window)
    label1_entry.pack()

    label2 = tk.Label(new_window, text="Стартовый капитал(руб):").pack()
    label2_entry = tk.Entry(new_window)
    label2_entry.pack()

    label3 = tk.Label(new_window, text="Срок инвестирования(лет):").pack()
    label3_entry = tk.Entry(new_window)
    label3_entry.pack()

    attachments = tk.Label(new_window, text="Дополнительные вложения:").pack()
    attachments_entry = tk.Entry(new_window)
    attachments_entry.pack()

    period = tk.Label(new_window, text="Период").pack()
    period_var = tk.StringVar(new_window)
    period_var.set("Месяц")
    period_options = ["Месяц", "Квартал", "Год"]
    period_menu = tk.OptionMenu(new_window, period_var, *period_options)
    period_menu.pack()

    def calculate_procent():
        target = float(label1_entry.get())
        capital = int(label2_entry.get())
        year = int(label3_entry.get())
        dop = float(attachments_entry.get())
        period = 0
        if period_var.get() == "Год":
            period = 1
        elif period_var.get() == "Квартал":
            period = 4
        else:
            period = 12
        # procent = 100*((target/capital)**(1/year)) - 100
        # procent = math.exp(math.log(target / capital) / year) - 1
        tmp = dop * period

        def calculate_interest_rate(principal, years, final_amount):
            r = 0.05  # initial guess for the interest rate
            precision = 0.01  # desired precision for the result
            future_value = 0

            for _ in range(1000):  # ограничение на количество итераций, чтобы избежать бесконечного цикла
                future_value = principal  # начальная сумма
                for i in range(years):
                    future_value += tmp  # добавляем ежегодные вложения
                    future_value *= (1 + r)  # рассчитываем будущую стоимость с учетом процентной ставки
                if abs(future_value - final_amount) < precision:  # если разница меньше заданной точности, завершаем цикл
                    break
                elif future_value < final_amount:  # если будущая стоимость меньше желаемой, увеличиваем процентную ставку
                    r += 0.001
                else:  # если будущая стоимость больше желаемой, уменьшаем процентную ставку
                    r -= 0.001
            return round(r * 100, 2)

        procent = calculate_interest_rate(capital, year, target)
        procent = round(procent, 2)
        if procent > 0:
            result_label.config(text=f"Годовой процент: {procent} %")
        else:
            result_label.config(text="Введены неверные данные")

    calculate_button = tk.Button(new_window, text="Рассчитать", command=calculate_procent).pack()
    result_label = tk.Label(new_window, text="")
    result_label.pack(pady=10)
    return_button = tk.Button(new_window, text="Вернуться назад", command=new_window.destroy).pack()


def YEAR():  # рассчитывает на 100% верно
    new_window = tk.Toplevel(frame)
    new_window.title("Расчёт Срока достижения цели")

    title = Label(new_window, text="Расчёт срока достижения цели\n Период реинвестирования - раз в год").pack()

    label1 = Label(new_window, text="Стартовый капитал(руб):").pack()
    label1_entry = tk.Entry(new_window)
    label1_entry.pack()

    label2 = tk.Label(new_window, text="Ваша цель(руб):").pack()
    label2_entry = tk.Entry(new_window)
    label2_entry.pack()

    label3 = tk.Label(new_window, text="Процент (годовой):").pack()
    label3_entry = tk.Entry(new_window)
    label3_entry.pack()

    attachments = tk.Label(new_window, text="Дополнительные вложения:").pack()
    attachments_entry = tk.Entry(new_window)
    attachments_entry.pack()

    period = tk.Label(new_window, text="Период").pack()
    period_var = tk.StringVar(new_window)
    period_var.set("Месяц")
    period_options = ["Месяц", "Квартал", "Год"]
    period_menu = tk.OptionMenu(new_window, period_var, *period_options)
    period_menu.pack()

    def calculate_year():
        capital = float(label1_entry.get())
        target = float(label2_entry.get())
        procent = float(label3_entry.get())
        dop = float(attachments_entry.get())
        period = 0
        if period_var.get() == "Год":
            period = 1
        elif period_var.get() == "Квартал":
            period = 4
        else:
            period = 12

        temp = dop * period
        year = 0
        while capital < target:
            capital += capital * procent / 100 + temp
            year += 1

        result_label.config(text=f"Срок достижения цели: {year} лет")

    calculate_button = tk.Button(new_window, text="Рассчитать", command=calculate_year).pack()
    result_label = tk.Label(new_window, text="")
    result_label.pack(pady=10)
    return_button = tk.Button(new_window, text="Вернуться назад", command=new_window.destroy).pack()


def DOP():  # Рассчитывает на 95% верно
    new_window = tk.Toplevel(frame)
    new_window.title("Расчёт Дополнительных Вложений")

    title = Label(new_window, text="Расчёт Дополнительных Вложений\n Период реинвестирования - раз в год").pack()

    label1 = Label(new_window, text="Стартовый капитал(руб):").pack()
    label1_entry = tk.Entry(new_window)
    label1_entry.pack()

    label2 = tk.Label(new_window, text="Ваша цель(руб):").pack()
    label2_entry = tk.Entry(new_window)
    label2_entry.pack()

    label3 = tk.Label(new_window, text="Процент (годовой):").pack()
    label3_entry = tk.Entry(new_window)
    label3_entry.pack()

    label4 = tk.Label(new_window, text="Срок инвестирования(лет):").pack()
    label4_entry = tk.Entry(new_window)
    label4_entry.pack()

    period = tk.Label(new_window, text="Период").pack()
    period_var = tk.StringVar(new_window)
    period_var.set("Месяц")
    period_options = ["Месяц", "Квартал", "Год"]
    period_menu = tk.OptionMenu(new_window, period_var, *period_options)
    period_menu.pack()

    def calculate_dop():
        capital = float(label1_entry.get())
        target = float(label2_entry.get())
        procent = float(label3_entry.get()) * 0.01
        year = int(label4_entry.get())
        period = 0
        if period_var.get() == "Год":
            period = 1
        elif period_var.get() == "Квартал":
            period = 4
        else:
            period = 12

        def calculate_pmt(PV, r, n, FV):
            r_monthly = r / period  # Процентная ставка в месяц
            n_months = n * period  # Количество месяцев

            PMT = (FV - PV * (1 + r_monthly) ** n_months) / (((1 + r_monthly) ** n_months - 1) / r_monthly)
            return PMT

        sum = calculate_pmt(capital, procent, year, target)
        sum = round(sum)
        if sum > 0:
            result_label.config(text=f"Необходимый размер пополнения: {sum} рублей в {period_var.get()}")
        else:
            result_label.config(text=f"Дополнительных вложений не требуется")

    calculate_button = tk.Button(new_window, text="Рассчитать", command=calculate_dop).pack()
    result_label = tk.Label(new_window, text="")
    result_label.pack(pady=10)
    return_button = tk.Button(new_window, text="Вернуться назад", command=new_window.destroy).pack()


def CAPITAL():  # Расчёты верны на 90%
    new_window = tk.Toplevel(frame)
    new_window.title("Расчёт Стартового Капитала")

    title = Label(new_window, text="Расчёт Стартового Капита\n Период реинвестирования - раз в год").pack()

    label1 = Label(new_window, text="Конечная сумма(руб):").pack()
    label1_entry = tk.Entry(new_window)
    label1_entry.pack()

    label2 = tk.Label(new_window, text="Срок инвестирования(лет):").pack()
    label2_entry = tk.Entry(new_window)
    label2_entry.pack()

    label3 = tk.Label(new_window, text="Процент (годовой):").pack()
    label3_entry = tk.Entry(new_window)
    label3_entry.pack()

    attachments = tk.Label(new_window, text="Дополнительные вложения:").pack()
    attachments_entry = tk.Entry(new_window)
    attachments_entry.pack()

    period = tk.Label(new_window, text="Период").pack()
    period_var = tk.StringVar(new_window)
    period_var.set("Месяц")
    period_options = ["Месяц", "Квартал", "Год"]
    period_menu = tk.OptionMenu(new_window, period_var, *period_options)
    period_menu.pack()

    def calculate_sum():
        target = float(label1_entry.get())
        year = int(label2_entry.get())
        procent = float(label3_entry.get()) / 100
        dop = float(attachments_entry.get())
        period = 0
        if period_var.get() == "Год":
            period = 1
        elif period_var.get() == "Квартал":
            period = 4
        else:
            period = 12

        def calculate_starting_capital(future_value, annual_interest_rate, years, additional_investments,
                                       investment_period):
            present_value = future_value / (1 + annual_interest_rate) ** years
            present_value -= additional_investments * (
                        (1 + annual_interest_rate) ** years - 1) / annual_interest_rate * (
                                         1 + annual_interest_rate) ** investment_period
            return present_value

        sum = calculate_starting_capital(target, procent, year, dop, period)
        sum = round(sum, 1)
        if sum > 0:
            result_label.config(text=f"Стартовый капитал должен составить: {sum} рублей")
        else:
            result_label.config(text=f"Неверно введены данные")

    calculate_button = tk.Button(new_window, text="Рассчитать", command=calculate_sum).pack()
    result_label = tk.Label(new_window, text="")
    result_label.pack(pady=10)
    return_button = tk.Button(new_window, text="Вернуться назад", command=new_window.destroy).pack()


root = Tk()
root.title("Калькулятор для инвестора")
root.geometry(f'{LENGHT}x{WIDTH}')

frame = Frame(root, bg='grey')
frame.place(relwidth=1, relheight=1)

function_list = []

title = Label(frame, text="Что вы хотите вычислить?", font=20, bg="white")
title.place(rely=0.01, relx=0.1)

buttons_name = [
    "Конечную сумму",
    "Процент",
    "Срок достижения цели",
    "Размер пополнений",
    "Стартовый капитал"
]

buttons = [SUM, PROCENT, YEAR, DOP, CAPITAL]
for i in range(len(buttons_name)):
    btn = Button(frame, text=buttons_name[i], command=buttons[i], padx=10, pady=5, width=50)
    btn.place(rely=0.06 + i * 0.05, relx=0.03)
    buttons.append(btn)

root.mainloop()
