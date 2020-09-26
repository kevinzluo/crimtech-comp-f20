import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {"u": (0, -1), "d": (0, 1), "l": (-1, 0), "r": (1, 0)}  # north is -y


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2)]
    direction = "r"
    dead = False

    # implements feature 9
    moving = False

    def __init__(self):
        pass

    def get_color(self, i):
        hc = (40, 50, 100)
        tc = (90, 130, 255)
        return tuple(map(lambda x, y: (x * (self.l - i) + y * i) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # TODO: See section 3, "Turning the snake".
        # prevent 180 degree turns, as in normal snake
        if DIR[dir] != tuple([-x for x in DIR[self.direction]]):
            self.direction = dir

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        if (0 <= x < 24) and (0 <= y < 24):
            sBody = self.body[1:]
            head = self.body[0]
            # filter all positions equal to head; if any, self collision
            if len(list(filter(lambda pos: pos == head, sBody))) != 0:
                return True
            return False
        return True

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self, grow=False):
        if not (self.moving):
            return
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        if not (grow):
            self.body.pop()
        else:
            self.l += 1
        self.body.insert(0, tuple(map(sum, zip(self.body[0], DIR[self.direction]))))

        if self.collision(*self.body[0]):
            self.kill()

    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn("u")
        if k == pygame.K_DOWN:
            self.turn("d")
        if k == pygame.K_LEFT:
            self.turn("l")
        if k == pygame.K_RIGHT:
            self.turn("r")
        self.moving = True

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)

    # Implements feature 11, "Try again!"
    def reset(self):
        self.moving = False
        self.l = 1
        self.body = [(WIDTH // 2 + 1, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2)]
        self.direction = "r"
        self.dead = False

    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        pass


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)


class Apple(object):
    position = (10, 10)
    color = (233, 70, 29)

    def __init__(self):
        self.place([])

    def place(self, snake):
        self.position = (rand_int(23), rand_int(23))
        if self.position in snake:
            self.position = (rand_int(23), rand_int(23))

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)


def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169, 215, 81) if (x + y) % 2 == 0 else (162, 208, 73)
            pygame.draw.rect(surface, color, r)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0
    grow = False

    font = pygame.font.SysFont("arialttf", 30)
    while True:
        # Implements Feature 10, "incremental difficulty".
        diffScale = (score + 49) ** 0.5 - 6
        clock.tick(8 * diffScale)

        snake.check_events()
        draw_grid(surface)
        snake.move(grow)
        grow = False

        apple.draw(surface)
        snake.draw(surface)
        # TODO: see section 5, "Eating the Apple".
        if snake.body[0] == apple.position:
            score += 1
            print("snake @ apple!")
            apple.place(snake.body)
            grow = True

        screen.blit(surface, (0, 0))
        # TODO: see section 8, "Display the Score"
        textSurface = font.render("Score: %d" % score, False, (0, 0, 0))
        screen.blit(textSurface, (0, 0))

        pygame.display.update()
        if snake.dead:
            print("You died. Score: %d" % score)
            snake.reset()
            score = 0
            # pygame.quit()
            # sys.exit(0)


if __name__ == "__main__":
    main()