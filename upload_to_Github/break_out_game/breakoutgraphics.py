"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.width)/2)

        self.chance = 3
        self.score = GLabel('Chances: '+str(self.chance))
        self.window.add(self.score, x=0, y=self.score.height)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.ball_velocity)  # The ball will get its momentum once the player clicks the mouse.
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(0, brick_rows):
            for j in range(0, brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.color = 'white'
                if i <= 1:
                    self.brick.fill_color = 'red'
                elif i <= 3:
                    self.brick.fill_color = 'orange'
                elif i <= 5:
                    self.brick.fill_color = 'yellow'
                elif i <= 7:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=0+(brick_width+brick_spacing)*j,
                                y=brick_offset+(brick_height+brick_spacing)*i)

    def paddle_move(self, mouse):
        # 不要超過左邊
        if mouse.x <= 0:
            self.paddle.x = 0
        # 不要超過右邊
        elif mouse.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

    def ball_velocity(self, event):
        # the mouseclick only works when the ball is not moving
        if self.ball_is_not_moving():
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def ball_is_not_moving(self):
        if self.__dx == 0 and self.__dy == 0:
            return True

    def ball_move(self):
        self.ball.move(self.__dx, self.__dy)

        # 碰到邊界反彈
        if self.ball.x <= 0 or self.ball.x+self.ball.width >= self.window.width:
            self.__dx *= -1
        if self.ball.y <= 0 or self.ball.y+self.ball.height >= self.window.height:
            self.__dy *= -1

        # 球的右下角
        if self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width):
            obj = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width)

            # 如果碰到paddle
            if self.ball.y+self.ball.width >= self.paddle.y:
                if self.__dy > 0:
                    self.__dy *= -1

            # 如果碰到brick
            else:
                self.__dy *= -1
                self.window.remove(obj)

        # 球的左下角
        elif self.window.get_object_at(self.ball.x, self.ball.y+self.ball.width):
            obj = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.width)

            # 如果碰到paddle
            if self.ball.y+self.ball.width >= self.paddle.y:
                if self.__dy > 0:
                    self.__dy *= -1

            # 如果碰到brick
            else:
                self.__dy *= -1
                self.window.remove(obj)

        # 球的右上角
        elif self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y):
            obj = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)

            # 如果碰到paddle
            if self.ball.y >= self.paddle.y:
                if self.__dy > 0:
                    self.__dy *= -1

            # 如果碰到brick
            else:
                self.__dy *= -1
                self.window.remove(obj)

        # 球的左上角
        elif self.window.get_object_at(self.ball.x, self.ball.y):
            obj = self.window.get_object_at(self.ball.x, self.ball.y)

            # 如果碰到paddle
            if self.ball.y >= self.paddle.y:
                if self.__dy > 0:
                    self.__dy *= -1

            # 如果碰到brick
            else:
                self.__dy *= -1
                self.window.remove(obj)

    def reset_ball_position(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.width) / 2)
        self.__dx = 0
        self.__dy = 0

    def change_score(self):
        if self.chance > 0:
            self.chance -= 1
            self.score.text = 'Chances: '+str(self.chance)















