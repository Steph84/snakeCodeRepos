import cocos
from cocos.director import director

class Mover(cocos.actions.Move):
    def step(self, dt):
        print(director)
        super(Mover, self).step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 500
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 500
        self.target.velocity = (vel_x, vel_y)
