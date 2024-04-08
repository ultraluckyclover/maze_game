from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze")
        self.width = width
        self.height = height

        self.canvas = Canvas(self.root, bg = "white", height=self.height, width=self.width)
        self.canvas_data = self.canvas

        self.canvas.pack(fill = BOTH, expand = 1)
        self.running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def draw_line(self,line,fill_color = "black"):
        self.line.draw(self.canvas, fill_color);

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Closing window...")
    
    def close(self):
        self.running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(self.p1.x,
                           self.p1.y,
                           self.p2.x,
                           self.p2.y,
                           fill = fill_color,
                           width = 2)
        
        canvas.pack(fill = BOTH, expand = 1)   


