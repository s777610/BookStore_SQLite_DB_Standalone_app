"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete Close

"""
from src_OOP.backend import Database
# from tkinter import *
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

# create the database object
database = Database("/Users/hungweicheng/PycharmProjects/BookStore_App/book.db")

class Window(object):


    def __init__(self, window, name):
        self.window = window
        self.window.wm_title(name)

        # class variables are shared by class
        l_title = Label(window, text="Title")
        l_title.grid(row=0, column=0)

        l_author = Label(window, text="Author")
        l_author.grid(row=0, column=2)

        l_year = Label(window, text="Year")
        l_year.grid(row=1, column=0)

        l_isbn = Label(window, text="ISBN")
        l_isbn.grid(row=1, column=2)

        self.title_text = StringVar()
        self.entry_title = Entry(window, textvariable=self.title_text)
        self.entry_title.grid(row=0, column=1)

        self.author_text = StringVar()
        self.entry_author = Entry(window, textvariable=self.author_text)
        self.entry_author.grid(row=0, column=3)

        self.year_text = StringVar()
        self.entry_year = Entry(window, textvariable=self.year_text)
        self.entry_year.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.entry_isbn = Entry(window, textvariable=self.isbn_text)
        self.entry_isbn.grid(row=1, column=3)

        self.list_box = Listbox(window, height=6, width=35)
        self.list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb = Scrollbar(window)
        sb.grid(row=2, column=2, rowspan=6)

        self.list_box.configure(yscrollcommand=sb.set)
        sb.configure(command=self.list_box.yview)

        # if we point to the row, the get_selected_row will be invoked.
        self.list_box.bind('<<ListboxSelect>>', self.get_selected_row)

        b_view_all = Button(window, text="View all", width=12, command=self.view_command)
        b_view_all.grid(row=2, column=3)

        b_search_entry = Button(window, text="Search entry", width=12, command=self.search_command)
        b_search_entry.grid(row=3, column=3)

        b_add_entry = Button(window, text="Add entry", width=12, command=self.add_command)
        b_add_entry.grid(row=4, column=3)

        b_update = Button(window, text="Update", width=12, command=self.update_command)
        b_update.grid(row=5, column=3)

        b_delete = Button(window, text="Delete", width=12, command=self.delete_command)
        b_delete.grid(row=6, column=3)

        b_close = Button(window, text="Close", width=12, command=window.destroy)
        b_close.grid(row=7, column=3)



    # if users point the row
    def get_selected_row(self, event):
        try:
            index = self.list_box.curselection()[0]  # the index of row users point
            self.selected_tuple = self.list_box.get(index)  # to get the row of index
            # the entry form will be fill with element of that row
            self.entry_title.delete(0, END)
            self.entry_title.insert(END, self.selected_tuple[1])
            self.entry_author.delete(0, END)
            self.entry_author.insert(END, self.selected_tuple[2])
            self.entry_year.delete(0, END)
            self.entry_year.insert(END, self.selected_tuple[3])
            self.entry_isbn.delete(0, END)
            self.entry_isbn.insert(END, self.selected_tuple[4])
        except IndexError:
            pass


    def view_command(self):
        self.list_box.delete(0, END)  # from 0 to end
        for row in database.view():
            self.list_box.insert(END, row)

    def search_command(self):
        self.list_box.delete(0, END)
        # backend search() will get the list of tuple, search() takes arg from UGI form
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list_box.insert(END, row)


    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list_box.delete(0, END)
        self.list_box.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.list_box.delete(0, END)
        return self.view_command()

    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list_box.delete(0, END)
        return self.view_command()





bookstore_window = Tk()
Window(bookstore_window, "Book Store Database")
bookstore_window.mainloop()
