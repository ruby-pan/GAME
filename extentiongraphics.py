from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 3  # Initial vertical speed for the ball.
MAX_X_SPEED = 4  # Maximum initial horizontal speed for the ball.
score = 0   # Score on score label.
num = 0 # Counter as to remove the live balls.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=window_width / 2 - paddle_width / 2,
                            y=window_height - paddle_offset)
        self.paddle.filled = 'True'
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Create score label
        self.score_label = GLabel('Score: ' + str(score))
        self.score_label.font = '-20'
        self.window.add(self.score_label, x=0, y=self.window.height)

        # Create lives
        self.lives_1 = GOval(20, 20, x=self.window.width-25, y=self.window.height-25)
        self.lives_1.filled = 'True'
        self.lives_1.fill_color = 'teal'
        self.lives_1.color = 'teal'
        self.window.add(self.lives_1)
        self.lives_2 = GOval(20, 20, x=self.window.width-55, y=self.window.height-25)
        self.lives_2.filled = 'True'
        self.lives_2.fill_color = 'darkturquoise'
        self.lives_2.color = 'darkturquoise'
        self.window.add(self.lives_2)
        self.lives_3 = GOval(20, 20, x=self.window.width-85, y=self.window.height-25)
        self.lives_3.filled = 'True'
        self.lives_3.fill_color = 'turquoise'
        self.lives_3.color = 'turquoise'
        self.window.add(self.lives_3)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=window_width / 2 - ball_radius,
                          y=window_height / 2 - ball_radius)
        self.ball.filled = 'True'
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.reset)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle)

        # Draw bricks
        for i in range(brick_cols):  # 直行
            for j in range(brick_rows):  # 橫列
                self.brick = GRect(brick_width, brick_height, x=i * (brick_width + brick_spacing),
                                   y=brick_offset + j * (brick_spacing + brick_height))
                self.brick.filled = 'True'
                if i + j < 3:
                    self.brick.fill_color = 'azure'
                elif i + j < 5:
                    self.brick.fill_color = 'powderblue'
                elif i + j < 7:
                    self.brick.fill_color = 'paleturquoise'
                elif i + j < 9:
                    self.brick.fill_color = 'turquoise'
                elif i + j < 10:
                    self.brick.fill_color = 'mediumturquoise'
                elif i + j < 12:
                    self.brick.fill_color = 'darkturquoise'
                elif i + j < 14:
                    self.brick.fill_color = 'lightseagreen'
                elif i + j < 16:
                    self.brick.fill_color = 'teal'
                else:
                    self.brick.fill_color = 'darkslategray'
                self.brick.color = 'white'
                self.window.add(self.brick)

    # To let the paddle follow mouse directions
    def reset(self, m):
        if PADDLE_WIDTH / 2 <= m.x <= self.window.width - PADDLE_WIDTH / 2:
            self.paddle.x = m.x - PADDLE_WIDTH / 2
        self.paddle.y = self.window.height - PADDLE_OFFSET

    # Return __dx
    def get_dx(self):
        return self.__dx

    # Return __dy
    def get_dy(self):
        return self.__dy

    # When ball touches walls, change direction
    def set_dx(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx *= -1

    # When ball touches roof, change direction
    def set_dy(self):
        if self.ball.y <= 0:
            self.__dy *= -1

    # When ball disappears from window, add a new ball in the middle
    def new_ball(self):
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2, x= self.window.width / 2 - BALL_RADIUS,
                          y= self.window.height / 2 - BALL_RADIUS)
        self.ball.filled = 'True'
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

    # Remove the live balls
    def renew_lives(self):
        global num
        if num == 0:
            self.window.remove(self.lives_3)
            num += 1
            pass
        elif num == 1:
            self.window.remove(self.lives_2)
            num += 1
            pass
        elif num == 2:
            self.window.remove(self.lives_1)
            num += 1

    # Ball breaks bricks but not the paddle when touched
    def bounce(self):
        global score
        point_a = self.window.get_object_at(self.ball.x, self.ball.y)
        point_b = self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y)
        point_c = self.window.get_object_at(self.ball.x, self.ball.y+ BALL_RADIUS*2)
        point_d = self.window.get_object_at(self.ball.x+ BALL_RADIUS*2, self.ball.y+ BALL_RADIUS*2)
        if point_a is not None and point_b is not None and point_a is not self.score_label and point_b is not self.score_label:
            self.__dy *= -1
            if self.ball.y <= self.window.height / 2:
                self.window.remove(point_a)
                score += 10
                self.score_label.text = 'Score: ' + str(score)
        elif point_c is not None and point_d is not None and point_c is not self.score_label and point_d is not self.score_label:
            self.__dy *= -1
            if self.ball.y <= self.window.height / 2:
                self.window.remove(point_d)
                score += 10
                self.score_label.text = 'Score: ' + str(score)
        elif point_a is not None and point_c is not None and point_c is not self.score_label and point_a is not self.score_label:
            self.__dx *= -1
            if self.ball.y <= self.window.height / 2:
                self.window.remove(point_c)
                score += 10
                self.score_label.text = 'Score: ' + str(score)
        elif point_b is not None and point_d is not None and point_b is not self.score_label and point_d is not self.score_label:
            self.__dx *= -1
            if self.ball.y <= self.window.height / 2:
                self.window.remove(point_b)
                score += 10
                self.score_label.text = 'Score: ' + str(score)

    # End game when all bricks disappeared
    def win(self):
        global score
        if score == 10 * BRICK_COLS * BRICK_ROWS:
            self.win_label = GLabel('You won!!')
            self.win_label.font = '-40'
            self.window.add(self.win_label, x=self.window.width/2, y=self.window.height/2)