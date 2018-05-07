# -----------
"""
@author: Sharon
"""
# -----------

import Tkinter as tk
import random

class SnakeGame():
    def __init__(self):
        self.block = 15

        self.score = 0

        r = random.randrange(201, 350, self.block)
        self.snakeX = [r, r+self.block, r+self.block*2]
        self.snakeY = [r, r, r]

        self.snakeDirection = 'left'
        self.snakeMove = [-1, 0]

        window = tk.Tk()
        window.geometry()
        window.maxsize(600,400)
        window.minsize(600,400)
        window.title("Snake Game")

        self.frame1 = tk.Frame(window, bg = "white", relief = GROOVE, borderwidth = 5)
        self.frame2 = tk.Frame(window, bg = "white", relief = RAISED, borderwidth = 2, height = 40, width = 600)
        self.canvas = tk.Canvas(self.frame1, bg = 'gray', width = 600, height = 360)
        self.score_label = tk.Label(self.frame2, text = "Score: 0")
        
        self.frame1.pack()
        self.frame2.pack(fill = BOTH)
        self.score_label.pack(side = LEFT)
        self.canvas.pack(fill = BOTH)
         
        self.draw_wall()
        self.draw_score()
        self.draw_food()
        self.draw_snake()
        
        self.play()
        
        window.mainloop()

    #  ----------- View Part -----------      
    def draw_wall(self):
        self.canvas.create_line(10, 10, 582, 10, fill = 'blue', width = 5)
        self.canvas.create_line(10, 359, 582, 359, fill = 'blue', width = 5)
        self.canvas.create_line(10, 8, 10, 363, fill = 'blue', width = 5)
        self.canvas.create_line(582, 8, 582, 363, fill = 'blue', width = 5)
        
    def draw_score(self):
        self.score()
        self.score_label.config(self.score_label, text = "Score: " + str(self.score))
        
    def draw_food(self):
        self.canvas.delete("food")
        self.foodx, self.foody = self.random_food()
        self.canvas.create_rectangle(self.foodx, self.foody, self.foodx+self.block, self.foody+self.block, fill = 'red', tags = 'food')

    def draw_snake(self):
        self.canvas.delete("snake")
        x,y=self.snake()
        for i in range(len(x)):
            self.canvas.create_rectangle(x[i], y[i], x[i]+self.block, y[i]+self.block, fill = 'orange', tags = 'snake')

    #  ----------- Model Part -----------  
    def random_food(self):      
        return(random.randrange(11,570,self.block), random.randrange(11,340,self.block))
    
    def snake(self):
        for i in range(len(self.snakeX)-1,0,-1):
            self.snakeX[i] = self.snakeX[i-1]
            self.snakeY[i] = self.snakeY[i-1]
        self.snakeX[0] += self.snakeMove[0]*self.block
        self.snakeY[0] += self.snakeMove[1]*self.block
        return(self.snakeX,self.snakeY)
        
    def score(self):
        self.score += 10
        
    
    #  ----------- Control Part -----------    
    def iseated(self):
        if self.snakeX[0]==self.foodx and self.snakeY[0]==self.foody:
            return True
        else:
            return False
    
    def isdead(self):
        if self.snakeX[0]<8 or self.snakeX[0] >580 or self.snakeY[0]<8 or self.snakeY[0]>350 :
            return True
        
        for i in range(1,len(self.snakeX)):
            if self.snakeX[0]==self.snakeX[i] and self.snakeY[0]==self.snakeY[i] :
                return True
        else:
            return False
    
    def move(self, event):
        if event.char == '<Right>' and self.snakeDirection != 'left':
            self.snakeMove = [1,0]
            self.snakeDirection = "right"
        elif event.char == '<Up>' and self.snakeDirection != 'down':
            self.snakeMove = [0,-1]
            self.snakeDirection = "up"
        elif event.char == '<Left>' and self.snakeDirection != 'right':
            self.snakeMove = [-1,0]
            self.snakeDirection = "left"
        elif event.char == '<Down>' and self.snakeDirection != 'up':
            self.snakeMove = [0,1]
            self.snakeDirection = "down"
        else:
            print event.keycode
            
    def play(self):
        self.canvas.bind('<Key>',self.move)
        self.canvas.focus_set()

        while True:
            if self.isdead():
                self.gameover()
                break
            elif self.iseated():
                self.snakeX[0] += self.snakeMove[0]*self.step
                self.snakeY[0] += self.snakeMove[1]*self.step   
                self.snakeX.insert(1,self.foodx)
                self.snakeY.insert(1,self.foody)

                self.draw_score()
                self.draw_food()
                self.draw_snake()
            else:
                self.draw_snake() 
                self.canvas.after(200)
                self.canvas.update()
        
    def gameover(self):
        self.canvas.unbind('<Key>')
        self.canvas.bind("<Key>",self.restart)
        self.canvas.create_text(270,180,text="Game Over!\n Press any key to continue",font='Helvetica -30 bold',tags='text')

    def restart(self,event):
        self.canvas.delete("food","snake","text")
        self.canvas.unbind('<Key>')

        # to initialize the snake in the range of (191,191,341,341)                
        r=random.randrange(191,191+15*10,self.step)
        self.snakeX=[r,r+self.step,r+self.step*2]
        self.snakeY=[r,r,r]
        
        # to initialize the moving direction
        self.snakeDirection = 'left'  
        self.snakeMove = [-1,0]
        
        # reset the score to zero 
        self.gamescore=-10 
        self.draw_score() 
        
        # to initialize the game (food and snake)
        self.draw_food()
        self.draw_snake()
        
        # to play the game
        self.play()

if __name__ == '__main__':
    SnakeGame()