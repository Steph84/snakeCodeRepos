import cocos
from cocos.director import director
import pyglet


class Sprite1(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        img = pyglet.image.load("pics/DKCStanding.png")
        img_grid = pyglet.image.ImageGrid(img, 1, 11)

        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1)

        spr = cocos.sprite.Sprite(anim)
        spr.position = 200, 500
        self.add(spr)


if __name__ == "__main__":
    director.init(width=1152, height=576, caption="My cocos window")

    spr1_layer = Sprite1()

    test_scene = cocos.scene.Scene(spr1_layer)
    test_scene.add(spr1_layer)

    director.run(test_scene)
