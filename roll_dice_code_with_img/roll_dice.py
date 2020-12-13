import tkinter
import random
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("300x300")
root.title("Dice rolling")

blank_line = tkinter.Label(root, text="")
blank_line.pack()

heading_label = tkinter.Label(root, text="dice rolling...", fg="black", bg="light gray", font="mincho 13",width="10",height="1")
heading_label.pack()

dice = ["one.png", "two.png", "three.png", "four.png", "five.png", "six.png"]
dice_randomize = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image_label = tkinter.Label(root, image=dice_randomize)
image_label.image = dice_randomize
image_label.pack(expand=True)


def rolling_dice():
    current_dice = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    image_label.configure(image = current_dice)
    image_label.image = current_dice


button = tkinter.Button(root, text="Roll", fg="white",bg="green",font="mincho 20",command=rolling_dice,width="5",height="1")
button.place(x=150,y=150)
button.pack(expand=True)
root.mainloop()
