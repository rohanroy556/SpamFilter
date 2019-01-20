from tkinter import *
from General import *
from tkinter import filedialog
from ClassifierGUI import MailClassifier


class MailViewer(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('800x500')
        self.title('Mail Viewer')
        self.mails = csv_to_list(read_csv('dataset/NaiveBayesResult.csv'))

        # *** Menu ***

        self.menu = Menu(self)
        self.config(menu=self.menu, )

        self.fileMenu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Open File...", command=self.open_browser)
        self.fileMenu.add_command(label="New Classifier...", command=self.new_classifier)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Naive Bayes Classifier", command=lambda: self.show_classifier('Naive Bayes'))
        self.fileMenu.add_command(label="kNN Classifier", command=lambda: self.show_classifier('kNN'))
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.quit)

        self.menu.add_command(label="Home", command=lambda: self.window_visible(self.home_frame))
        self.menu.add_command(label="Inbox", command=lambda: self.window_visible(self.inbox_frame))
        self.menu.add_command(label="Junk", command=lambda: self.window_visible(self.junk_frame))

        # *** Home ***

        self.home_frame = Frame(self)
        self.home_frame.pack(side="top", fill="both", expand=True)
        self.scroll = Scrollbar(self.home_frame, orient=VERTICAL)
        self.select_home = Listbox(self.home_frame, yscrollcommand=self.scroll.set, height=16, selectmode=EXTENDED)
        self.set_fill(self.select_home, 'All')
        self.scroll.config(command=self.select_home.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.select_home.pack(side=LEFT, fill=BOTH, expand=1)
        self.select_home.bind('<Double-1>', self.mail_view)

        # *** Inbox ***

        self.inbox_frame = Frame(self)
        self.inbox_frame.pack(side="top", fill="both", expand=True)
        self.scroll = Scrollbar(self.inbox_frame, orient=VERTICAL)
        self.select_inbox = Listbox(self.inbox_frame, yscrollcommand=self.scroll.set, height=16, selectmode=EXTENDED)
        self.set_fill(self.select_inbox, 'Ham')
        self.scroll.config(command=self.select_inbox.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.select_inbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.inbox_frame.pack_forget()
        self.select_inbox.bind('<Double-1>', self.mail_view)

        # *** Junk ***

        self.junk_frame = Frame(self)
        self.junk_frame.pack(side="top", fill="both", expand=True)
        self.scroll = Scrollbar(self.junk_frame, orient=VERTICAL)
        self.select_junk = Listbox(self.junk_frame, yscrollcommand=self.scroll.set, height=16, selectmode=EXTENDED)
        self.set_fill(self.select_junk, 'Spam')
        self.scroll.config(command=self.select_junk.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.select_junk.pack(side=LEFT, fill=BOTH, expand=1)
        self.junk_frame.pack_forget()
        self.select_junk.bind('<Double-1>', self.mail_view)

    def open_browser(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("CSV Files", "*.csv"), ("all files", "*.*")))
        self.update_mails(filename)
        self.window_visible(self.home_frame)

    def update_mails(self, new_file_name):
        self.mails = csv_to_list(read_csv(new_file_name))
        self.set_fill(self.select_home, 'All')
        self.set_fill(self.select_inbox, 'Ham')
        self.set_fill(self.select_junk, 'Spam')

    def window_visible(self, window_frame):
        self.home_frame.pack_forget()
        self.inbox_frame.pack_forget()
        self.junk_frame.pack_forget()
        window_frame.pack(side="top", fill="both", expand=True)

    def set_fill(self, select_list, select_type):
        select_list.delete(0, END)
        c = 1
        for subject, body, sender, m_type in self.mails:
            if select_type == 'All':
                select_list.insert(END, str(c) + " : " + sender + "  -   " + subject)
            elif m_type == 'Ham' and m_type == select_type:
                select_list.insert(END, str(c) + " : " + sender + "  -   " + subject)
            elif m_type == 'Spam' and m_type == select_type:
                select_list.insert(END, str(c) + " : " + sender + "  -   " + subject)
            c += 1

    def mail_view(self, event):
        item = event.widget.get('active')
        index = int(item.split(':')[0])
        c = 1
        for subject, body, sender, m_type in self.mails:
            if index == c:
                toplevel = Toplevel()
                toplevel.title('Mail')
                Frame(toplevel).pack(fill=X)
                sub = Label(toplevel, text=subject, height=0, width=80, bg='white')
                sub.pack()
                Frame(toplevel).pack(fill=X)
                send = Label(toplevel, text=sender, height=0, width=80, bg='white')
                send.pack()
                Frame(toplevel).pack(fill=X)
                bd = Label(toplevel, text=body, height=0, width=80, bg='white', wraplength=500)
                bd.pack()
                Frame(toplevel).pack(fill=X)
            c += 1

    def new_classifier(self):
        self.destroy()
        MailClassifier()

    def show_classifier(self, classifier):
        if classifier == 'Naive Bayes':
            self.update_mails('dataset/NaiveBayesResult.csv')
        if classifier == 'kNN':
            self.update_mails('dataset/kNNResult.csv')
        self.window_visible(self.home_frame)


if __name__ == "__main__":
    root = MailViewer()
    root.mainloop()
