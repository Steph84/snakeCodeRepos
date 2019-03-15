import cocos
from cocos.director import director


class HelloCocos(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        label = cocos.text.Label("Hello Cocos", font_name="Times New Roman", font_size=32,
                                 anchor_x="center", anchor_y="center")
        size = director.get_window_size()
        label.position = size[0]/2, size[1]/2
        self.add(label)


if __name__ == "__main__":
    director.init(width=1152, height=576, caption="My cocos window")

    hello_layer = HelloCocos()
    test_scene = cocos.scene.Scene(hello_layer)

    director.run(test_scene)
