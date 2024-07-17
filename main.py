import numpy as np
import tkinter as tk


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()
        self.running = False
        self.direction = (0, 1)
        self.reset()

        # Bind arrow keys for user control
        self.root.bind("<Up>", self.turn_up)
        self.root.bind("<Down>", self.turn_down)
        self.root.bind("<Left>", self.turn_left)
        self.root.bind("<Right>", self.turn_right)

        # Start the game loop
        self.root.after(100, self.game_step)

    def place_food(self):
        while True:
            food_position = (np.random.randint(0, 10), np.random.randint(0, 10))
            if food_position not in self.snake:
                return food_position

    def reset(self):
        self.snake = [(5, 5)]
        self.food = self.place_food()
        self.running = True
        self.direction = (0, 1)
        self.update_canvas()

    def move_snake(self):
        head_x, head_y = self.snake[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if not (0 <= new_head[0] < 10 and 0 <= new_head[1] < 10) or new_head in self.snake:
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.place_food()
        else:
            self.snake.pop()

        self.update_canvas()

    def game_step(self):
        if self.running:
            self.move_snake()
            self.root.after(100, self.game_step)
        else:
            self.game_over()

    def update_canvas(self):
        self.canvas.delete(tk.ALL)
        for (x, y) in self.snake:
            self.canvas.create_rectangle(y * 30, x * 30, (y + 1) * 30, (x + 1) * 30, fill="green")
        fx, fy = self.food
        self.canvas.create_rectangle(fy * 30, fx * 30, (fy + 1) * 30, (fx + 1) * 30, fill="red")

    def game_over(self):
        self.canvas.create_text(150, 150, text="Game Over", fill="red", font=("Arial", 24))

    # Methods for changing direction
    def turn_up(self, event):
        if self.direction != (1, 0):
            self.direction = (-1, 0)

    def turn_down(self, event):
        if self.direction != (-1, 0):
            self.direction = (1, 0)

    def turn_left(self, event):
        if self.direction != (0, 1):
            self.direction = (0, -1)

    def turn_right(self, event):
        if self.direction != (0, -1):
            self.direction = (0, 1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snake Game")
    game = SnakeGame(root)
    root.mainloop()
