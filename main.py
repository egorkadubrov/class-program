from pygame import*
init()

win = display.set_mode((1000, 800))
display.set_caption("Arkanoid")
clock = time.Clock()

platform = Rect(400, 700, 120, 20)
platform_speed = 10

class Ball:
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.dx = speed
        self.dy = speed
        self.radius = radius
        self.color = color
        self.rect = Rect(self.x, self.y, self.radius * 2, self.radius * 2 )
    def reset(self):
        draw.circle(win, self.color, (self.x, self.y), self.radius)

def load_level_map(filename):
    bricks = list()
    with open(filename, 'r') as file:
       lines = [line for line in file.readlines()]

    for row_index, line in enumerate(lines):
        for col_index, char in enumerate(line):
            if char == '#':
               x = col_index * 50
               y = row_index * 50
               brick = Rect(x, y, 50, 50)
               bricks.append(brick)
    return bricks

ball = list()
ball.append(Ball(200, 200, 10, 8, (255, 255, 255)))

lvl = load_level_map('lvl.txt')


while True:
    win.fill((0,0,0))
    for e in event.get():
        if e.type == QUIT:
            quit()

    draw.rect(win, (0, 255, 255), platform)

    for brick in lvl:
       draw.rect(win, (255, 0, 0), brick)
       draw.rect(win, (0, 0, 0), [brick.x, brick.y, brick.w, brick.h], 2)


    for bal in ball:
        bal.reset()


    keys = key.get_pressed()
    if keys[K_d]:
        platform.x += platform_speed
    if keys[K_a]:
        platform.x -= platform_speed



    display.update()
    clock.tick(60)

