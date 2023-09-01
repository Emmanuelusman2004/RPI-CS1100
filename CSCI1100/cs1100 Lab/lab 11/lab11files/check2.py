# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:41:12 2022

@author: Emmanuel Usman
"""

import tkinter as tk
import Ball

class BallDraw(object):
    def __init__ (self, parent):
        self.ball=Ball.Ball(8,3,7,7,7,'blue')
        self.wait_time = 100
        self.isstopped = False
        self.maxx = 400
        self.maxy = 400
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack()
        self.chart_1 = tk.Canvas(self.frame,width=self.maxx,height=self.maxy,background="red")
        self.chart_1.grid(row=0, column=0)
        self.chart_1.pack()
        self.restart = tk.Button(self.frame, text="Restart",command=self.restart)
        self.restart.pack()
        self.slow = tk.Button(self.frame, text="Slower", command=self.slower)
        self.slow.pack()
        self.fast = tk.Button(self.frame, text="Faster", command=self.faster)
        self.fast.pack()
        self.quit = tk.Button(self.frame, text="Quit", command=self.quit)
        self.quit.pack()
    def faster(self):
        if self.wait_time > 2:
            self.wait_time /= 2
    def slower(self):
        self.wait_time *= 2
    def restart(self):
        self.isstopped = False
        self.ball_x,self.ball_y = 80,200
        self.animate()
    def quit(self):
        self.isstopped = True
        self.parent.destroy()
    def draw_ball(self):
        self.chart_1.delete(tk.ALL)
        bounding_box=self.ball.bounding_box()
        self.chart_1.create_oval(bounding_box, fill=self.ball.get_color())
        self.chart_1.update()
        self.chart_1.after(self.wait_time)
    def animate(self):
        while self.ball.some_inside(self.maxx, self.maxy) and not self.isstopped:
            self.draw_ball()
            self.ball.move()
            self.ball.check_and_reverse(self.maxx,self.maxy)

if __name__ == "__main__":
    root = tk.Tk()
    bd = BallDraw(root)
    bd.animate()
    root.mainloop()