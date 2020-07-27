import random

class Person:
    def __init__(self, name, position_x, position_y ):
        self.position_x = position_x
        self.position_y = position_y

    def create_path(self, num_steps, step_lenght):
        x_positions = []
        y_positions = []

        

        for _ in range(num_steps):
            x_positions.append(self.position_x)
            y_positions.append(self.position_y)
            select_direction = random.choice([(0, step_lenght * 1), (0,step_lenght *  -1), (step_lenght * 1, 0), (step_lenght * -1, 0)])
            x_step, y_step = select_direction
            self.position_y += y_step
            self.position_x += x_step
        



        return  (x_positions, y_positions, abs(self.position_x), abs(self.position_y))