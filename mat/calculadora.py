from tkinter import *
from tkinter import messagebox


def virgula():
    output.insert(END, ",")


def porgentagem():
    output.insert(END, "%")


def apagar_um():
    posicao = len(output.get())
    output.delete(posicao-1, posicao)


def limpar():
    output.delete(0, END)


def number_7():
    output.insert(END, "7")


def number_8():
    output.insert(END, "8")


def number_9():
    output.insert(END, "9")


def divisao():
    output.insert(END, "÷")


def number_4():
    output.insert(END, "4")


def number_5():
    output.insert(END, "5")


def number_6():
    output.insert(END, "6")


def mult():
    output.insert(END, "×")


def number_1():
    output.insert(END, "1")


def number_2():
    output.insert(END, "2")


def number_3():
    output.insert(END, "3")


def subtracao():
    output.insert(END, "-")


def number_0():
    output.insert(END, "0")


def igualdade():
    result = output.get()
    if result == "":
        messagebox.showinfo("Alerta", "O Campo de Calculo Esta Vazio")
    else:
        calculo = eval(result.replace("×", "*").replace("÷", "/").replace(",", ".").replace("%", "/100"))
        output.delete(0, END)
        output.insert(END, calculo)


def soma():
    output.insert(END, "+")


tela = Tk()
tela.title("Calculadora - v1")
tela.resizable(False, False)
tela.config(border=15, bg='#1C1C1C')
output = Entry(tela)
output.config(font=2)
output.grid(column=0, row=0, columnspan=4, ipady=3)

BG_NUMBERS = '#000000'
FG_NUMBERS = 'white'
BG_OPERADORES = '#FB5000'
BG_OUTROS = '#1A6C01'
WIDTH_BTNS = 2
FONT_NUMBERS = 10

PADY_TOP = (20, 5)
PADY_LINE1 = (5, 5)
PADY_LINE2 = (5, 5)
PADY_BOTTOM = (5, 30)

HOVER_NUMBERS = '#262525'
HOVER_OPERADORES = '#DE9776'
HOVER_OUTROS = '#6BB256'

# LINE - 1
btn_virgula = Button(tela, text=",", width=WIDTH_BTNS, bg=BG_OUTROS,
                     activebackground=HOVER_OUTROS, command=virgula)
btn_porcentagem = Button(tela, text="%", width=WIDTH_BTNS, bg=BG_OUTROS,
                         activebackground=HOVER_OUTROS, command=porgentagem)
btn_apagar_um = Button(tela, text="<", width=WIDTH_BTNS, bg=BG_OUTROS,
                       activebackground=HOVER_OUTROS, command=apagar_um)
btn_limpar = Button(tela, text="C", width=WIDTH_BTNS,
                    activebackground=HOVER_OPERADORES, bg=BG_OPERADORES, command=limpar)
# LINE - 2
btn_7 = Button(tela, text="7", width=WIDTH_BTNS, bg=BG_NUMBERS, fg=FG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_7)
btn_8 = Button(tela, text="8", width=WIDTH_BTNS, bg=BG_NUMBERS, fg=FG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_8)
btn_9 = Button(tela, text="9", width=WIDTH_BTNS, bg=BG_NUMBERS, fg=FG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_9)
btn_divisao = Button(tela, text="÷", width=WIDTH_BTNS,
                     activebackground=HOVER_OPERADORES, bg=BG_OPERADORES, command=divisao)
# LINE - 3
btn_4 = Button(tela, text="4", width=WIDTH_BTNS, bg=BG_NUMBERS, fg=FG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_4)
btn_5 = Button(tela, text="5", width=WIDTH_BTNS, bg=BG_NUMBERS, fg=FG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_5)
btn_6 = Button(tela, text="6", width=WIDTH_BTNS, bg=BG_NUMBERS, fg=FG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_6)
btn_mult = Button(tela, text="×", width=WIDTH_BTNS,
                  activebackground=HOVER_OPERADORES, bg=BG_OPERADORES, command=mult)
# LINE - 4
btn_1 = Button(tela, text="1", width=WIDTH_BTNS, bg=BG_NUMBERS, fg=FG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_1)
btn_2 = Button(tela, text="2", width=WIDTH_BTNS, bg=BG_NUMBERS, fg=FG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_2)
btn_3 = Button(tela, text="3", width=WIDTH_BTNS, bg=BG_NUMBERS, fg=FG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_3)
btn_subtracao = Button(tela, text="-", width=WIDTH_BTNS,
                       activebackground=HOVER_OPERADORES, bg=BG_OPERADORES, command=subtracao)
# LINE - 5
btn_0 = Button(tela, text="0", width=8, bg=BG_NUMBERS,
               activebackground=HOVER_NUMBERS, command=number_0, fg=FG_NUMBERS,)
btn_igualdade = Button(tela, text="=", width=WIDTH_BTNS, bg=BG_OUTROS,
                       activebackground=HOVER_OUTROS, command=igualdade)
btn_soma = Button(tela, text="+", width=WIDTH_BTNS,
                  activebackground=HOVER_OPERADORES, bg=BG_OPERADORES, command=soma)

# LINE - 1 GRID
btn_virgula.grid(column=0, row=1, pady=PADY_TOP, ipadx=2)
btn_porcentagem.grid(column=1, row=1, pady=PADY_TOP, ipadx=2)
btn_apagar_um.grid(column=2, row=1, pady=PADY_TOP, ipadx=2)
btn_limpar.grid(column=3, row=1, pady=PADY_TOP, ipadx=2)
# LINE - 2 GRID
btn_7.grid(column=0, row=2, pady=PADY_LINE1, ipadx=2)
btn_8.grid(column=1, row=2, pady=PADY_LINE1, ipadx=2)
btn_9.grid(column=2, row=2, pady=PADY_LINE1, ipadx=2)
btn_divisao.grid(column=3, row=2, pady=PADY_LINE1, ipadx=2)
# LINE - 3 GRID
btn_4.grid(column=0, row=3, pady=PADY_LINE2, ipadx=2)
btn_5.grid(column=1, row=3, pady=PADY_LINE2, ipadx=2)
btn_6.grid(column=2, row=3, pady=PADY_LINE2, ipadx=2)
btn_mult.grid(column=3, row=3, pady=PADY_LINE2, ipadx=2)
# LINE - 4 GRID
btn_1.grid(column=0, row=4, pady=PADY_LINE2, ipadx=2)
btn_2.grid(column=1, row=4, pady=PADY_LINE2, ipadx=2)
btn_3.grid(column=2, row=4, pady=PADY_LINE2, ipadx=2)
btn_subtracao.grid(column=3, row=4, pady=PADY_LINE2, ipadx=2)
# LINE - 5 GRID
btn_0.grid(column=0, row=5, pady=PADY_BOTTOM, columnspan=2, ipadx=3.5)
btn_igualdade.grid(column=2, row=5, pady=PADY_BOTTOM, ipadx=2)
btn_soma.grid(column=3, row=5, pady=PADY_BOTTOM, ipadx=2)

tela.mainloop()
