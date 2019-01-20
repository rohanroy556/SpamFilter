from tkinter import *
from tkinter import filedialog
from NaivesBayesClassifier import naive_bayes_classifer
from NaivesBayesTraining import training
from kNNClassifier import knn_classifier
from Preprocessing import data_cleaning


class MailClassifier(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('500x200')
        self.title('Mail Classifier')

        # *** Menu ***

        self.menu = Menu(self)
        self.config(menu=self.menu, )

        self.menu.add_command(label="Naive Bayes Classifier",
                              command=lambda: self.window_visible(self.naive_bayes_frame))
        self.menu.add_command(label="kNN Classifier", command=lambda: self.window_visible(self.knn_frame))
        self.menu.add_command(label="Data Cleaner", command=lambda: self.window_visible(self.clean_frame))
        self.menu.add_command(label="Exit", command=self.exit)

        # *** Naive Bayes Classifier ***
        # *** Trainer ***

        for i in range(25):
            Frame(self).pack(fill=X)
        self.naive_bayes_frame = Frame(self)
        self.naive_bayes_frame.pack(side="top", fill="both", expand=True)
        self.spamLabel = Label(self.naive_bayes_frame, text="Spam Mails", width=12, bg='white')
        self.spamLabel.grid(row=0, column=0, sticky=W)
        self.spamVar = StringVar()
        self.spam = Entry(self.naive_bayes_frame, width=60, textvariable=self.spamVar)
        self.spam.grid(row=0, column=1, sticky=W)
        self.browser = Button(self.naive_bayes_frame, text="...", width=5, bg='white',
                              command=lambda: self.open_browser(self.spamVar))
        self.browser.grid(row=0, column=2)

        self.hamLabel = Label(self.naive_bayes_frame, text="Ham Mails", width=12, bg='white')
        self.hamLabel.grid(row=1, column=0, sticky=W)
        self.hamVar = StringVar()
        self.ham = Entry(self.naive_bayes_frame, width=60, textvariable=self.hamVar)
        self.ham.grid(row=1, column=1, sticky=W)
        self.browser = Button(self.naive_bayes_frame, text="...", width=5, bg='white',
                              command=lambda: self.open_browser(self.hamVar))
        self.browser.grid(row=1, column=2)

        self.train = Button(self.naive_bayes_frame, text="Train", width=15, bg='white', state=DISABLED,
                            command=lambda: self.classifier_trainer('Train'))
        self.train.grid(row=2, column=1)

        # *** Classify ***

        Frame(self.naive_bayes_frame).grid(row=3, pady=10)
        self.testLabel = Label(self.naive_bayes_frame, text="Test Mails", width=12, bg='white')
        self.testLabel.grid(row=4, column=0, sticky=W)
        self.testVar = StringVar()
        self.test = Entry(self.naive_bayes_frame, width=60, textvariable=self.testVar)
        self.test.grid(row=4, column=1, sticky=W)
        self.browser = Button(self.naive_bayes_frame, text="...", width=5, bg='white',
                              command=lambda: self.open_browser(self.testVar))
        self.browser.grid(row=4, column=2)

        self.nb_classify = Button(self.naive_bayes_frame, text="Classify", width=15, bg='white', state=DISABLED,
                                  command=lambda: self.classifier_trainer('Classify'))
        self.nb_classify.grid(row=5, column=1)

        # *** kNN Classifier ***

        self.knn_frame = Frame(self)
        self.knn_frame.pack(side="top", fill="both", expand=True)
        self.spamLabel = Label(self.knn_frame, text="Spam Mails", width=12, bg='white')
        self.spamLabel.grid(row=0, column=0, sticky=W)
        self.spam = Entry(self.knn_frame, width=60, textvariable=self.spamVar)
        self.spam.grid(row=0, column=1, sticky=W)
        self.browser = Button(self.knn_frame, text="...", width=5, bg='white',
                              command=lambda: self.open_browser(self.spamVar))
        self.browser.grid(row=0, column=2)

        self.hamLabel = Label(self.knn_frame, text="Ham Mails", width=12, bg='white')
        self.hamLabel.grid(row=1, column=0, sticky=W)
        self.ham = Entry(self.knn_frame, width=60, textvariable=self.hamVar)
        self.ham.grid(row=1, column=1, sticky=W)
        self.browser = Button(self.knn_frame, text="...", width=5, bg='white',
                              command=lambda: self.open_browser(self.hamVar))
        self.browser.grid(row=1, column=2)

        self.testLabel = Label(self.knn_frame, text="Test Mails", width=12, bg='white')
        self.testLabel.grid(row=2, column=0, sticky=W)
        self.test = Entry(self.knn_frame, width=60, textvariable=self.testVar)
        self.test.grid(row=2, column=1, sticky=W)
        self.browser = Button(self.knn_frame, text="...", width=5, bg='white',
                              command=lambda: self.open_browser(self.testVar))
        self.browser.grid(row=2, column=2)

        self.knn_classify = Button(self.knn_frame, text="Classify", width=15, bg='white', state=DISABLED,
                                   command=lambda: self.classifier_trainer('kNN'))
        self.knn_classify.grid(row=3, column=1)
        self.knn_frame.pack_forget()

        # *** Data Cleaner ***

        self.clean_frame = Frame(self)
        self.clean_frame.pack(side="top", fill="both", expand=True)
        self.cleanLabel = Label(self.clean_frame, text="Clean Data", width=12, bg='white')
        self.cleanLabel.grid(row=0, column=0, sticky=W)
        self.dataVar = StringVar()
        self.clean = Entry(self.clean_frame, width=60, textvariable=self.dataVar)
        self.clean.grid(row=0, column=1, sticky=W)
        self.browser = Button(self.clean_frame, text="...", width=5, bg='white',
                              command=lambda: self.open_browser(self.dataVar))
        self.browser.grid(row=0, column=2)

        self.cleaner = Button(self.clean_frame, text="Clean", width=15, bg='white', state=DISABLED,
                              command=lambda: data_cleaning(self.dataVar.get()))
        self.cleaner.grid(row=1, column=1)
        self.clean_frame.pack_forget()

    def open_browser(self, var):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("CSV Files", "*.csv"), ("all files", "*.*")))
        var.set(filename)

        if self.spamVar.get() != '' and self.hamVar.get() != '':
            self.train.config(state=NORMAL)
        if self.testVar.get() != '':
            self.nb_classify.config(state=NORMAL)
        if self.spamVar.get() != '' and self.hamVar.get() != '' and self.testVar.get() != '':
            self.knn_classify.config(state=NORMAL)
        if self.dataVar.get() != '':
            self.cleaner.config(state=NORMAL)

    def classifier_trainer(self, c_type):
        if c_type == 'Train':
            training(self.spamVar.get(), self.hamVar.get())
        if c_type == 'Classify':
            naive_bayes_classifer(self.testVar.get())
        if c_type == 'kNN':
            knn_classifier(self.spamVar.get(), self.hamVar.get(), self.testVar.get(), '5')

    def window_visible(self, window_frame):
        self.naive_bayes_frame.pack_forget()
        self.knn_frame.pack_forget()
        self.clean_frame.pack_forget()
        window_frame.pack(side="top", fill="both", expand=True)

    def exit(self):
        self.destroy()
        from MailGUI import MailViewer
        MailViewer()


if __name__ == "__main__":
    trainer = MailClassifier()
    trainer.mainloop()
