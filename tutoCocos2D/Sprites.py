import cocos
from cocos.director import director


class Sprite1(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        spr = cocos.sprite.Sprite("pics/heros.png")
        spr.position = 400, 360
        self.add(spr)


class Sprite2(cocos.sprite.Sprite):
    def __init__(self):
        super().__init__("pics/enemy1.png")
        self.position = 640, 360


if __name__ == "__main__":
    director.init(width=1152, height=576, caption="My cocos window")

    spr1_layer = Sprite1()
    spr2 = Sprite2()

    test_scene = cocos.scene.Scene(spr1_layer)
    test_scene.add(spr1_layer)
    test_scene.add(spr2)

    director.run(test_scene)
