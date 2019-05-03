import cocos
from cocos.director import director
from pyglet.window import key

class Mover(cocos.actions.Move):
    def step(self, dt):
        super(Mover, self).step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 500
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 500
        self.target.velocity = (vel_x, vel_y)

class Hero(cocos.layer.Layer):
    def __init__(self, window_size):
        super().__init__()
        spr = cocos.sprite.Sprite("res/pics/heros.png")
        spr.position = (window_size[0]/2, window_size[1]/4)
        spr.velocity = (0, 0)
        spr.do(Mover())
        self.add(spr)

# class Main:
#     def __init__(self):
#         director.init(caption="RogueOne", autoscale=True, fullscreen=False)

#         self.keyboard = key.KeyStateHandler()
#         director.window.push_handlers(self.keyboard)

#         window_size = director.get_window_size()
#         my_hero = Hero(window_size)
#         my_scene = cocos.scene.Scene(my_hero)

#         director.run(my_scene)

# if __name__ == "__main__":
#     Main()

if __name__ == "__main__":
    director.init(caption="RogueOne", autoscale=True, fullscreen=False)

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    window_size = director.get_window_size()
    my_hero = Hero(window_size)
    my_scene = cocos.scene.Scene(my_hero)

    director.run(my_scene)
