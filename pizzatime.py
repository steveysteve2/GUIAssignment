import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.total = 0.0

        self.main_window.geometry("500x250")
        self.main_window.title("Pizza Time!")

        self.top_frame = tkinter.Frame(self.main_window, bg='maroon')
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text='Select toppings: ', bg='maroon', fg='yellow')
        self.prompt_label.pack(side='top')

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.top_frame,text='Pepperoni', variable=self.cb_var1, bg='maroon', fg='white')
        self.cb2 = tkinter.Checkbutton(self.top_frame,text='Mushrooms', variable=self.cb_var2, bg='maroon', fg='white')
        self.cb3 = tkinter.Checkbutton(self.top_frame,text='Meat Lovers', variable=self.cb_var3, bg='maroon', fg='white')

        self.cb1.pack(side='top')
        self.cb2.pack(side='top')
        self.cb3.pack(side='top')

        self.radio_var = tkinter.IntVar()

        self.radio_var.set(2)

        self.prompt_label2 = tkinter.Label(self.top_frame, text='\nSelect crust: ', bg='maroon', fg='yellow')
        self.prompt_label2.pack(side='top')

        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Thin Crust', 
                                       variable=self.radio_var, value = 1, bg='maroon', fg='white')
        
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Thick Crust', 
                                       variable=self.radio_var, value = 2, bg='maroon', fg='white')

        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Gluten-Free', 
                                       variable=self.radio_var, value = 3, bg='maroon', fg='white')
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.prompt_label = tkinter.Label(self.bottom_frame, text='Enter name for the order: ')
        self.name_entry = tkinter.Entry(self.bottom_frame, width=10)

        self.prompt_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.ok_button = tkinter.Button(self.bottom_frame, text='Submit',command=self.cal_order, bg='maroon')
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit',command=self.main_window.destroy, bg='maroon')
        
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def cal_order(self):
        message = "You have selected: \n"

        self.crust = self.radio_var.get()

        if self.crust == 1:
            message += 'Thin Crust with \n'
            self.total += 8.25
            
        elif self.crust == 2:
            message += 'Thick Crust with \n'
            self.total += 10.25
            
        else:
            message += 'Gluten-Free with \n'
            self.total += 9.25

        if self.cb_var1.get() == 1:
            message += 'Pepperoni\n'
            self.total += 1.0
            
        if self.cb_var2.get() == 1:
            message += 'Mushrooms\n'
            self.total += 1.5
            
        if self.cb_var3.get() == 1:
            message += 'Meat Lovers\n'
            self.total += 2.0

        if self.total > 0:
            message += (f"\nTotal: ${self.total}")
        else:
            message += "Please enter valid order!"
            
        tkinter.messagebox.showinfo(f'Name: {self.name_entry}\nTotal:', message)


mygui = MyGUI()