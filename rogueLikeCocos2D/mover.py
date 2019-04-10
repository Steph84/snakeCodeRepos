import cocos, main
from pyglet.window import key


class Mover(cocos.actions.Move):
    def step(self, dt):
        super(Mover, self).step(dt)
        vel_x = (main.Main.keyboard[key.RIGHT] - main.Main.keyboard[key.LEFT]) * 500
        vel_y = (main.Main.keyboard[key.UP] - main.Main.keyboard[key.DOWN]) * 500
        self.target.velocity = (vel_x, vel_y)
