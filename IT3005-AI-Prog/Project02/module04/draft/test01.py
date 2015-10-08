import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.direction = None

        self.canvas = tk.Canvas(width=400, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_oval(190, 190, 210, 210, 
                                tags=("ball",),
                                outline="red", fill="red")

        self.canvas.bind("<Any-KeyPress>", self.on_press)
        self.canvas.bind("<Any-KeyRelease>", self.on_release)
        self.canvas.bind("<1>", lambda event: self.canvas.focus_set())

        self.animate()

    def on_press(self, event):
        delta = {
            "Right": (1,0),
            "Left": (-1, 0),
            "Up": (0,-1),
            "Down": (0,1)
        }
        self.direction = delta.get(event.keysym, None)

    def on_release(self, event):
        self.direction = None

    def animate(self):
        if self.direction is not None:
            self.canvas.move("ball", *self.direction)
        self.after(50, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()