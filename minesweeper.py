import random
import tkinter


def print_field_beautiful(field):
    for i in range(1, len(field)):
        for j in range(1, len(field[i])):
            if field[i][j] != -1:
                print("%2d" % (field[i][j]), end=' ')
        print()


def how_many_surrounding(x, y):
    count = 0
    delta_x = -1
    delta_y = -1
    for i in range(3):
        delta_x = -1
        for j in range(3):
            if field[y + delta_y][x + delta_x] == -2:
                count += 1
            delta_x += 1
        delta_y += 1
    return count


def open_cell(button, y, x, button_in_field):
    if field[y][x] != None:
        button.config(text=field[y][x])
        field[y][x] = None
    if button_in_field == 0:
        delta_x = -1
        delta_y = -1
        for i in range(3):
            delta_x = -1
            for j in range(3):
                if (field[y + delta_y][x + delta_x] != None and 
                    field[y + delta_y][x + delta_x] != -1):
                    open_cell(buttons[y + delta_y - 1][x + delta_x - 1], y + delta_y, 
                              x + delta_x, field[y + delta_y][x + delta_x])
                delta_x += 1
            delta_y += 1
    elif button_in_field == -2:
        for i in range(len(buttons)):
            for j in range(len(buttons[0])):
                open_cell(buttons[i][j], i + 1, j + 1, field[i + 1][j + 1])


def click(event):
    i = 0
    while i < len(buttons) and event.widget not in buttons[i]:
        i += 1
    index = buttons[i].index(event.widget)
    open_cell(event.widget, i + 1, index + 1, field[i + 1][index + 1])


def flag(event):
    if event.widget.cget("text") == "":
        event.widget.config(text="✅")
    else:
        event.widget.config(text="")

width = 9
height = 9
count_of_mines = 10
# 9 * 9 - 10
# 16 * 16 - 40
# 30 * 16 - 99
width_cell = 30
width_canvas = width_cell * (width + 2)
height_canvas = width_cell * (height + 2)
field = ([[-1] * (width + 2)] + 
        [[-1] + [0 for i in range(width)] + [-1] for j in range(height)] + 
        [[-1] * (width + 2)])
for i in range(count_of_mines):
    x = random.randint(1, width)
    y = random.randint(1, height)
    while field[y][x] != 0:
        x = random.randint(1, width)
        y = random.randint(1, height)
    field[y][x] = -2
for i in range(1, height + 1):
    for j in range(1, width + 1):
        if field[i][j] != -2:
            field[i][j] = how_many_surrounding(j, i)
print_field_beautiful(field)

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=width_canvas, height=height_canvas)
canvas.pack()
buttons = [[0 for i in range(width)] for j in range(height)]
for i in range(1, height + 1):
    for j in range(1, width + 1):
        buttons[i - 1][j - 1] = tkinter.Button(highlightbackground="black")
        buttons[i - 1][j - 1].place(x=j * width_cell, y=i * width_cell, 
                                    height=width_cell, width=width_cell)
        buttons[i - 1][j - 1].bind("<Button-1>", click)
        buttons[i - 1][j - 1].bind("<Button-3>", flag)
root.mainloop()
