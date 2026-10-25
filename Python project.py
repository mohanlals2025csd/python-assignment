
import tkinter as tk
import random

PALETTES = {
    "SUNSET": ["#FF6B6B", "#F7B267", "#F79D65", "#C8553D", "#723D46"],
    "OCEAN": ["#03045E", "#0077B6", "#00B4D8", "#90E0EF", "#CAF0F8"],
    "FOREST": ["#283618", "#606C38", "#A3B18A", "#DDA15E", "#BC6C25"],
    "CANDY": ["#FF99C8", "#FCF6BD", "#D0F4DE", "#A9DEF9", "#E4C1F9"],
    "LAVENDER": ["#6A4C93", "#9D84B7", "#C8B6E2", "#EDE3F5", "#F7F1FA"],
}

BG = "#171923"
CARD_BG = "#242735"
TEXT = "#F7F7FB"
MUTED = "#A6A9B8"

root = tk.Tk()
root.title("Palette Studio")
root.geometry("760x570")
root.configure(bg=BG)
root.resizable(False, False)

current_colors = []

def copy_color(color):
    root.clipboard_clear()
    root.clipboard_append(color)
    status_label.config(text=f"{color} copied!")

def show_palette(theme, colors=None):
    global current_colors
    current_colors = list(colors if colors else PALETTES[theme])

    theme_label.config(text=f"{theme} PALETTE")
    status_label.config(text="Click a color card to copy its hex code.")

    for widget in color_frame.winfo_children():
        widget.destroy()

    for color in current_colors:
        card = tk.Frame(color_frame, bg=CARD_BG, padx=7, pady=7)
        card.pack(side="left", padx=7)

        swatch = tk.Button(
            card,
            text="",
            bg=color,
            activebackground=color,
            width=12,
            height=7,
            relief="flat",
            cursor="hand2",
            command=lambda c=color: copy_color(c)
        )
        swatch.pack()

        tk.Label(
            card,
            text=color,
            bg=CARD_BG,
            fg=TEXT,
            font=("Arial", 10, "bold")
        ).pack(pady=(9, 2))

        tk.Label(
            card,
            text="CLICK TO COPY",
            bg=CARD_BG,
            fg=MUTED,
            font=("Arial", 7)
        ).pack()

def random_palette():
    colors = [
        "#{:02X}{:02X}{:02X}".format(
            random.randint(40, 240),
            random.randint(40, 240),
            random.randint(40, 240)
        )
        for _ in range(5)
    ]
    show_palette("YOUR RANDOM", colors)

tk.Label(
    root,
    text="✦  PALETTE STUDIO",
    bg=BG,
    fg=TEXT,
    font=("Arial", 25, "bold")
).pack(pady=(25, 5))

tk.Label(
    root,
    text="Pick a mood. Find your colors.",
    bg=BG,
    fg=MUTED,
    font=("Arial", 11)
).pack(pady=(0, 20))

theme_frame = tk.Frame(root, bg=BG)
theme_frame.pack()

for theme in PALETTES:
    tk.Button(
        theme_frame,
        text=theme.title(),
        bg=CARD_BG,
        fg=TEXT,
        activebackground="#393D50",
        activeforeground=TEXT,
        relief="flat",
        padx=13,
        pady=8,
        cursor="hand2",
        command=lambda t=theme: show_palette(t)
    ).pack(side="left", padx=5)

theme_label = tk.Label(
    root,
    text="",
    bg=BG,
    fg="#B9A0FF",
    font=("Arial", 12, "bold")
)
theme_label.pack(pady=(30, 12))

color_frame = tk.Frame(root, bg=BG)
color_frame.pack()

tk.Button(
    root,
    text="✦  Surprise Me",
    bg="#8066D4",
    fg="white",
    activebackground="#6C53BD",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=random_palette
).pack(pady=27)

status_label = tk.Label(
    root,
    text="",
    bg=BG,
    fg=MUTED,
    font=("Arial", 10)
)
status_label.pack()

show_palette("SUNSET")
root.mainloop()
