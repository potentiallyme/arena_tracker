import tkinter as tk
import os
from tkinter import simpledialog, messagebox

filename = './champs.txt' # modify path and name here iyw

def read_champs():
    with open(filename, 'r') as file:
        champs = file.readlines()
    return [champ.strip() for champ in champs]

def write_champs(champs):
    try:
        with open(filename, 'w') as file:
            file.write(f"[ {len(champs) - 2} ]\n*-----*\n")
            file.writelines([f"{champ}\n" for champ in champs[2:]])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving: {e}")

def handle_entry():
    add_name = add_entry.get().title()
    replace_old = replace_entry.get().title()
    replace_new = to_entry.get().title()
    remove_name = remove_entry.get().title()
    champs = read_champs()
    
    if add_name:
        if add_name not in champs:
            champs.append(add_name)
            write_champs(champs)
            messagebox.showinfo("ANOTHER ONE", f"~* {add_name} added *~")
        else:
            messagebox.showwarning("ALREADY DONE", f"!! {add_name} is already completed !!")

    elif replace_old and replace_new:
        if replace_old in champs:
            if replace_new not in champs:
                champs[champs.index(replace_old)] = replace_new
                write_champs(champs)
                messagebox.showinfo("VIEGO R", f"-(( {replace_old} transformed into {replace_new} ))-")
            else:
                messagebox.showwarning("NUH UH", f":: You think this is One for All? ::")
        else:
            messagebox.showwarning("MISINPUT", f"-{{ {replace_old} is hiding elsewhere }}-")
    
    elif remove_name:
        if remove_name in champs:
            champs.remove(remove_name)
            write_champs(champs)
            messagebox.showinfo("WHAT", f"?? {remove_name} was fake ??")
        else:
            messagebox.showwarning("NO CAN DO", f"... {remove_name} isn't here ...")
    
    else:
        messagebox.showwarning("U LOSING IT", "\\_ Might wanna enter something? _/")
    
    clear_entries()


def clear_entries():
    add_entry.delete(0, tk.END)
    replace_entry.delete(0, tk.END)
    to_entry.delete(0, tk.END)
    remove_entry.delete(0, tk.END)
    update_text_display()

def update_text_display():
    champs = read_champs()
    text_box = tk.Text(frame, width=13, height=40, wrap=tk.WORD, font=("Consolas", 12), bg='#222222', fg='white')
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, "\n".join(champs))
    text_box.tag_configure('center', justify='center')
    text_box.tag_add('center', '1.0', 'end')
    text_box.config(state='normal')
    text_box.config(height=40)
    text_box.grid(row=0, column=2, rowspan=10, sticky='nsew', pady=(5, 5), padx=(15, 0))
    text_box.config(state='disabled')

def on_press(event):
    global x, y
    x = event.x
    y = event.y

def on_drag(event):
    dx = event.x - x
    dy = event.y - y
    root.geometry(f'+{root.winfo_x() + dx}+{root.winfo_y() + dy}')

def close_window():
    root.destroy()

## GUI setup
root = tk.Tk()
root.overrideredirect(True)
root.configure(bg='black', bd=5, relief='solid', highlightbackground='#424242', highlightthickness=3)
root.attributes('-topmost', True)

window_width = 350
window_height = 360
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 10
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

custom_title = tk.Label(root, text="COMPLETED CHAMPS", font=('Consolas', 16, 'bold'), fg='white', bg='#222222')
custom_title.pack(fill='both')
custom_title.bind("<ButtonPress-1>", on_press)
custom_title.bind("<B1-Motion>", on_drag)

# main frame
frame = tk.Frame(root, bg='#000000')
frame.pack(fill='both', expand=True, padx=20, pady=20)

# column 0 / setting each manually easier than loop for handle_entry
add_entry = tk.Entry(frame, width=13, font=('Consolas', 12), bg='black',fg='white', insertbackground='white', highlightthickness=1, highlightbackground='#424242', highlightcolor='white')
replace_entry = tk.Entry(frame, width=13, font=('Consolas', 12), bg='black', fg='white', insertbackground='white', highlightthickness=1, highlightbackground='#424242', highlightcolor='white')
to_entry = tk.Entry(frame, width=13, font=('Consolas', 12), bg='black', fg='white', insertbackground='white', highlightthickness=1, highlightbackground='#424242', highlightcolor='white')
remove_entry = tk.Entry(frame, width=13, font=('Consolas', 12), bg='black', fg='white', insertbackground='white', highlightthickness=1, highlightbackground='#424242', highlightcolor='white')

tk.Label(frame, text="ADD", font=('Consolas', 12), bg='black', fg='white').grid(row=0, column=0)
tk.Label(frame, text="REPLACE", font=('Consolas', 12), bg='black', fg='white').grid(row=2, column=0)
tk.Label(frame, text="WITH", font=('Consolas', 12), bg='black', fg='white').grid(row=4, column=0)
tk.Label(frame, text="REMOVE", font=('Consolas', 12), bg='black', fg='white').grid(row=6, column=0)

add_entry.grid(row=1, column=0, pady=(0,25))
replace_entry.grid(row=3, column=0, pady=(0, 5))
to_entry.grid(row=5, column=0, pady=(0, 25))
remove_entry.grid(row=7, column=0, pady=(0, 25))

# column 1
divider = tk.Frame(frame, width=2, bg='#888888', height=700)
divider.grid(row=0, column=1, rowspan=10, padx=(25,10), sticky='ns')

# column 2
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(9, weight=1)

update_text_display()

root.bind('<Return>', lambda event: handle_entry())
root.bind('<Escape>', lambda event: close_window())

root.mainloop()
