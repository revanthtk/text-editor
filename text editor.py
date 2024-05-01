#------------------------------------Text editor-----------------------------------------------
import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.textarea = tk.Text(self.root, wrap='word')
        self.textarea.pack(fill='both', expand=True)
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def new_file(self):
        self.textarea.delete('1.0', tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.textarea.delete('1.0', tk.END)
                self.textarea.insert('1.0', content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            content = self.textarea.get('1.0', tk.END)
            with open(file_path, 'w') as file:
                file.write(content)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
#------------------------------------------------Thankyou------------------------------------------------------
