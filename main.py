import tkinter as tk
import random

# Constants
WIDTH = 400
HEIGHT = 600
BALL_RADIUS = 20
GRAVITY = 1
BOUNCE_DAMPENER = 0.8

class BouncingBallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click to Drop a Ball")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
        self.canvas.pack()
        
        # Store multiple balls and their velocities
        self.balls = [] # List to store ball object IDs
        self.velocities = [] # List to store y-velocities for each ball

        # Bind mouse click event
        self.canvas.bind("<Button-1>", self.create_ball_on_click)
        
        # Start the animation loop
        self.animate()

    def create_ball(self, x, y):
        """Creates a new ball at the given coordinates."""
        colors = ["green", "red", "blue", "yellow", "orange", "purple", "cyan"]
        color = random.choice(colors)

        ball = self.canvas.create_oval(
            x - BALL_RADIUS,
            y - BALL_RADIUS,
            x + BALL_RADIUS,
            y + BALL_RADIUS,
            fill=color,
            outline="black"
        )
        self.balls.append(ball)
        self.velocities.append(0) # Initial vertical velocity is 0

    def create_ball_on_click(self, event):
        """Event handler for mouse clicks."""
        self.create_ball(event.x, event.y)

    def animate(self):
        # Iterate over all balls using a copy of the list in case it's modified
        for i, ball in enumerate(self.balls):
            # Apply gravity
            self.velocities[i] += GRAVITY
            
            # Move the ball
            self.canvas.move(ball, 0, self.velocities[i])
            
            # Get current position
            pos = self.canvas.coords(ball)
            
            # Check for collision with the bottom
            if pos and pos[3] >= HEIGHT:
                # Place ball exactly at the bottom to prevent it from getting stuck
                self.canvas.coords(ball, pos[0], HEIGHT - (BALL_RADIUS * 2), pos[2], HEIGHT)
                # Reverse and dampen velocity to simulate a bounce
                self.velocities[i] = -self.velocities[i] * BOUNCE_DAMPENER

        # Schedule the next frame
        self.root.after(15, self.animate) # Update roughly 60 times per second

def main():
    root = tk.Tk()
    app = BouncingBallApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
