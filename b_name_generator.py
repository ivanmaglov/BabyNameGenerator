import random
from tkinter import*

class Generator:

    def __init__(self,master):

        self.bname=StringVar()
        self.gname=StringVar()

        def generateBname():
            self.GBname=random.choice(['Ivan','William','John','Jacob','Christophe','Joshua','Michael','Jayden','Ethan','James',
                                       'Daniel','Angel' ,'Alexander','David','Matthew ','Benjamin','Ryan','Nicholas','Brody',
                                       'Luis','Carlos','Diego','Sebastian','Gabriel','Kevin','Adrian','ivan',
                                       'Mason','James','Isaac','Hunter','Aiden','Samuel','Jesus','Jack','Landon ','Oliver',
                                       'Henry','Lucas','Carter','Owen','Theodore ','Leo','George','Dylan','Toby','Blake ','Dominic '])
            self.bname.set(self.GBname)
            return

        def generateGname():
            self.GGname=random.choice(['Ava','Emma','Sophia','Emily','Isabella','Olivia','Elizabeth','Chloe','Isabella',
                                       'Julia','Grace','Alexis','Mia','Gabriela','Skylar','Penny','Megan','Camila','Victoria',
                                       'Penelope','Lily','Zoey','Lillian','Ariana','Ellie','Bella','Hannah', 'Nora','Hailey','Violet',
                                       'Elena','Alexa','Stella','Caroline','Allison','Melanie', 'Adeline', 'Maya', 'Anna',
                                       'Eva','Eleanor', 'Lucy', 'Willow', 'Valentina', 'Naomi', 'Piper', 'Jade', 'Maria',
                                       'Lydia', 'Ariel', 'Brianna', 'Jasmine', 'Ruby', 'Jasmine', 'Natalia'])
            self.gname.set(self.GGname)

        master.title("Baby Name Generator")
        master.resizable(False,False)

        self.frame_header = Frame(master,bg='cadet blue')
        self.frame_header.pack()

        self.frame2 = Frame(master,bg='cadet blue')
        self.frame2.pack(side=TOP)

        self.lbl_title=Label(self.frame_header,text="Baby Name Generator",  fg='black', font=('arial',35, 'bold'),bg='cadet blue',justify= 'center')
        self.lbl_title.pack()

        self.bnentry = Entry(self.frame_header, state=DISABLED, textvariable=self.bname, bd=20, fg='cadet blue', font=('arial', 40, 'bold'),bg='cadet blue',justify='center')
        self.bnentry.pack(side=RIGHT)

        self.gnentry = Entry(self.frame_header, state=DISABLED, textvariable=self.gname,  bd=20, fg='cadet blue', font=('arial', 40, 'bold'),bg='cadet blue', justify='center')
        self.gnentry.pack(side=LEFT)

        self.gbname = Button(self.frame2, padx=8, width=30, pady=8, bd=8, font=("Arial", 25, 'bold'), text=" Generate girl name ",
                         bg="cadet blue", fg="black",command=generateGname)
        self.gbname.pack(side=LEFT)

        self.ggname = Button(self.frame2, padx=8, width=30, pady=8, bd=8, font=("Arial", 25, 'bold'), text=" Generate boy name ",bg="cadet blue", fg="black", command=generateBname)
        self.ggname.pack(side=RIGHT)

def main():
    root=Tk()
    root.geometry()
    bng=Generator(root)
    root.mainloop()

if __name__ == "__main__":main()
#q=random.choice(['hi','hi2','hi3','ggf'])
#print(q)