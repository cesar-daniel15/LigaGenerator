# main_window.py
from customtkinter import *
from PIL import Image
from dashboard import dashboard_window


# Calculate the center of screen
def centerWindow(window, width=500, height=400):
    # Get the width and height of the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

# Show the loader
def showLoader():
    loader.place(relx=0.5, rely=0.7, anchor=CENTER)
    loader.start()
    btn.configure(state="disabled")
    app.after(2000, openNextWindow)

# Open the next window
def openNextWindow():
    loader.stop()
    loader.place_forget()
    app.withdraw()
    dashboard_window()

app = CTk()
app.geometry("500x400")
app.title("Liga Generator")
set_appearance_mode("light")

centerWindow(app)

my_font = CTkFont(family="Helvetica", size=18, weight="bold")
title_font = CTkFont(family="Helvetica", size=25, weight="bold")
image_path = r"C:/Users/asus/Documents/GitHub/LigaGenerator/assets/icons/icon.png"

# Button
btn = CTkButton(master=app, text="Launch", corner_radius=32, fg_color="#FC6A03", hover_color="#FF8C42", font=my_font, width=150, height=50, command=showLoader)
btn.place(relx=0.5, rely=0.8, anchor=CENTER)

# Title
title_label = CTkLabel(master=app, text="Liga Generator", font=title_font, text_color="black")
title_label.place(relx=0.5, rely=0.6, anchor=CENTER)

# Image
image = CTkImage(light_image=Image.open(image_path), size=(200, 200))
image_label = CTkLabel(app, image=image, text="")
image_label.pack()

# Loader
loader = CTkProgressBar(master=app, mode="indeterminate", fg_color="#FC6A03", progress_color="black", width=200)
loader.configure()

app.mainloop()