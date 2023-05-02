import tkinter as tk
from tkinter import messagebox
from qrcode import make
from PIL import ImageTk, Image

def generate_qr():
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return
    qr = make(url)
    img = ImageTk.PhotoImage(qr)
    label.config(image=img)
    label.image = img
    qr.show()

root = tk.Tk()
root.title("QR Code Generator")

label = tk.Label(root)
label.pack()

entry = tk.Entry(root)
entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

root.mainloop()
