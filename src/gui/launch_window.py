# Launch Window code

from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")
app.title("Liga Generator")
set_appearance_mode("light")

my_font = CTkFont(family="Helvetica", size=18, weight="bold")
title_font = CTkFont(family="Helvetica", size=25, weight="bold")
image_path = r"C:/Users/asus/Documents/GitHub/LigaGenerator/assets/icons/icon.png"

# Button
btn = CTkButton(master=app, text="Entrar", corner_radius=32, fg_color="#FC6A03", hover_color="#FF8C42", font=my_font, width=150, height=50)
btn.place(relx=0.5, rely=0.8, anchor=CENTER)

# Title
title_label = CTkLabel(master=app, text="Liga Generator", font=title_font, text_color="black")
title_label.place(relx=0.5, rely=0.6, anchor=CENTER)

# Image
image = CTkImage(light_image=Image.open(image_path), size=(200, 200))
image_label = CTkLabel(app, image=image, text="")
image_label.pack()

app.mainloop()