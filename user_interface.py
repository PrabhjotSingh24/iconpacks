import tkinter as tk
from tkinter import ttk, filedialog

def select_folder(entry_widget):
    folder_path = filedialog.askdirectory()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, folder_path)

def generate_files():
    # Add your logic for generating files here
    # For now, let's print a message
    print("Generating files...")

def open_drawable():
    # Add logic to open the "drawable" folder
    print("Opening drawable folder...")

def open_iconpack():
    # Add logic to open the "iconpack" folder
    print("Opening iconpack folder...")

# Create the main window
root = tk.Tk()
root.title("IconPack Files Generator")
root.geometry("500x500")  # Set window size

# Create a PanedWindow
paned_window = ttk.PanedWindow(root, orient="horizontal")
paned_window.pack(fill="both", expand=True)

# Create the left pane (Icon Preview)
left_pane = ttk.Frame(paned_window)
paned_window.add(left_pane)

# Add a label for Icon Preview
icon_label = tk.Label(left_pane, text="Icon Preview")
icon_label.pack()

# Create the right pane
right_pane = ttk.Frame(paned_window)
paned_window.add(right_pane)

# Create the "From" label and input box
from_label = tk.Label(right_pane, text="From Folder Path:")
from_label.pack()

from_entry = tk.Entry(right_pane, width=40)
from_entry.pack()

# Create the '+' button for "From" folder selection
from_select_button = tk.Button(right_pane, text="+", command=lambda: select_folder(from_entry))
from_select_button.pack()

# Create the "To" label and input box
to_label = tk.Label(right_pane, text="To Folder Path:")
to_label.pack()

to_entry = tk.Entry(right_pane, width=40)
to_entry.pack()

# Create the '+' button for "To" folder selection
to_select_button = tk.Button(right_pane, text="+", command=lambda: select_folder(to_entry))
to_select_button.pack()

# Create the "Generate" button
generate_button = tk.Button(right_pane, text="Generate", command=generate_files)
generate_button.pack()

# Create the "Show Drawable" button
show_drawable_button = tk.Button(right_pane, text="Show Drawable", command=open_drawable)
show_drawable_button.pack()

# Create the "Show IconPack" button
show_iconpack_button = tk.Button(right_pane, text="Show IconPack", command=open_iconpack)
show_iconpack_button.pack()

# Create a dropdown (select) with options
dropdown_label = tk.Label(right_pane, text="Select an option:")
dropdown_label.pack()

options = ["Default", "No All"]
selected_option = tk.StringVar()
selected_option.set(options[0])  # Set default option

dropdown = tk.OptionMenu(right_pane, selected_option, *options)
dropdown.pack()

# Run the Tkinter event loop
root.mainloop()
