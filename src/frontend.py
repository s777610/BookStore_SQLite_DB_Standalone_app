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
import src.backend as backend
# from tkinter import *
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

# if users point the row
def get_selected_row(event):
    try:
        global selected_tuple
        index = list_box.curselection()[0]  # the index of row users point
        selected_tuple = list_box.get(index)  # to get the row of index
        # the entry form will be fill with element of that row
        entry_title.delete(0, END)
        entry_title.insert(END, selected_tuple[1])
        entry_author.delete(0, END)
        entry_author.insert(END, selected_tuple[2])
        entry_year.delete(0, END)
        entry_year.insert(END, selected_tuple[3])
        entry_isbn.delete(0, END)
        entry_isbn.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list_box.delete(0, END)  # from 0 to end
    for row in backend.view():
        list_box.insert(END, row)

def search_command():
    list_box.delete(0, END)
    # backend search() will get the list of tuple, search() takes arg from UGI form
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_box.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box.delete(0, END)
    list_box.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    list_box.delete(0, END)
    return view_command()

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box.delete(0, END)
    return view_command()

window = Tk()
window.wm_title("Book Store Database")

l_title = Label(window, text="Title")
l_title.grid(row=0, column=0)

l_author = Label(window, text="Author")
l_author.grid(row=0, column=2)

l_year = Label(window, text="Year")
l_year.grid(row=1, column=0)

l_isbn = Label(window, text="ISBN")
l_isbn.grid(row=1, column=2)

title_text = StringVar()
entry_title = Entry(window, textvariable=title_text)
entry_title.grid(row=0, column=1)

author_text = StringVar()
entry_author = Entry(window, textvariable=author_text)
entry_author.grid(row=0, column=3)

year_text = StringVar()
entry_year = Entry(window, textvariable=year_text)
entry_year.grid(row=1, column=1)

isbn_text = StringVar()
entry_isbn = Entry(window, textvariable=isbn_text)
entry_isbn.grid(row=1, column=3)

list_box = Listbox(window, height=6, width=35)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=sb.set)
sb.configure(command=list_box.yview)

# if we point to the row, the get_selected_row will be invoked.
list_box.bind('<<ListboxSelect>>', get_selected_row)


b_view_all = Button(window, text="View all", width=12, command=view_command)
b_view_all.grid(row=2, column=3)

b_search_entry = Button(window, text="Search entry", width=12, command=search_command)
b_search_entry.grid(row=3, column=3)

b_add_entry = Button(window, text="Add entry", width=12, command=add_command)
b_add_entry.grid(row=4, column=3)

b_update = Button(window, text="Update", width=12, command=update_command)
b_update.grid(row=5, column=3)

b_delete = Button(window, text="Delete", width=12, command=delete_command)
b_delete.grid(row=6, column=3)

b_close = Button(window, text="Close", width=12, command=window.destroy)
b_close.grid(row=7, column=3)




window.mainloop()
