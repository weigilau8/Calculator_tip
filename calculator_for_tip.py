import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_tip():
    try:
        bill = float(bill_entry.get())
        tip_percentage = int(tip_entry.get())
        split_by = int(split_entry.get())

        if tip_percentage not in (10, 15) and tip_percentage > 0:
          confirmation = messagebox.askyesno("Confirm Other Tip", f"You've entered {tip_percentage}%. Are you sure?")
          if not confirmation:
              return

        if bill <= 0 or split_by <= 0 or tip_percentage < 0:
            raise ValueError("Please enter valid positive numbers.")
        
        percentage = (tip_percentage / 100) + 1
        bill_plus_tip = (bill * percentage)
        pay = round(bill_plus_tip / split_by, 2)
        result_label.config(text=f"Each person should pay: ${pay}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")


main = tk.Tk()
main.title("Tip Calculator")


bill_label = ttk.Label(main, text="Total Bill: $")
bill_label.grid(row=0, column=0, padx=5, pady=5, sticky="w") 
bill_entry = ttk.Entry(main)
bill_entry.grid(row=0, column=1, padx=5, pady=5)


tip_label = ttk.Label(main, text="Tip Percentage (10, 15, or other):")
tip_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
tip_entry = ttk.Entry(main)
tip_entry.grid(row=1, column=1, padx=5, pady=5)


split_label = ttk.Label(main, text="Split By:")
split_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
split_entry = ttk.Entry(main)
split_entry.grid(row=2, column=1, padx=5, pady=5)


calculate_button = ttk.Button(main, text="Calculate", command=calculate_tip)
calculate_button.grid(row=3, column=0, columnspan=2, pady=(10, 5))


result_label = ttk.Label(main, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=(0, 10))

main.mainloop()