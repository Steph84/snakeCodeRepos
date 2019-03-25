import cocos
from cocos.director import director
import pyglet
from pyglet.window import key


class Mover(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 500
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 500
        self.target.velocity = (vel_x, vel_y)
        scroller.set_focus(self.target.x, self.target.y)


class Sprite1(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()

        img = pyglet.image.load("pics/DKCStanding.png")
        img_grid = pyglet.image.ImageGrid(img, 1, 11)

        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1)

        spr = cocos.sprite.Sprite(anim)
        spr.position = 200, 200
        spr.velocity = (0, 0)

        # to make move it
        spr.do(Mover())
        self.add(spr)


class BackgroundLayer(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()

        bg = cocos.sprite.Sprite("pics/background.png")

        # divide by 2 only...
        bg.position = 3072//2, 1536//2

        # define px_width and px_height to stop bg to scroll at the edge
        self.px_width = 3072
        self.px_height = 1536

        self.add(bg)


if __name__ == "__main__":
    director.init(width=1152, height=576, caption="My cocos window")

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    spr1_layer = Sprite1()
    bg_layer = BackgroundLayer()

    scroller = cocos.layer.ScrollingManager()
    scroller.add(bg_layer)
    scroller.add(spr1_layer)

    test_scene = cocos.scene.Scene()
    test_scene.add(scroller)

    director.run(test_scene)
