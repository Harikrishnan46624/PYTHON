import  pygame, random, sys
pygame.init()

WIDTH = 900
HEIGHT = 600

display = pygame.display.set_mode((WIDTH, HEIGHT))
game_close = False
game_over = False
cell = 30
clock = pygame.time.Clock()
eaten = False
score = 0
pygame.mixer.music.load(r"sanke/SnakeGame-Pygame_music_monkey.mp3")
pygame.mixer.music.play(-1)

def draw_grids():
    for x in range(0, WIDTH, cell):
        for y in range(0, HEIGHT, cell):
            rect = pygame.Rect(x, y, cell, cell)
            pygame.draw.rect(display, '#404040', rect, 1)

def display_score():
    font = pygame.font.SysFont('Tlwg Typist', 30)
    score_font = font.render(f"score: {score}", True, 'white')
    font_pos = score_font.get_rect(center=((WIDTH // 2) - 30, 30))
    display.blit(score_font, font_pos)

def end_screen():
    bg = pygame.image.load(r"sanke/game-over-neon-sign-brick-wall-background-86413715.jpg")
    display.blit(bg, (0, 0))



class Snake:
    def __init__(self) -> None:
        self.x = 300
        self.y = 300
        self.body = [pygame.Rect(self.x, self.y, cell, cell)]
        self.direction = 'none'

    def draw_snake(self):
        for block in self.body:
            pygame.draw.rect(display, 'green', block, 0)

    def update_snake(self):
        self.body.append(pygame.Rect(self.x, self.y, cell, cell))
        self.head = self.body[-1]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move(self):
        if self.direction == 'left':
            self.x -= cell
        if self.direction == 'right':
            self.x += cell
        if self.direction == 'up':
            self.y -= cell
        if self.direction == 'down':
            self.y += cell
        self.update_snake()

    def dead(self):
        global game_over
        for block in self.body[1:]:
            if block.colliderect(snake.body[0]):
                game_over = True
        if self.head.x <= 0 or self.head.x >= WIDTH:
            game_over = True
        if self.head.y <= 0 or self.head.y >= HEIGHT:
            game_over = True

class Fruit:
    def __init__(self) -> None:
        self.x = random.randint(0, WIDTH) // cell * cell
        self.y = random.randint(0, HEIGHT) // cell * cell

    def draw_fruit(self):
        self.body = pygame.Rect(self.x, self.y, cell, cell)
        pygame.draw.rect(display, 'red', self.body)

    def get_random_position(self):
        self.x = random.randint(0, WIDTH) // cell * cell
        self.y = random.randint(0, HEIGHT) // cell * cell


snake = Snake()
fruit = Fruit()

while not game_close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.move_left()
            if event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.move_right()
            if event.key == pygame.K_UP and snake.direction != 'down':
                snake.move_up()
            if event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.move_down()


    display.fill((0,0,0))
    draw_grids()
    snake.draw_snake()
    snake.move()
    fruit.draw_fruit()
    display_score()

    if (snake.head).colliderect(fruit.body):
        eaten = True
        score += 10
        print(score)
    else:
        snake.body.pop(0)

    if eaten:
        fruit.get_random_position()
        eaten = False

    snake.dead()
    if game_over:
        end_screen()
        pygame.mixer.music.stop() 
    

    pygame.display.update()
    clock.tick(10)
