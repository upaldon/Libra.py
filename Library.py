import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow
import json
import os

DATA_FILE = "bibliotheque_data.json"

#fonction de sauvegarde / chargement Json

def charger_donnees():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                # Vérifie que les données ont la structure correcte
                if isinstance(data, dict) and "books" in data and "lend_list" in data:
                    return data
                else:
                    print("Le fichier JSON a une structure incorrecte. Réinitialisation des données.")
                    return {"books": [], "lend_list": []}
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Erreur de décodage JSON: {e}")
            return {"books": [], "lend_list": []}
    else:
        return {"books": [], "lend_list": []}

def sauvegarder_donnees(books, lend_list) :
    with open (DATA_FILE, "w") as f:
        json.dump({"books" :books, "lend_list" : lend_list}, f,indent=4)
class Library :
    def __init__(self, master):
        self.master= master
        self.master.title("📚 📕 📘 LIBRARY SYSTEM 📕 📘 📚")
        self.master.geometry("600x600")
        self.master.config(bg='#708090')
         #  Chargement de l'image de fond
        image = Image.open("D:/Tuto/bilio.jpg") # Mets ici ton chemin d'image
        image = image.resize((600, 600))
        self.bg_image = ImageTk.PhotoImage(image)

        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
       
        #chargement des donnees
        data = charger_donnees()
        self.books = data.get("books", [])
        self.lend_list= data.get("lend_list", [])
        
         # Champs de login
        self.login_label = tk.Label(self.master, text="📚📖Library System📖📚", font=("Helvetica", 16), bg='#708090')
        self.username_label = tk.Label(self.master, text="Username👤", font=("Helvetica", 12), bg='#708090')
        self.username_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.password_label = tk.Label(self.master, text="Password🔑", font=("Helvetica", 12), bg='#708090')
        self.password_entry = tk.Entry(self.master, font=("Helvetica", 12), show="*")
        self.login_button = tk.Button(self.master, text="Login🔐", command=self.login)
        self.registrer_button = tk.Button(self.master, text="Register👤➕", command=self.registrer)

        # Ajout des widgets au canvas
        self.canvas.create_window(300, 50, window=self.login_label)
        self.canvas.create_window(300, 120, window=self.username_label)
        self.canvas.create_window(300, 150, window=self.username_entry)
        self.canvas.create_window(300, 190, window=self.password_label)
        self.canvas.create_window(300, 220, window=self.password_entry)
        self.canvas.create_window(250, 270, window=self.login_button)
        self.canvas.create_window(350, 270, window=self.registrer_button)

        
        self.username= "Aldon"
        self.password ="212219"
        self.librarians = [["Aldon","212219"]]

    def login(self) :
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        for librarian in self.librarians:
            if self.username == librarian [0] and self.password == librarian [1]:
                self.username_entry.delete(0, tk.END)
                self.username_entry.delete(0, tk.END)
                self.login_label.destroy()
                self.username_label.destroy()
                self.username_entry.destroy()
                self.password_label.destroy()
                self.password_entry.destroy()
                self.login_button.destroy()
                self.registrer_button.destroy()
                self.canvas.destroy()  # Supprime le canvas avec l'image de fond
                self.library_management_screen()
                return
        messagebox.showerror("Error","Invalid username or password")        

    def registrer(self) :
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.librarians.append([self.username, self.password])
        self.username_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)
    
    def library_management_screen(self) :
        #label pour ajouter un livre
        self.add_book_label = tk.Label(self.master, text="Add Book➕📖",font=("Helvetica", 20),bg='#708090', fg='white')
        self.add_book_label.pack()
        self.add_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.add_book_entry.pack()
        self.add_book_button= tk.Button(self.master, text="Add Book➕",command=self.add_book, font=("Helvetica",12))
        self.add_book_button.pack()
        #label pour supprimer un livre
        self.remove_book_label= tk.Label(self.master, text="Remove Book🗑️📖", font=("helvetica",16),bg='#708090',fg='white')
        self.remove_book_label.pack()
        self.remove_book_entry= tk.Entry(self.master, font=("Heveltica", 12))
        self.remove_book_entry.pack()
        self.remove_book_button=tk.Button(self.master, text="Remove book🗑️", command=self.remove_book, font=("Heveltica", 12))
        self.remove_book_button.pack()
         #label pour voir les livres
        self.view_book_button= tk.Button(self.master, text="View book📕📘", command=self.view_book, font=("Heveltica",12))
        self.view_book_button.pack()
        #label d'emprunter un livre
        self.issue_book_label=tk.Label(self.master, text="Issue book🔄📚",font=("Helvetica",20), bg='#708090',fg='white')
        self.issue_book_label.pack()
        self.issue_book_entry=tk.Entry(self.master, font=("Heveltica", 12))
        self.issue_book_entry.pack()
        self.issue_book_button=tk.Button(self.master, text="Issue book🔄", command=self.issue_book, font=("Heveltica",12))
        self.issue_book_button.pack()
        
        #pour voir liste des livres empruntes
        self.view_lent_books_button = tk.Button(self.master, text="View Lent Books📝", command=self.view_lent_books, font=("Helvetica", 12))
        self.view_lent_books_button.pack()

        #pour remettre un livre
        self.return_book_label = tk.Label(self.master, text="Return Book🔄📖", font=("Helvetica", 16), bg='#708090', fg='white')
        self.return_book_label.pack()
        self.return_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.return_book_entry.pack()
        self.return_book_button = tk.Button(self.master, text="Return Book🔄📖", command=self.return_book, font=("Helvetica", 12))
        self.return_book_button.pack()


    def add_book(self) :
        book = self.add_book_entry.get()
        if book :
            self.books.append(book)
            sauvegarder_donnees(self.books, self.lend_list)
            messagebox.showinfo("Success✅", "Book added successfull➕📖")
            self.add_book_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("champ vide", "please enter name books📕")


    def remove_book(self) :
        input_val = self.remove_book_entry.get()
        try:
            index = int(input_val) -1 #car -1 on affiche a partir de 1
            if 0 <= index < len(self.books):
                book = self.books.pop(index)
                sauvegarder_donnees(self.books, self.lend_list)
                messagebox.showinfo("Success✅", f"🗑️📖Book removed successfull : {book}")
            else : 
                messagebox.showerror("Error","Invalid number.")
        except ValueError:
            messagebox.showerror("Error❌","Please enter a valid number")

        self.remove_book_entry.delete(0, tk.END)
    def view_book(self):
        if not self.books :
            messagebox.showinfo("Books", "No Books Available")
            return
        message = "\n".join([f"{i+1}. {book}" for i, book in enumerate(self.books)])
        messagebox.showinfo("Books📕📘", message)    
        
    def issue_book(self):
        book = self.issue_book_entry.get()
        if book in self.books :
            self.lend_list.append(book)
            self.books.remove(book)
            sauvegarder_donnees(self.books, self.lend_list)
            messagebox.showinfo("Success✅", "Book issued successfully✅📘")
        else:
            messagebox.showerror("Error","Book not found")
        self.issue_book_entry.delete(0, tk.END)


    def view_lent_books(self):
        if not self.lend_list:
            messagebox.showinfo("Lent books", "No books issue.")
            return
        message = "\n".join([f"{i+1}.{book}" for i, book in enumerate (self.lend_list)]) #creer la liste des livres empruntes
        messagebox.showinfo("Lent books🔄📚", message)

    def return_book(self):
        book = self.return_book_entry.get()  # Récupérer le livre à retourner
        if book in self.lend_list:
            self.lend_list.remove(book)  # Retirer le livre de la liste des livres empruntés
            self.books.append(book)  # Ajouter le livre à la liste des livres disponibles
            sauvegarder_donnees(self.books, self.lend_list)  # Sauvegarder les données
            messagebox.showinfo("Success", f"Book '{book}' returned successfully 📚✅")
        else:
            messagebox.showerror("Error", "Book not found in lent books")  # Si le livre n'est pas trouvé dans la liste des empruntés
    
        self.return_book_entry.delete(0, tk.END)  # Réinitialise le champ de texte

if __name__ == "__main__"  :
    root = tk.Tk()   
    app = Library(root)   
    root.mainloop()


