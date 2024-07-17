# Snake Game

This is a simple implementation of the classic Snake game using Python and Tkinter.

## Features

- Control the snake using the arrow keys.
- The snake grows longer when it eats the food.
- The game ends if the snake runs into the wall or itself.
- A "Game Over" message is displayed when the game ends.

## Requirements

- Python 3.x
- Tkinter
  
## How to Play

- Use the arrow keys to change the direction of the snake.
- The snake will move continuously in the direction it is facing.
- Guide the snake to the red food to make it grow longer.
- Avoid running into the walls or the snake's own body.

## Code Explanation

### `SnakeGame` Class

- **`__init__(self, root)`**: Initializes the game, sets up the canvas, binds the keys, and starts the game loop.
- **`place_food(self)`**: Places the food at a random location on the grid.
- **`reset(self)`**: Resets the game state.
- **`move_snake(self)`**: Moves the snake in the current direction and checks for collisions.
- **`game_step(self)`**: The main game loop that moves the snake and updates the game state.
- **`update_canvas(self)`**: Updates the canvas to reflect the current game state.
- **`game_over(self)`**: Displays the "Game Over" message.
- **Direction change methods (`turn_up`, `turn_down`, `turn_left`, `turn_right`)**: Change the direction of the snake based on user input
