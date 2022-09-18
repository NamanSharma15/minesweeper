from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
root.configure(bg="black")
root.title("Minesweeper Game")
root.geometry(f'{settings.Width}x{settings.Height}')
root.resizable(False,False)
top_frame = Frame(
    root,
    bg = 'black',
    width  = settings.Width,
    height= utils.height_prc(25)
)
top_frame.place(x=0,y=0)
title = Label(
    top_frame,
    bg = 'Black',
    fg = 'Green',
    text = 'Minesweeper',
    font = ('',50)
)
title.place(x = 400 , y = 20)
left_frame = Frame(
    root,
    width=utils.width_prc(25),
    height=utils.height_prc(75),
    bg='black'
)
left_frame.place(x = 0,y = utils.height_prc(25))
center_frame = Frame(
    root,
    bg = 'black',
    width=utils.width_prc(75),
    height=utils.height_prc(75)
)
center_frame.place(x = utils.width_prc(25),y = utils.height_prc(25))
for i in range(settings.Grid_size):
    for j in range(settings.Grid_size):
        c = Cell(i,j)
        c.create_btn_obj(center_frame)
        c.cell_btn_obj.grid(
            column=i,row=j
        )
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)
Cell.randomize_mines()
root.mainloop()