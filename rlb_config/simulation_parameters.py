
# ------------- Maps
sim_map_image_path = "/home/vguillet/ros2_ws/src/rlb_tools/rlb_tools/Caylus_map/Caylus_map.png"
paths_image_path = "/home/vguillet/ros2_ws/src/rlb_tools/rlb_tools/Caylus_map/Caylus_map_paths.png"
hard_obstacles_image_path = "/home/vguillet/ros2_ws/src/rlb_tools/rlb_tools/Caylus_map/Caylus_map_hard_obstacles.png"
dense_vegetation_img_path = "/home/vguillet/ros2_ws/src/rlb_tools/rlb_tools/Caylus_map/Caylus_map_dense_vegetation.png"
light_vegetation_img_path = "/home/vguillet/ros2_ws/src/rlb_tools/rlb_tools/Caylus_map/Caylus_map_light_vegetation.png"

images_shape = (911, 1000)

ref_1_pixel =(7, 193)
ref_1_latlon = (44.27303, 1.72456)

ref_2_pixel = (871, 908)
ref_2_latlon = (44.276598, 1.730598)

# ------------- Obstacles signal blocking probabilities
hard_obstacles_signal_blocking_prob = 1.
dense_vegetation_signal_blocking_prob = .0
light_vegetation_signal_blocking_prob = .0


# ------------- Turtle emulator
agent_count = 5
agent_start_index = 1
agent_spawn_delay = 0.5

real_time_factor = 1.0
auto_dt = True

lin_vel_scaling_factor = 0.1
ang_vel_scaling_factor = 0.07

# -- Meta
timers_period = 0.000001


