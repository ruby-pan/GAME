
from campy.gui.events.timer import pause
from extentiongraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120     # 120 frames per second
NUM_LIVES = 3			    # Number of attempts
graphics = BreakoutGraphics()

def main():
    onmouseclicked(go)

def go(m):
    # A valve to stop onmouseclick() after the first click to start the game, and to run animation loop
    global NUM_LIVES
    if NUM_LIVES <= 0:
        pass
    else:
        while True:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.set_dx()
            graphics.set_dy()
            graphics.bounce()
            graphics.win()
            if graphics.ball.y >= graphics.window.height:   
                graphics.new_ball()
                NUM_LIVES -= 1
                graphics.renew_lives()
                break
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
