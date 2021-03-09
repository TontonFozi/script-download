from tkinter import *
from PIL import Image


def paint_red(im_depart):
    (colones, lines) = im_depart.size
    im_inverse = Image.new("RGB", (colones, lines), (255, 255, 255))

    for c in range(colones):
        for l in range(lines):
            (R, G, B) = im_depart.getpixel((c, l))
            im_inverse.putpixel((c, l), (R, 0, 0))
    return im_inverse


def paint_green(im_depart):
    (colones, lines) = im_depart.size
    im_inverse = Image.new("RGB", (colones, lines), (255, 255, 255))

    for c in range(colones):
        for l in range(lines):
            (R, G, B) = im_depart.getpixel((c, l))
            im_inverse.putpixel((c, l), (0, G, 0))
    return im_inverse


def paint_blue(im_depart):
    (colones, lines) = im_depart.size
    im_inverse = Image.new("RGB", (colones, lines), (255, 255, 255))

    for c in range(colones):
        for l in range(lines):
            (R, G, B) = im_depart.getpixel((c, l))
            im_inverse.putpixel((c, l), (0, 0, B))
    return im_inverse


def paint_special(im_depart):
    (colones, lines) = im_depart.size
    im_inverse = Image.new("RGB", (colones, lines))

    for c in range(colones):
        for l in range(lines):
            if c > colones / 2 and l > lines / 2:
                (R, G, B) = im_depart.getpixel((c, l))
                im_inverse.putpixel((colones - c - 1, lines - l - 1), (0, 0, B))
            elif c < colones / 2 and l > lines / 2:
                (R, G, B) = im_depart.getpixel((c, l))
                im_inverse.putpixel((colones - c - 1, lines - l - 1), (R, 0, 0))
            elif c > colones / 2 and l < lines / 2:
                (R, G, B) = im_depart.getpixel((c, l))
                im_inverse.putpixel((colones - c - 1, lines - l - 1), (0, G, 0))
            elif c < colones / 4 and l > lines / 4:
                im_inverse.putpixel((colones - c - 1, lines - l - 1), (255, 255, 255))
            elif c > colones / 4 and l < lines / 4:
                im_inverse.putpixel((colones - c - 1, lines - l - 1), (255, 255, 255))
    return im_inverse


im = Image.open("image.jpg")

# window
window = Tk()
window.title('Filtres')
window.geometry('1080x720')
window.minsize(850, 650)
window.iconbitmap('LOGO.ico')
window.config(background='#41B77F')

# text
label_title = Label(window, text='Choisissez vos filtres', font=('Courrier', 40), bg='#41B77F', fg='white')
label_title.pack()
label_subtitle = Label(window, text='(cliquez sur un des boutons pour sélectionnez votre filtre)', font=('Courrier', 25),
                       bg='#41B77F', fg='white')
label_subtitle.pack()


# bouton + def
def see_red():
    paint_red(im).show()


red = Button(window, text='Filtre Rouge', font=('Courrier', 25), bg='white', fg='red', command=see_red)
red.pack(pady=50)


def see_blue():
    paint_blue(im).show()


blue = Button(window, text='Filtre Bleu', font=('Courrier', 25), bg='white', fg='blue', command=see_blue)
blue.pack()


def see_green():
    paint_green(im).show()


green = Button(window, text='Filtre Vert', font=('Courrier', 25), bg='white', fg='green', command=see_green)
green.pack(pady="50")


def see_wtf():
    paint_special(im).show()


wtf = Button(window, text='Filtre Spécial', font=('Courrier', 25), bg='white', fg='black', command=see_wtf)
wtf.pack()

press_quit = Button(text="QUIT", font=('Courrier', 15), bg='white', fg='red', command=window.destroy)
press_quit.pack(side="bottom")

window.mainloop()