from turtle import *
from random import *
from tkinter import *


def triangle(cote):
    down()
    for i in range(3):
        forward(cote)
        left(120)
    up()


def etoile(cote):
    for i in range(8):
        triangle(cote)
        forward(cote)
        right(45)


def couleur():
    number = randint(1, 4)
    if number == 1:
        return "red"
    elif number == 2:
        return "blue"
    elif number == 3:
        return "green"
    elif number == 4:
        return "purple"


def ciel(nb_etoiles):
    bgcolor("black")
    speed(20)
    for i in range(nb_etoiles):
        up()
        x = randint(-300, 300)
        y = randint(-300, 300)
        goto(x, y)
        color(couleur())
        cote = randint(5, 20)
        etoile(cote)
    hideturtle()


# window
window = Tk()
window.title('Etoile')
window.geometry('1080x720')
window.minsize(1080, 720)
window.maxsize(1080, 720)
window.iconbitmap('LOGO.ico')
window.config(background='#41B77F')

# text
label_title = Label(window, text="Choisissez le nombre d'étoile que vous voulez dessiner", font=('Courrier', 30),
                    bg='#41B77F', fg='white')
label_title.pack()

# bouton + def


def action_etoile1():
    ciel(10)


etoile1 = Button(text="10 étoiles", font=('Courrier', 15), bg='white', fg='#41B77F', command=action_etoile1)
etoile1.place(x=500, y=100)


def action_etoile2():
    ciel(25)


etoile2 = Button(text="25 étoiles", font=('Courrier', 15), bg='white', fg='#41B77F', command=action_etoile2)
etoile2.place(x=500, y=180)


def action_etoile3():
    ciel(50)


etoile3 = Button(text="50 étoiles", font=('Courrier', 15), bg='white', fg='#41B77F', command=action_etoile3)
etoile3.place(x=500, y=260)


sublabel_title = Label(window, text="Entrez le nombre d'étoile que vous voulez précisement", font=('Courrier', 30),
                    bg='#41B77F', fg='white')
sublabel_title.place(x=90, y=360)

wtf = Entry(window, font=('Courrier', 25))
wtf.place(x=365, y=420)


def user_star():
    draw = int(wtf.get())
    ciel(draw)


confirm = Button(text="Entrer", font=('Courrier', 15), bg='white', fg='#41B77F', command=user_star)
confirm.place(x=505, y=480)

press_quit = Button(text="QUIT", font=('Courrier', 15), bg='white', fg='red', command=window.destroy)
press_quit.pack(side="bottom")

window.mainloop()

done()
