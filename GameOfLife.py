import tkinter as tk
from tkinter import font as tkFont
import random
from time import sleep

#Create the root window
root= tk.Tk()
root.title("Simulator")

#Create the canvas within the window
canvas_width = 700
canvas_height = 700
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

start_x1 = 2
start_x2 = 23
start_y1 = 1
start_y2 = 22

coordinates = [(start_x1,start_y1,start_x2,start_y2)]
current_pos = start_x2

#Get the coordinates for the squares of the first row
while current_pos+23 <= canvas_width-200:
    new_x1= coordinates[-1][0] + 23
    new_y1= coordinates[-1][1]
    new_x2= coordinates[-1][2] + 23
    new_y2= coordinates[-1][3]

    coordinates.append((new_x1,new_y1,new_x2,new_y2))
    
    current_pos = new_x2

#Get all coordinates
y_increment = 23

for coords in coordinates:
    if coords[3]+y_increment>=canvas_height-200:
        break
    new_x1 = coords[0]
    new_y1 = coords[1] + y_increment
    new_x2 = coords[2]
    new_y2 = coords[3] + y_increment

    coordinates.append((new_x1,new_y1,new_x2,new_y2))


class cell:
    def __init__ (self,canvas, x1, y1, x2, y2, position):
        self.canvas = canvas
        self.cell = canvas.create_rectangle(x1, y1, x2, y2, fill="black")
        self.state = False
        self.position = position
        canvas.tag_bind(self.cell, "<Button-1>", self.toggle)


    def toggle(self, event=None):
        self.state = not self.state
        new_color = "white" if self.state else "black"
        self.canvas.itemconfig(self.cell, fill=new_color)

    def get_status(self):
        if self.state == True:
            return 'alive'
        else:
            return 'dead'

    def get_left_neighbour(self):
        #A cell has a left neighbour if it is not in the first column
        left_boundary_cells = [int(no_cells_per_row+1)*(i) for i in range(int(no_cells_per_row+1))]
        if self.position in left_boundary_cells:
            return 'no neighbour'
        else:
            return self.position-1

    def get_right_neighbour(self):
        #A cell has a left neighbour if it is not in the first column
        right_boundary_cells = [int((no_cells_per_row)*(i)+no_cells_per_row) for i in range(int(no_cells_per_row+1))]
        if self.position in right_boundary_cells:
            return 'no neighbour'
        else:
            return self.position+1

    def get_above_neighbour(self):
        #A cell has an above neighbour if it is not in the first row
        above_bounary_cells = [i for i in range(int(no_cells_per_row+1))]
        if self.position in above_bounary_cells:
            return 'no neighbour'
        else:
            return self.position-21

    def get_below_neighbour(self):
        #A cell has a below neighbour if it is not in the last row
        below_bounary_cells = below_bounary_cells = [int(((no_cells_per_row-1)*no_cells_per_row)+i+1) for i in range(int(no_cells_per_row+1))] 
        if self.position in below_bounary_cells:
            return 'no neighbour'
        else:
            return self.position+21

    def get_upper_left_diagonal_neighbour(self):
        #A cell has an upper left diagonal neihbour if it is not in the first row and first column
        if (self.get_above_neighbour() != 'no neighbour')  and (self.get_left_neighbour() !='no neighbour'):
            return self.position-22
        else:
            return 'no neighbour'

    def get_upper_right_diagonal_neighbour(self):
        #A cell has an upper right diagonal neihbour if it is not in the first row and last column
        if (self.get_above_neighbour() != 'no neighbour')  and (self.get_right_neighbour() != 'no neighbour'):
            return self.position-20
        else:
            return 'no neighbour'

    def get_lower_left_diagonal_neighbour(self):
        #A cell has a lower left diagonal neihbour if it is not in the last row and first column
        if (self.get_below_neighbour() != 'no neighbour')  and (self.get_left_neighbour() != 'no neighbour'):
            return self.position+20
        else:
            return 'no neighbour'

    def get_lower_right_diagonal_neighbour(self):
        #A cell has a lower right diagonal neihbour if it is not in the last row and last column
        if (self.get_below_neighbour() != 'no neighbour')  and (self.get_right_neighbour() != 'no neighbour'):
            return self.position+22
        else:
            return 'no neighbour'
      
    
    def update_status(self):
        #At this stage, the cell determines whether it is alive or dead and updates itself accordingly
        current_status = self.state

        #We need to get the statuses of each neighbour
        neighbour_info = []
        neighbour_info.append(self.get_left_neighbour())
        neighbour_info.append(self.get_right_neighbour())
        neighbour_info.append(self.get_above_neighbour())
        neighbour_info.append(self.get_below_neighbour())
        neighbour_info.append(self.get_upper_left_diagonal_neighbour())
        neighbour_info.append(self.get_upper_right_diagonal_neighbour())
        neighbour_info.append(self.get_lower_left_diagonal_neighbour())
        neighbour_info.append(self.get_lower_right_diagonal_neighbour())

        neighbour_statuses = []
        for info in neighbour_info:
            if info == 'no neighbour':
                neighbour_statuses.append('no neighbour')
            else:
                neighbour_statuses.append(cell_list[info].state)

        total_alive_neighbours = sum(item for item in neighbour_statuses if isinstance(item, bool))

        #Conditions for survial and death
        if (total_alive_neighbours > 3) and (self.state == False):
            return 0
        elif (total_alive_neighbours > 3) and (self.state == True):
            return 0
        elif (total_alive_neighbours < 2) and (self.state == False):
            return 0
        elif (total_alive_neighbours < 2) and (self.state == True):
            return 0
        elif (total_alive_neighbours in (2,3)) and (self.state == True):
            return 1
        elif (total_alive_neighbours == 3) and (self.state == False):
            return 1
        elif (total_alive_neighbours in (2,3)) and (self.state == False):
            return 0


    def execute_status(self, new_status):
        if new_status == 1:
            self.canvas.itemconfig(self.cell, fill='white')
            self.state = True
        else:
            self.canvas.itemconfig(self.cell, fill='black')
            self.state = False
        
        
        


cell_list = []
coordinate_position = 0
for coords in coordinates:
    a,b,c,d = coords
    cell_list.append(cell(canvas,a,b,c,d,coordinate_position))
    coordinate_position += 1

#Get the number of cells per row
no_cells_per_row = (cell_list[-1].position)**0.5


def play_round():
    new_status = []
    for cell in cell_list:
            new_status.append(cell.update_status())
    for i in range(len(cell_list)):
        cell_list[i].execute_status(new_status[i])
    root.after(200, play_round)

begin_game_btn = tk.Button(canvas, text="Begin", command=play_round)
#tk.Button(canvas, text="Debug ", command=debug_func)
helv36 = tkFont.Font(family='Helvetica', size=30, weight='bold')
begin_game_btn['font'] = helv36
canvas.create_window(600, 50, window=begin_game_btn, height=50)




root.mainloop()
