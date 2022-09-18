from tkinter import Button, Label
import settings
import random
import ctypes
import sys
class Cell:
    all = []
    cell_count = settings.cell_count
    def __init__(self,x,y,ismine=False):
        self.ismine = ismine
        self.is_opened = False
        self.is_mine_candidte=False
        self.cell_btn_obj = None
        cell_count_label_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)
    def create_btn_obj(self,location):
        btn = Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>',self.left_click_actions)
        btn.bind('<Button-3>',self.right_click_actions)
        self.cell_btn_obj= btn
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text = f"Cells left: {Cell.cell_count}",
            bg = 'black',
            fg = 'white',
            font=("",30)
        )
        Cell.cell_count_label_object = lbl
    def left_click_actions(self,event):
        if self.ismine:
                self.show_mine()
        else:
            if self.surrounded_cells_mine_length==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.cell_show()
            self.cell_show()
            if Cell.cell_count ==settings.minecount:
                ctypes.windll.user32.MessageBoxW(0,"You Have won the Game",'Winner',0)
        self.cell_btn_obj.unbind('<Button-1>')
        self.cell_btn_obj.unbind('<Button-3>')  
    def show_mine(self):
        self.cell_btn_obj.configure(bg = 'red')
        ctypes.windll.user32.MessageBoxW(0,"You clicked on a mine",'Game Over',0)
        sys.exit()
    def get_cell(self,x,y):
        for k in Cell.all:
            if k.x == x and k.y == y:
                return k
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell(self.x - 1,self.y - 1),
            self.get_cell(self.x - 1,self.y),
            self.get_cell(self.x,self.y - 1),
            self.get_cell(self.x - 1,self.y + 1),
            self.get_cell(self.x + 1,self.y - 1),
            self.get_cell(self.x + 1,self.y + 1),
            self.get_cell(self.x + 1,self.y),
            self.get_cell(self.x,self.y + 1)
            ]
        cells = [cell for cell in cells if not cell==None]
        return cells
    @property
    def surrounded_cells_mine_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.ismine:
                counter+=1
        return counter
    def cell_show(self):
        if not self.is_opened:
            Cell.cell_count-=1
            self.cell_btn_obj.configure(bg = 'cyan' , text = f"{self.surrounded_cells_mine_length}")
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text = f"Cells left: {Cell.cell_count}"
                )
        self.is_opened = True
        self.cell_btn_obj.configure(bg='cyan')
    def right_click_actions(self,event):
        if not self.is_mine_candidte:
            self.cell_btn_obj.configure(bg='orange')
            self.is_mine_candidte=True
        else:
            self.cell_btn_obj.configure(bg = 'SystemButtonFace')
            self.is_mine_candidte=False
    @staticmethod
    def randomize_mines():
        picked_Cells = random.sample(
            Cell.all, settings.minecount
        )
        for i in picked_Cells:
            i.ismine = True
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
