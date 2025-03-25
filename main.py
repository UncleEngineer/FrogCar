from ursina import *

app = Ursina()

# Load player model
player = Entity(
    model='assets/models/cartoon_frog.glb',
    scale=1,
    position=(-50, -0.99, 100),
    collider='box'
)

# Ground entity
ground = Entity(
    model='assets/models/house.glb',
    scale=1,
    position=(0, 0, 0),
    collider='mesh'
)

# Tower house entity
tower_house = Entity(
    model='assets/models/tower_house.glb',
    scale=20,
    position=(0, 0, 100),
    collider='box'
)

# Camera setup
camera.parent = player
camera.position = (0, 5, -20)
camera.rotation_x = 5

# Movement variables
velocity = Vec3(0, 0, 0)
acceleration = 0.5
max_speed = 100

def update():
    global velocity

    input_direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized()

    input_direction = camera.forward * input_direction.z + camera.right * input_direction.x
    input_direction.y = 0
    input_direction = input_direction.normalized()

    velocity = lerp(velocity, input_direction * max_speed, time.dt * acceleration)
    player.position += velocity * time.dt

    if velocity.length() > 0.05:
        player.look_at(player.position + velocity)

app.run()
