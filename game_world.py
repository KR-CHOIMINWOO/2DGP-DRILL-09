world = []

def add_object(o):
    world.append(o)

def update():
    for o in world:
        o.update()

def render():
    for o in world:
        o.draw()

def remove_object(o):
    if o in world:
        world.remove(o)
    else:
        print("Object not found in game world.")