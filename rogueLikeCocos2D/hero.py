import cocos, main

class Hero(cocos.layer.Layer):
    def __init__(self, window_size):
        super().__init__()

        spr = cocos.sprite.Sprite("res/pics/heros.png")
        spr.position = (window_size[0]/2, window_size[1]/4)
        spr.velocity = (0, 0)
        spr.do(main.Mover())
        self.add(spr)
