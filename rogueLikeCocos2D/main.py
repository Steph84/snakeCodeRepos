import cocos
from cocos.director import director
import hero

if __name__ == "__main__":
    director.init(width=1152, height=576, caption="RogueOne")

    myHero = hero.Hero()

    myScene = cocos.scene.Scene(myHero)

    director.run(myScene)
