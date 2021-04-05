"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

A basic breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120     # 120 frames per second
NUM_LIVES = 3			    # Number of attempts
graphics = BreakoutGraphics()

def main():
    onmouseclicked(go)

def go(m):
    # A valve to stop onmouseclick() after the first click to start the game, and to run animation loop.
    global NUM_LIVES
    if NUM_LIVES <= 0:
        pass
    else:                           # 我還沒解終止遊戲 贏了的部分!!!!!!!!!!
        while True:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.set_dx()   #撞到牆換方向
            graphics.set_dy()   #撞到天花板換方向
            graphics.bounce()   #撞到block換方向(要在修)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if graphics.ball.y >= graphics.window.height:   #若超出視窗
                graphics.new_ball()
                NUM_LIVES -= 1
                break
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
