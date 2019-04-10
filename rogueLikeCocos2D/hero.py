import cocos
from cocos.director import director


class Hero(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        spr = cocos.sprite.Sprite("res/pics/heros.png")
        spr.position = 400, 360
        self.add(spr)
