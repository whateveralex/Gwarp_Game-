from scene import Scene, MagicForest, TheCabin, TheShed, Dungeon, Death, Finished

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play (self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()



class Map(object):

    scenes = {
        'magic_forest' : MagicForest(),
        'the_cabin' : TheCabin(),
        'the_shed' : TheShed(),
        'dungeon' : Dungeon(),
        'death' : Death(),
        'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('magic_forest')
a_game = Engine(a_map)
a_game.play()
