import cocos, hero
from cocos.director import director
from pyglet.window import key


class Main:
    def __init__(self):
        self.keyboard = key.KeyStateHandler()
        director.init(caption="RogueOne", autoscale=True, fullscreen=False)
        window_size = director.get_window_size()

        director.window.push_handlers(self.keyboard)

        my_hero = hero.Hero(window_size)

        my_scene = cocos.scene.Scene(my_hero)

        director.run(my_scene)


if __name__ == "__main__":
    Main()
