# dashboard_window.py
from customtkinter import *
from PIL import Image

# Calculate the center of screen
def centerWindow(window, width=1024, height=800):
    # Get the width and height of the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

# Dashboard Window code
def dashboard_window():
    app = CTkToplevel()
    app.geometry("1024x800")
    app.title("Dashboard Liga Generator")
    set_appearance_mode("light")

    centerWindow(app)

    # Define colors and fonts
    text_font = CTkFont(family="Helvetica", size=18)
    title_font = CTkFont(family="Helvetica", size=25, weight="bold")
    image_path = r"C:/Users/asus/Documents/GitHub/LigaGenerator/assets/icons/icon.png"
    main_color = "#FC6A03"
    hover_color = "#FF8C42"

    # Sidebar
    sidebar(app, text_font,  title_font, main_color, hover_color, image_path)

    content_frame = CTkFrame(app, corner_radius=0, fg_color="#ffffff")
    content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    # Title
    title_label = CTkLabel(content_frame, text="Liga Generator", font=title_font, text_color="black")
    title_label.pack(pady=20)

    app.mainloop()

# Sidebar
def sidebar(app, text_font, title_font, main_color, hover_color, image_path):
    # Create sidebar frame
    sidebar_frame = CTkFrame(app, width=400, corner_radius=0, fg_color=main_color)
    sidebar_frame.pack(side=LEFT, fill=Y)

    # Image
    image = CTkImage(light_image=Image.open(image_path), size=(100, 100))
    image_label = CTkLabel(sidebar_frame, image=image, text="")
    image_label.pack(pady=10, padx=10, fill=X)

    # Buttons
    btn_home = CTkButton(sidebar_frame, text="Home", corner_radius=25, fg_color=main_color, hover_color=hover_color, font=text_font, text_color="white")
    btn_home.pack(pady=10, padx=10, fill=X)

    btn_results = CTkButton(sidebar_frame, text="Results", corner_radius=25, fg_color=main_color,hover_color=hover_color, font=text_font, text_color="white")
    btn_results.pack(pady=10, padx=10, fill=X)

    btn_reports = CTkButton(sidebar_frame, text="Reports", corner_radius=25, fg_color=main_color, hover_color=hover_color, font=text_font, text_color="white")
    btn_reports.pack(pady=10, padx=10, fill=X)

    btn_settings = CTkButton(sidebar_frame, text="Settings", corner_radius=25, fg_color=main_color, hover_color=hover_color, font=text_font, text_color="white")
    btn_settings.pack(pady=10, padx=10, fill=X)

    btn_about = CTkButton(sidebar_frame, text="About", corner_radius=25, fg_color=main_color, hover_color=hover_color, font=text_font, text_color="white")
    btn_about.pack(pady=10, padx=10, fill=X)

    return sidebar_frame