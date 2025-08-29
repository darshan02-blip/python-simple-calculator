# Fancy Calculator (CLI + Tkinter optional)
import tkinter as tk

def cli_calculator():
    while True:
        print("\n🔢 Calculator Menu")
        print("1 ➕ Addition")
        print("2 ➖ Subtraction")
        print("3 ✖ Multiplication")
        print("4 ➗ Division")
        print("5 ❌ Exit")

        choice = input("👉 Enter your choice (1-5): ")

        if choice == '5':
            print("👋 Exiting Calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("⚠ Invalid choice! Try again.")
            continue

        try:
            num1 = float(input("🔹 Enter first number: "))
            num2 = float(input("🔹 Enter second number: "))
        except ValueError:
            print("⚠ Please enter valid numbers!")
            continue

        if choice == '1':
            result = num1 + num2
            print(f"✅ {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"✅ {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"✅ {num1} × {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("⚠ Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"✅ {num1} ÷ {num2} = {result}")

def gui_calculator():
    def calculate():
        try:
            n1 = float(entry1.get())
            n2 = float(entry2.get())
            op = operation.get()

            if op == "Addition":
                res.set(f"✅ {n1} + {n2} = {n1+n2}")
            elif op == "Subtraction":
                res.set(f"✅ {n1} - {n2} = {n1-n2}")
            elif op == "Multiplication":
                res.set(f"✅ {n1} × {n2} = {n1*n2}")
            elif op == "Division":
                if n2 == 0:
                    res.set("⚠ Cannot divide by zero!")
                else:
                    res.set(f"✅ {n1} ÷ {n2} = {n1/n2}")
        except:
            res.set("⚠ Invalid input!")

    win = tk.Tk()
    win.title("Fancy Calculator")

    tk.Label(win, text="🔹 Enter first number:").pack()
    entry1 = tk.Entry(win)
    entry1.pack()

    tk.Label(win, text="🔹 Enter second number:").pack()
    entry2 = tk.Entry(win)
    entry2.pack()

    operation = tk.StringVar(value="Addition")
    tk.OptionMenu(win, operation, "Addition", "Subtraction", "Multiplication", "Division").pack()

    tk.Button(win, text="Calculate", command=calculate).pack()
    res = tk.StringVar()
    tk.Label(win, textvariable=res, font=("Arial", 14), fg="blue").pack()

    win.mainloop()

# Run CLI by default
if __name__ == "__main__":
    print("Choose Mode:")
    print("1. CLI (Command Line)")
    print("2. GUI (Tkinter)")
    mode = input("👉 Enter choice (1/2): ")

    if mode == '2':
        gui_calculator()
    else:
        cli_calculator()
