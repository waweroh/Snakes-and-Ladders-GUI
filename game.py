import tkinter as tk
from PIL import ImageTk, Image
import random


def play_game():

    global ply1_btn, ply2_btn, img_roll

    # Buttons for Players
    # Player 1
    ply1_btn.place(x=1000, y=300)

    # Player 2
    ply2_btn.place(x=1000, y=400)

    # Exit
    exit_btn = tk.Button(
        root,
        text="Exit",
        height=1,
        width=10,
        fg="black",
        bg="blue",
        font=("Cursive", 14, "bold"),
        activebackground="green",
        command=root.destroy,
    )
    exit_btn.place(x=1000, y=50)

    # Dice
    img_roll = Image.open("images/dice.png")
    img_roll = img_roll.resize((70, 70))
    img_roll = ImageTk.PhotoImage(img_roll)
    dice_btn = tk.Button(root, image=img_roll, height=50, width=50)
    dice_btn.place(x=1025, y=150)


def reset_coins():
    global coin1, coin2
    global pos1, pos2

    coin1.place(x=1000, y=580)
    coin2.place(x=1000, y=580)

    pos1, pos2 = 0, 0


def load_dice_images():
    global Dice
    names = [
        "dice1.png",
        "dice2.png",
        "dice3.png",
        "dice4.png",
        "dice5.png",
        "dice6.png",
    ]

    for name in names:
        img_roll = Image.open(f"images/{name}")
        img_roll = img_roll.resize((70, 70))
        img_roll = ImageTk.PhotoImage(img_roll)
        Dice.append(img_roll)


def check_ladder(turn):
    global pos1, pos2
    global ladder

    # No Ladder
    f = 0
    if turn == 1:
        if pos1 in ladder:
            pos1 = ladder[pos1]
            f = 1
        else:
            if pos2 in ladder:
                pos2 = ladder[pos2]
                f = 1

    return f


def check_snake(turn):
    global pos1, pos2
    global snake

    # No Snake
    s = 0
    if turn == 1:
        if pos1 in snake:
            pos1 = snake[pos1]
            s = 1
        else:
            if pos2 in snake:
                pos2 = snake[pos2]
                s = 1

    return s


def roll_dice():
    global Dice
    global turn
    global pos1, pos2
    global ply1_btn, ply2_btn

    r = random.randint(1, 6)
    dice_btn = tk.Button(root, image=Dice[r - 1], height=80, width=80)
    dice_btn.place(x=1025, y=150)

    if turn == 1:
        if (pos1 + r) <= 100:
            pos1 += r
        lad = check_ladder(turn)
        snk = check_snake(turn)
        move_coin(turn, pos1)
        if r != 6 and lad != 1 and snk != 1:
            turn = 2
            ply1_btn.configure(state="disabled")
            ply2_btn.configure(state="normal")
    else:
        if (pos2 + r) <= 100:
            pos2 += r
        lad = check_ladder(turn)
        snk = check_snake(turn)
        move_coin(turn, pos2)
        if r != 6 and lad != 1 and snk != 1:
            turn = 1
            ply1_btn.configure(state="normal")
            ply2_btn.configure(state="disabled")


def move_coin(turn, r):
    global coin1, coin2, Index

    if turn == 1:
        coin1.place(x=Index[r][0], y=Index[r][1])
    else:
        coin2.place(x=Index[r][0], y=Index[r][1])

    is_winner()


def is_winner():
    global pos1, pos2

    if pos1 == 100:
        msg = "Player 1 is the winner"
        lab = tk.Label(
            root, text=msg, height=2, width=20, bg="red", font=("Cursive", 30, "bold")
        )
        lab.place(x=300, y=300)
        reset_coins()
    elif pos2 == 100:
        msg = "Player 2 is the winner"
        lab = tk.Label(
            root, text=msg, height=2, width=20, bg="red", font=("Cursive", 30, "bold")
        )
        lab.place(x=300, y=300)
        reset_coins()


def get_Index():
    global coin1, coin2

    # fmt: off
    Num = [
        100, 99, 98, 97, 96, 95, 94, 93, 92, 91,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
        80, 79, 78, 77, 76, 75, 74, 73, 72, 71,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
        60, 59, 58, 57, 56, 55, 54, 53, 52, 51,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
        40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
    # fmt: on

    row = 40
    i = 0
    for x in range(1, 11):
        col = 70
        for y in range(1, 11):
            Index[Num[i]] = (col, row)
            col = col + 90
            i = i + 1
        row = row + 60

    # print(Index)


# List to store dice images
Dice = []

# Store x & y coordinates of given Num
Index = {}

# initial positions of players
# pos1 = None
# pos2 = None

# Ladder Bottom -> Top
ladder = {4: 25, 21: 39, 29: 74, 43: 76, 63: 80, 71: 89}

# Snakes Head -> Tail
snake = {30: 7, 47: 15, 56: 19, 73: 51, 82: 42, 92: 75, 98: 55}

root = tk.Tk()
root.geometry("1200x800")
root.title("Snakes and Ladders")

F1 = tk.Frame(root, width=1200, height=800, relief="raised")
F1.place(x=0, y=0)

# Set board
img1 = ImageTk.PhotoImage(Image.open("images/snl_board.png"))
Lab = tk.Label(F1, image=img1)
Lab.place(x=50, y=30)

# Player Buttons
ply1_btn = tk.Button(
    root,
    text="Player 1",
    height=1,
    width=10,
    fg="red",
    bg="cyan",
    font=("Cursive", 14, "bold"),
    activebackground="white",
    command=roll_dice,
)
ply2_btn = tk.Button(
    root,
    text="Player 2",
    height=1,
    width=10,
    fg="red",
    bg="orange",
    font=("Cursive", 14, "bold"),
    activebackground="white",
    command=roll_dice,
)

# Player 1 coin
coin1 = tk.Canvas(root, width=40, height=40)
coin1.create_oval(10, 10, 40, 40, fill="cyan")

# Player 2 coin
coin2 = tk.Canvas(root, width=40, height=40)
coin2.create_oval(10, 10, 40, 40, fill="orange")

# Default Player 1 to start
turn = 1

# Keep coins at initial position
reset_coins()

# Get Index of Each Num
get_Index()

# Load Dice Images
load_dice_images()

# Setting Buttons
play_game()

root.mainloop()