# dashboard.py
from customtkinter import *

def dashboard_window():
    dashboard_window = CTkToplevel()
    dashboard_window.title("Dashboard")

    label = CTkLabel(dashboard_window, text="Bem-vindo ao Dashboard!", font=("Helvetica", 18, "bold"))
    label.pack(pady=50)

    dashboard_window.geometry("600x400")
    dashboard_window.mainloop()
