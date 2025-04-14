import tkinter as tk
import random
from time import sleep

#Create the root window
root= tk.Tk()
root.title("Simulator")

#Create the canvas within the window
canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

#Add a rectangle to the canvas
#The first two coordinates are where the top left corner starts
#The last two coordinates are where the bottom right corner starts
#canvas.create_rectangle(2, 24, 23, 46, fill="blue")
#canvas.create_rectangle(25, 1, 46, 22, fill="red")

##def agents_overlap(agent1, agent2):
##    #These get the bounding box positions of the agents on the screen
##    x1,y1,x2,y2 = agent1.canvas.bbox(agent1.rect)
##    a1,b1,a2,b2 = agent2.canvas.bbox(agent2.rect)
##
##    #We then check if the bouding boxes overlap at all
##    #This will return true or false
##    return (
##        x1 < a2 and x2 > a1 and
##        y1 < b2 and y2 > b1
##    )
##
##class Agent:
##    def __init__(self, canvas):
##        self.canvas = canvas
##        self.x = 100
##        self.y = 100
##        self.size = random.randint(5,100)
##        self.rect = canvas.create_rectangle( (self.x,self.y,self.x+self.size,self.y+self.size))
##
##    def move(self):
##        #Defines how the agent moves
##        dx = random.randint(-1,1)
##        dy = random.randint(-1,1)
##        self.canvas.move(self.rect, dx, dy) 
##
##        self.x += dx
##        self.y += dy
##
##    def get_pos(self):
##        #Gets the agents current position
##        return self.x, self.y
##
###Create the agents
##agent = Agent(canvas)
##agent2 = Agent(canvas)

##def update():
##    agent.move()
##    agent2.move()
##    
##    if agents_overlap(agent, agent2):
##        #print("Collision detected!")
##        canvas.itemconfig(agent.rect, fill="red")
##        canvas.itemconfig(agent2.rect, fill="red")
##    else:
##        canvas.itemconfig(agent.rect, fill="blue")
##        canvas.itemconfig(agent2.rect, fill="blue")
##    #print(agent.get_pos())
##    root.after(50, update)

start_x1 = 2
start_x2 = 23
start_y1 = 1
start_y2 = 22

coordinates = [(start_x1,start_y1,start_x2,start_y2)]
current_pos = start_x2

#Get the coordinates for the squares of the first row
while current_pos+23 <= canvas_width:
    new_x1= coordinates[-1][0] + 23
    new_y1= coordinates[-1][1]
    new_x2= coordinates[-1][2] + 23
    new_y2= coordinates[-1][3]

    coordinates.append((new_x1,new_y1,new_x2,new_y2))
    
    current_pos = new_x2

#Get all coordinates
y_increment = 23


for coords in coordinates:
    if coords[3]+y_increment>=canvas_height:
        break
    new_x1 = coords[0]
    new_y1 = coords[1] + y_increment
    new_x2 = coords[2]
    new_y2 = coords[3] + y_increment

    coordinates.append((new_x1,new_y1,new_x2,new_y2))


class cell:
    def __init__ (self,canvas, x1, y1, x2, y2):
        self.canvas = canvas
        self.cell = canvas.create_rectangle(x1, y1, x2, y2, fill="black")
        self.state = False
        canvas.tag_bind(self.cell, "<Button-1>", self.toggle)

    def toggle(self, event=None):
        self.state = not self.state
        new_color = "white" if self.state else "black"
        self.canvas.itemconfig(self.cell, fill=new_color)

    
cell_list = []
for coords in coordinates:
    a,b,c,d = coords
    cell_list.append(cell(canvas,a,b,c,d))
##def draw_cells(index=0):
##    if index < len(coordinates):
##        x1, y1, x2, y2 = coordinates[index]
##        cell_list.append(cell(canvas, x1, y1, x2, y2))
##        # Schedule the next one after 200ms
##        root.after(200, draw_cells, index + 1)
##
##draw_cells()

def update():
    pass

update()  # start the loop

root.mainloop()
