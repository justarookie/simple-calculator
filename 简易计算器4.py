import tkinter as tk
from functools import partial

class CalculatorModel:
    def __init__(self):
        self.expression = ""

    def clear(self):
        self.expression = ""

    def append_to_expression(self, value):
        self.expression += str(value)

    def evaluate_expression(self):
        try:
            expression = self.expression.replace("÷", "/").replace("x", "*")
            result = eval(expression)
            return int(result) if result.is_integer() else result
        except Exception:
            return "Error"

    def calculate_percentage(self):
        try:
            expression = eval(self.expression)
            return expression / 100
        except Exception:
            return "Error"

class CalculatorView:
    def __init__(self, master, controller):
        self.display = tk.Label(master, text="", font=("Helvetica", 16), height=2, width=18)
        self.display.grid(row=0, column=0, columnspan=4, pady=10)
        self.controller = controller

    def update_display(self, text):
        self.display["text"] = text

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def on_keypress(self, key):
        if key == "AC":
            self.model.clear()
            self.view.update_display("")
        elif key == "←":
            self.model.expression = self.model.expression[:-1]
            self.view.update_display(self.model.expression)
        elif key == "%":
            result = self.model.calculate_percentage()
            self.view.update_display(str(result))
        elif key == "=":
            result = self.model.evaluate_expression()
            self.view.update_display(str(result))
        else:
            self.model.append_to_expression(key)
            self.view.update_display(self.model.expression)
    def on_keyboard_input(self, event):
        """处理键盘输入"""
        key = event.char
        if key.isdigit() or key in "+-*/.x÷%()=":
            self.on_keypress(key)
        elif key == "\r":  # 回车键相当于“=”
            self.on_keypress("=")
        elif key == "\b":  # 退格键
            self.on_keypress("←")
        elif key.lower() == "c":  # 小写"c"或大写"C"
            self.on_keypress("AC")
def create_calculator_window():
    window = tk.Tk()
    window.geometry("300x450")
    window.title("MVC计算器")

    model = CalculatorModel()
    view = CalculatorView(window, None)
    controller = CalculatorController(model, view)
    view.controller = controller

    keys = [
        ("AC", "clear"),
        ("←", "backspace"),
        ("% ", "percentage"),
        ("÷", "operator"),
        ("7", "number"),
        ("8", "number"),
        ("9", "number"),
        ("x", "operator"),
        ("4", "number"),
        ("5", "number"),
        ("6", "number"),
        ("-", "operator"),
        ("1", "number"),
        ("2", "number"),
        ("3", "number"),
        ("+", "operator"),
        ("0", "number"),
        (".", "decimal"),
        ("(", "bracket"),
        (")", "bracket"),
        ("=", "calculate")
    ]

    def get_command(controller, key_type, key):
        """根据键类型返回对应的控制器方法"""
        commands = {
            "clear": lambda: controller.on_keypress("AC"),
            "backspace": lambda: controller.on_keypress("←"),
            "percentage": lambda: controller.on_keypress("%"),
            "operator": lambda: controller.on_keypress(key),
            "number": lambda: controller.on_keypress(key),
            "decimal": lambda: controller.on_keypress("."),
            "bracket": lambda: controller.on_keypress(key),
            "calculate": lambda: controller.on_keypress("=")
        }
        return commands[key_type] if key_type in commands else lambda: None


    row = 1
    col = 0
    for key, key_type in keys:
        button = tk.Button(window, text=key, font=("Helvetica", 12), height=2, width=5)
        button.grid(row=row, column=col, padx=5, pady=5)
        # 根据键类型获取并绑定正确的命令处理器
        button.configure(command=get_command(controller, key_type, key))
        col += 1
        if col > 3:
            col = 0
            row += 1

    row = 1
    col = 0
    for key, _ in keys:
        button = tk.Button(window, text=key, font=("Helvetica", 12), height=2, width=5)
        button.grid(row=row, column=col, padx=5, pady=5)
        # 绑定按钮到控制器的方法，并传递按键字符
        button.configure(command=partial(controller.on_keypress, key))
        col += 1
        if col > 3:
            col = 0
            row += 1
    window.bind("<Key>", controller.on_keyboard_input)
    window.mainloop()

if __name__ == "__main__":
    create_calculator_window()