# tkinter is the GUI library like PyQt
from pymongo import MongoClient
from tkinter import*
from tkinter import ttk, messagebox
import random
from datetime import datetime
import tkinter.messagebox

client = MongoClient(port=27017)
db = client.Books
books = db.books

class Library:
    # as soon as the class is initiated we can assign the window size and other specs
    def __init__(self, root):
        self.root = root
        self.root.title("Library System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="powder blue")

        # creating variables
        MType = StringVar()
        Ref = StringVar()
        Title = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address1 = StringVar()
        Address2 = StringVar()
        Postcode = StringVar()
        Mobileno = StringVar()
        BookId = StringVar()
        BookTitle = StringVar()
        BookType = StringVar()
        Author = StringVar()
        DateBorrow = StringVar()
        dateDue = StringVar()
        SellingPrice = StringVar()
        LateReturnFine = StringVar()
        DateOverDue = StringVar()
        DaysOnLoan = StringVar()
        Prescription = StringVar()

        # function to exit
        def iExit():
            iExit = tkinter.messagebox.askyesno("Library System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        # function to reset
        def ireset():
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            Postcode.set("")
            Mobileno.set("")
            BookId.set("")
            BookTitle.set("")
            BookType.set("")
            Author.set("")
            DateBorrow.set("")
            dateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            self.txtDisplay.delete("1.0", END)

        # function to add
        def iadd():
            # this will push the data into database
            books.insert_one({"Member Type": MType.get(), "Reference No": Ref.get(), "Firstname": Firstname.get(),
                             "Surname": Surname.get(), "Address 1": Address1.get(), "Address 2": Address2.get(),
                             "Mobile No": Mobileno.get()})
            messagebox.showinfo("Successful", "You have added a member")

            # after adding we can clear the fields
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            Postcode.set("")
            Mobileno.set("")

        # function to delete
        def idelete():
            ireset()
            self.txtDisplay.delete("1.0", END)

        # function to display data
        def idisplayData():
            self.txtFrameDetail.insert(END, "\t" + MType.get() + "\t" + Ref.get() + "\t" + Title.get() +
                                       "\t" + Firstname.get() + "\t" + Surname.get() + "\t" + Address1.get() +
                                       "\t" + Address2.get() + "\t" + Postcode.get() + "\t" + BookTitle.get() +
                                       "\t" + DateBorrow.get() + "\t" + DaysOnLoan.get() + "\n")

        def ireceipt():
            self.txtDisplay.insert(END, 'Member Type : \t\t' + MType.get() + "\n")
            self.txtDisplay.insert(END, 'Ref No : \t\t' + Ref.get() + "\n")
            self.txtDisplay.insert(END, 'Title : \t\t' + Title.get() + "\n")
            self.txtDisplay.insert(END, 'Firstname : \t\t' + Firstname.get() + "\n")
            self.txtDisplay.insert(END, 'Surname : \t\t' + Surname.get() + "\n")
            self.txtDisplay.insert(END, 'Address1 : \t\t' + Address1.get() + "\n")
            self.txtDisplay.insert(END, 'Address2 : \t\t' + Address2.get() + "\n")
            self.txtDisplay.insert(END, 'Post Code : \t\t' + Postcode.get() + "\n")
            self.txtDisplay.insert(END, 'Mobile No : \t\t' + Mobileno.get() + "\n")
            self.txtDisplay.insert(END, 'Book ID : \t\t' + BookId.get() + "\n")
            self.txtDisplay.insert(END, 'Book Title : \t\t' + BookTitle.get() + "\n")
            self.txtDisplay.insert(END, 'Author : \t\t' + Author.get() + "\n")
            self.txtDisplay.insert(END, 'Date Borrowed : \t\t' + DateBorrow.get() + "\n")

        # creating Frame
        Mainframe = Frame(self.root)
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, width=350, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle = Label(TitleFrame, width=30, font=('arial', 30, 'bold'),
                              text="\tLibrary System\t", padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(Mainframe, bd=20, width=800, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(Mainframe, bd=20, width=800, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(Mainframe, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Library Membership Information",)
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Book Details",)
        DataFrameRight.pack(side=RIGHT)

        # creating widgets for the left frame
        # label for member type
        self.lbMemberType = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Member Type:", padx=2, pady=2)
        self.lbMemberType.grid(row=0, column=0, sticky=W)
        # dropdown to select
        self.cbMemberType = ttk.Combobox(DataFrameLeft, font=('arial', 12, 'bold'), state='readonly', textvariable=MType
                                         , width=23)
        self.cbMemberType['value'] = ('', 'Student', 'Professor', 'Admin Staff')
        self.cbMemberType.current(0)
        self.cbMemberType.grid(row=0, column=1)

        # label for book id
        self.lbBookId = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Book Id:", padx=2, pady=2)
        self.lbBookId.grid(row=0, column=2, sticky=W)
        # textfield entry for book id
        self.txtBookId = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=BookId)
        self.txtBookId.grid(row=0, column=3)

        # label for reference
        self.lbRef = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Reference No:", padx=2, pady=2)
        self.lbRef.grid(row=1, column=0, sticky=W)
        # textfield entry for reference
        self.txtRef = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Ref)
        self.txtRef.grid(row=1, column=1)

        # label for Book Title
        self.lbBookTitle = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Book Title:", padx=2, pady=2)
        self.lbBookTitle.grid(row=1, column=2, sticky=W)
        # textfield entry for book id
        self.txtBookTitle = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=BookTitle)
        self.txtBookTitle.grid(row=1, column=3)

        # label for title of name
        self.lblTitle = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Title:", padx=2, pady=2)
        self.lblTitle.grid(row=2, column=0, sticky=W)
        # combobox for title of name
        self.cbTitle = ttk.Combobox(DataFrameLeft, state='readonly', font=('arial', 12, 'bold'), width=23, textvariable=Title)
        self.cbTitle['value'] = ('', 'Mr.', 'Miss.', 'Mrs.', 'Dr.', 'Prof.')
        self.cbTitle.current(0)
        self.cbTitle.grid(row=2, column=1)

        # label for author
        self.lblAuthor = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Author:", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        # textfield entry for Author
        self.txtAuthor = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Author)
        self.txtAuthor.grid(row=2, column=3)

        # label for First name
        self.lblFirstName = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="First Name:", padx=2, pady=2)
        self.lblFirstName.grid(row=3, column=0, sticky=W)
        # textfield entry for First name
        self.txtFirstName = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Firstname)
        self.txtFirstName.grid(row=3, column=1)

        # label for date borrowed
        self.lblDateBorrowed = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Date Borrowed:", padx=2, pady=2)
        self.lblDateBorrowed.grid(row=3, column=2, sticky=W)
        # textfield entry for date borrowed
        self.txtDateBorrowed = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=DateBorrow)
        self.txtDateBorrowed.grid(row=3, column=3)

        # label for Surname
        self.lblSurname = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Surname:", padx=2, pady=2)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        # textfield entry for Surname
        self.txtSurname = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Surname)
        self.txtSurname.grid(row=4, column=1)

        # label for DateDue
        self.lblDateDue = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Date Due:", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=2, sticky=W)
        # textfield entry for date due
        self.txtDateDue = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=dateDue)
        self.txtDateDue.grid(row=4, column=3)

        # label for Address1
        self.lblAddress1 = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Address 1:", padx=2, pady=2)
        self.lblAddress1.grid(row=5, column=0, sticky=W)
        # textfield entry for Address1
        self.txtAddress1 = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Address1)
        self.txtAddress1.grid(row=5, column=1)

        # label for days on loan
        self.lblDaysOnLoan = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="days on loan:", padx=2, pady=2)
        self.lblDaysOnLoan.grid(row=5, column=2, sticky=W)
        # textfield entry for Address1
        self.txtDaysOnLoan = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=DaysOnLoan)
        self.txtDaysOnLoan.grid(row=5, column=3)

        # label for Address2
        self.lblAddress2 = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Address 2:", padx=2, pady=2)
        self.lblAddress2.grid(row=6, column=0, sticky=W)
        # textfield entry for Address2
        self.txtAddress2 = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Address2)
        self.txtAddress2.grid(row=6, column=1)

        # label for fine
        self.lblLateReturnFine = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Late return fine:", padx=2, pady=2)
        self.lblLateReturnFine.grid(row=6, column=2, sticky=W)
        # textfield entry fine
        self.txtLateReturnFine = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=LateReturnFine)
        self.txtLateReturnFine.grid(row=6, column=3)

        # label for Postcode
        self.lblPostCode = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Post Code:", padx=2, pady=2)
        self.lblPostCode.grid(row=7, column=0, sticky=W)
        # textfield entry for Postcode
        self.txtPostCode = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Postcode)
        self.txtPostCode.grid(row=7, column=1)

        # label for dateoverdue
        self.lblDateOverDue = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Date Over Due:", padx=2, pady=2)
        self.lblDateOverDue.grid(row=7, column=2, sticky=W)
        # textfield dateoverdue
        self.txtDateOverDue = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=DateOverDue)
        self.txtDateOverDue.grid(row=7, column=3)

        # label for Mobile number
        self.lblMobileNo = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Mobile Number:", padx=2, pady=2)
        self.lblMobileNo.grid(row=8, column=0, sticky=W)
        # textfield entry for Mobile Number
        self.txtMobileNo = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=Mobileno)
        self.txtMobileNo.grid(row=8, column=1)

        # label for selling price
        self.lblSellingPrice = Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Selling Price:", padx=2, pady=2)
        self.lblSellingPrice.grid(row=8, column=2, sticky=W)
        # textfield selling price
        self.txtSellingPrice = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=25, textvariable=SellingPrice)
        self.txtSellingPrice.grid(row=8, column=3)

        # creating  buttons to display,delete,rest and exit
        self.btnDisplay = Button(ButtonFrame, command=idisplayData, text="Display Info", font=('arial', 12, 'bold'),
                                 width=20, bd=4)
        self.btnDisplay.grid(row=0, column=0)

        self.btnDelete = Button(ButtonFrame, text="DELETE", command=idelete, font=('arial', 12, 'bold'), width=20, bd=4)
        self.btnDelete.grid(row=0, column=1)

        self.btnAdd = Button(ButtonFrame, text="ADD", font=('arial', 12, 'bold'), width=20, bd=4, command=iadd)
        self.btnAdd.grid(row=0, column=2)

        self.btnReset = Button(ButtonFrame, text="RESET", font=('arial', 12, 'bold'), width=20, bd=4, command=ireset)
        self.btnReset.grid(row=0, column=3)

        self.btnExit = Button(ButtonFrame, text="EXIT", font=('arial', 12, 'bold'), width=20, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=4)

        # creating widgets for the right frame

        # creating a display for list of books
        self.txtDisplay = Text(DataFrameRight, font=('arial', 12, 'bold'), width=32, height=13, padx=8, pady=20)
        self.txtDisplay.grid(row=0, column=2)
        # creating a ScrollBar
        scrollBar = Scrollbar(DataFrameRight)
        scrollBar.grid(row=0, column=1, sticky='ns')

        # creating a list of books
        ListOfBooks = ["Compiler Design", "Computer Graphics", "Management Information System", "Enterprise Resource Planning", "Theory of Automata",
                       "Programming in Python", "Software Engineering", "Computer Networks"]
        bookList = Listbox(DataFrameRight, width=28, height=12, font=('arial', 12, 'bold'))
        bookList.bind('<<ListBoxSelect>>')
        bookList.grid(row=0, column=0, padx=8)
        scrollBar.config(command=bookList.yview)

        for items in ListOfBooks:
            bookList.insert(END, items)

        # label to display about book
        self.lbllabel=Label(FrameDetail, font=('arial', 10, 'bold'), pady=4,
                            text="Member Type\tReference No.\t Title\t Firstname\t Surname\t Address 1"
                                 "\t Address 2\t post Code\t Book Title\t Date Borrowed\t Days on loan",)
        self.lbllabel.grid(row=0, column=0)

        self.txtDisplay = Text(FrameDetail, font=('arial', 12, 'bold'), width=121, height=4, padx=2, pady=4)
        self.txtDisplay.grid(row=1, column=0)
        

if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
