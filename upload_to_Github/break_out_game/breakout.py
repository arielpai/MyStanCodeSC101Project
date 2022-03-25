"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Ariel Pai's Assignment 2
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!

    # 計算玩家玩的次數
    t = 1
    while True:
        # 玩家失敗三次就輸了
        if t <= 3:
            pause(FRAME_RATE)
            graphics.ball_move()
            # 如果球掉下去，就回到中心點，並且少一命（t要+1）
            if graphics.ball.y+graphics.ball.width >= graphics.window.height:
                graphics.reset_ball_position()
                t += 1
                graphics.change_score()
        else:
            break



if __name__ == '__main__':
    main()
