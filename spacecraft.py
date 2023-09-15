# This is the Spacecraft class

class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'Up':
            self.z += 1
        elif self.direction == 'Down':
            self.z -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'Up':
            self.z -= 1
        elif self.direction == 'Down':
            self.z += 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'Up':
            if self.prev_direction == 'N':
                self.direction = 'W'
            elif self.prev_direction == 'S':
                self.direction = 'E'
            elif self.prev_direction == 'E':
                self.direction = 'N'
            elif self.prev_direction == 'W':
                self.direction = 'S'
        elif self.direction == 'Down':
            if self.prev_direction == 'N':
                self.direction = 'W'
            elif self.prev_direction == 'S':
                self.direction = 'E'
            elif self.prev_direction == 'E':
                self.direction = 'N'
            elif self.prev_direction == 'W':
                self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'
        elif self.direction == 'Up':
            if self.prev_direction == 'N':
                self.direction = 'E'
            elif self.prev_direction == 'S':
                self.direction = 'W'
            elif self.prev_direction == 'E':
                self.direction = 'S'
            elif self.prev_direction == 'W':
                self.direction = 'N'
        elif self.direction == 'Down':
            if self.prev_direction == 'N':
                self.direction = 'E'
            elif self.prev_direction == 'S':
                self.direction = 'W'
            elif self.prev_direction == 'E':
                self.direction = 'S'
            elif self.prev_direction == 'W':
                self.direction = 'N'

    def turn_up(self):
        self.prev_direction = self.direction
        if self.direction == 'N':
            self.direction = 'Up'
        elif self.direction == 'S':
            self.direction = 'Down'
        elif self.direction == 'E':
            self.direction = 'Up'
        elif self.direction == 'W':
            self.direction = 'Up'
        elif self.direction == 'Up':
            self.direction = 'Up'
        elif self.direction == 'Down':
            self.direction = 'Up'

    def turn_down(self):
        self.prev_direction = self.direction
        if self.direction == 'N':
            self.direction = 'Down'
        elif self.direction == 'S':
            self.direction = 'Down'
        elif self.direction == 'E':
            self.direction = 'Down'
        elif self.direction == 'W':
            self.direction = 'Down'
        elif self.direction == 'Up':
            self.direction = 'Down'
        elif self.direction == 'Down':
            self.direction = 'Down'

# I have written out some examples of using the Spacecraft class with a sequence of commands
# Example 1
if __name__ == '__main__':
    spacecraft = Spacecraft(0, 0, 0, 'N')

    commands = ["f", "r", "u", "b", "l"]

    for command in commands:
        if command == "f":
            spacecraft.move_forward()
        elif command == "b":
            spacecraft.move_backward()
        elif command == "l":
            spacecraft.turn_left()
        elif command == "r":
            spacecraft.turn_right()
        elif command == "u":
            spacecraft.turn_up()
        elif command == "d":
            spacecraft.turn_down()

    print("Final Position: ({}, {}, {})".format(spacecraft.x, spacecraft.y, spacecraft.z))
    print("Final Direction: {}".format(spacecraft.direction))

# Example 2
# if __name__ == '__main__':
#     spacecraft = Spacecraft(0, 0, 0, 'N')

#     commands = ["f", "r", "u", "b", "l", "f", "f", "d", "r", "b"]

#     for command in commands:
#         if command == "f":
#             spacecraft.move_forward()
#         elif command == "b":
#             spacecraft.move_backward()
#         elif command == "l":
#             spacecraft.turn_left()
#         elif command == "r":
#             spacecraft.turn_right()
#         elif command == "u":
#             spacecraft.turn_up()
#         elif command == "d":
#             spacecraft.turn_down()

#     print("Final Position: ({}, {}, {})".format(spacecraft.x, spacecraft.y, spacecraft.z))
#     print("Final Direction: {}".format(spacecraft.direction))