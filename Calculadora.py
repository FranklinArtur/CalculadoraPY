import tkinter as tk
from tkinter import messagebox
import math
from fractions import Fraction
from sympy import symbols, Eq, solve
from sympy.parsing.sympy_parser import parse_expr

def calcular_basico():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacao = operacao_var.get()

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero!")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Erro", "Operação inválida!")
            return

        messagebox.showinfo("Resultado", f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos!")

def calcular_bhaskara():
    try:
        a = float(entry_bhaskara_a.get())
        b = float(entry_bhaskara_b.get())
        c = float(entry_bhaskara_c.get())
        delta = b**2 - 4*a*c
        if delta < 0:
            messagebox.showerror("Erro", "Delta negativo! Sem raízes reais.")
            return
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        messagebox.showinfo("Resultado", f"Raízes:\nX1 = {x1}\nX2 = {x2}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

def calcular_expressao_algebrica():
    try:
        expressao = entry_expressao.get()
        resultado = parse_expr(expressao).evalf()
        messagebox.showinfo("Resultado", f"Resultado: {resultado}")
    except SyntaxError:
        messagebox.showerror("Erro", "Erro de sintaxe! Verifique a expressão e tente novamente.")
    except Exception as e:
        messagebox.showerror("Erro", f"Expressão inválida!\nErro: {e}")

def calcular_regra_de_tres():
    try:
        a = float(entry_regra_a.get())
        b = float(entry_regra_b.get())
        c = float(entry_regra_c.get())
        d = (b * c) / a
        messagebox.showinfo("Resultado", f"{a} está para {b} assim como {c} está para {d}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

def calcular_porcentagem():
    try:
        total = float(entry_porcentagem_total.get())
        porcentagem = float(entry_porcentagem_percent.get())
        resultado = (total * porcentagem) / 100
        messagebox.showinfo("Resultado", f"Porcentagem: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

def verificar_conjuntos():
    try:
        conjunto1 = set(map(int, entry_conjunto1.get().split(',')))
        conjunto2 = set(map(int, entry_conjunto2.get().split(',')))
        uniao = conjunto1.union(conjunto2)
        interseccao = conjunto1.intersection(conjunto2)
        diferenca = conjunto1.difference(conjunto2)
        simetrica = conjunto1.symmetric_difference(conjunto2)
        subconjunto = conjunto1.issubset(conjunto2)
        messagebox.showinfo("Resultado", f"União: {uniao}\nInterseção: {interseccao}\nDiferença: {diferenca}\nDiferença Simétrica: {simetrica}\nConjunto 1 é subconjunto do Conjunto 2? {subconjunto}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores inteiros separados por vírgula!")

def resolver_sistema_linear():
    try:
        a1 = float(entry_sistema_a1.get())
        b1 = float(entry_sistema_b1.get())
        c1 = float(entry_sistema_c1.get())
        a2 = float(entry_sistema_a2.get())
        b2 = float(entry_sistema_b2.get())
        c2 = float(entry_sistema_c2.get())

        eq1 = Eq(a1 * symbols('x') + b1 * symbols('y'), c1)
        eq2 = Eq(a2 * symbols('x') + b2 * symbols('y'), c2)

        resultado = solve((eq1, eq2), (symbols('x'), symbols('y')))
        messagebox.showinfo("Resultado", f"Solução do Sistema Linear: x = {resultado[symbols('x')]}, y = {resultado[symbols('y')]}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

root = tk.Tk()
root.title("Calculadora Avançada")
root.geometry("500x500")

frame_basico = tk.LabelFrame(root, text="Operações Básicas")
frame_basico.pack(pady=5)
entry_num1 = tk.Entry(frame_basico, width=10)
entry_num1.pack(side=tk.LEFT, padx=5)
operacao_var = tk.StringVar()
operacao_var.set("+")
tk.OptionMenu(frame_basico, operacao_var, "+", "-", "*", "/").pack(side=tk.LEFT, padx=5)
entry_num2 = tk.Entry(frame_basico, width=10)
entry_num2.pack(side=tk.LEFT, padx=5)
tk.Button(frame_basico, text="Calcular", command=calcular_basico).pack(side=tk.LEFT, padx=5)

frame_bhaskara = tk.LabelFrame(root, text="Fórmula de Bhaskara")
frame_bhaskara.pack(pady=5)
entry_bhaskara_a = tk.Entry(frame_bhaskara, width=10)
entry_bhaskara_a.pack(side=tk.LEFT, padx=5)
entry_bhaskara_b = tk.Entry(frame_bhaskara, width=10)
entry_bhaskara_b.pack(side=tk.LEFT, padx=5)
entry_bhaskara_c = tk.Entry(frame_bhaskara, width=10)
entry_bhaskara_c.pack(side=tk.LEFT, padx=5)
tk.Button(frame_bhaskara, text="Calcular", command=calcular_bhaskara).pack(side=tk.LEFT, padx=5)

frame_expressao = tk.LabelFrame(root, text="Expressões Algébricas")
frame_expressao.pack(pady=5)
entry_expressao = tk.Entry(frame_expressao, width=30)
entry_expressao.pack()
tk.Label(frame_expressao, text="Digite uma expressão algébrica válida, ex: 2*x + 3*y - 5").pack()
tk.Button(frame_expressao, text="Calcular", command=calcular_expressao_algebrica).pack()

frame_regra = tk.LabelFrame(root, text="Regra de Três")
frame_regra.pack(pady=5)
entry_regra_a = tk.Entry(frame_regra, width=5)
entry_regra_a.pack(side=tk.LEFT)
tk.Label(frame_regra, text="está para").pack(side=tk.LEFT)
entry_regra_b = tk.Entry(frame_regra, width=5)
entry_regra_b.pack(side=tk.LEFT)
tk.Label(frame_regra, text="assim como").pack(side=tk.LEFT)
entry_regra_c = tk.Entry(frame_regra, width=5)
entry_regra_c.pack(side=tk.LEFT)
tk.Button(frame_regra, text="Calcular", command=calcular_regra_de_tres).pack(side=tk.LEFT)

frame_porcentagem = tk.LabelFrame(root, text="Porcentagem")
frame_porcentagem.pack(pady=5)
entry_porcentagem_total = tk.Entry(frame_porcentagem, width=10)
entry_porcentagem_total.pack(side=tk.LEFT, padx=5)
tk.Label(frame_porcentagem, text="de").pack(side=tk.LEFT, padx=5)
entry_porcentagem_percent = tk.Entry(frame_porcentagem, width=10)
entry_porcentagem_percent.pack(side=tk.LEFT, padx=5)
tk.Button(frame_porcentagem, text="Calcular", command=calcular_porcentagem).pack(side=tk.LEFT, padx=5)

frame_conjuntos = tk.LabelFrame(root, text="Operações com Conjuntos")
frame_conjuntos.pack(pady=5)
entry_conjunto1 = tk.Entry(frame_conjuntos, width=20)
entry_conjunto1.pack()
entry_conjunto2 = tk.Entry(frame_conjuntos, width=20)
entry_conjunto2.pack()
tk.Button(frame_conjuntos, text="Calcular", command=verificar_conjuntos).pack()

frame_sistema_linear = tk.LabelFrame(root, text="Sistema Linear")
frame_sistema_linear.pack(pady=5)
entry_sistema_a1 = tk.Entry(frame_sistema_linear, width=5)
entry_sistema_a1.pack(side=tk.LEFT)
entry_sistema_b1 = tk.Entry(frame_sistema_linear, width=5)
entry_sistema_b1.pack(side=tk.LEFT)
entry_sistema_c1 = tk.Entry(frame_sistema_linear, width=5)
entry_sistema_c1.pack(side=tk.LEFT)
entry_sistema_a2 = tk.Entry(frame_sistema_linear, width=5)
entry_sistema_a2.pack(side=tk.LEFT)
entry_sistema_b2 = tk.Entry(frame_sistema_linear, width=5)
entry_sistema_b2.pack(side=tk.LEFT)
entry_sistema_c2 = tk.Entry(frame_sistema_linear, width=5)
entry_sistema_c2.pack(side=tk.LEFT)
tk.Button(frame_sistema_linear, text="Calcular", command=resolver_sistema_linear).pack(side=tk.LEFT)

root.mainloop()