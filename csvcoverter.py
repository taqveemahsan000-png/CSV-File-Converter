import csv
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


def list_to_csv(data, filename="output.csv"):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow([item])
        messagebox.showinfo("Success", f"List successfully written to {filename}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def convert_to_csv():
    text_data = text_box.get("1.0", tk.END).strip()
    if not text_data:
        messagebox.showerror("Error", "Please paste a list of numbers.")
        return

    data = text_data.split("\n")
    filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if filename:
        list_to_csv(data, filename)


root = tk.Tk()
root.title("List to CSV Converter")
root.geometry("400x300")

label = tk.Label(root, text="Paste your list below:")
label.pack(pady=5)

text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_box.pack(padx=10, pady=10)

convert_button = tk.Button(root, text="Convert to CSV", command=convert_to_csv)
convert_button.pack(pady=10)

root.mainloop()