import math

#Input format (input.txt):
#100 100 0 0 1 0 0
#30 150 0 0 -1 0 0

# Read input from file
with open('input.txt', 'r') as f:
    colin_params = list(map(int, f.readline().split()))
    petin_params = list(map(int, f.readline().split()))

# Unpack Colin's parameters
R_colin, x_colin, y_colin, z_colin, vx_colin, vy_colin, vz_colin = colin_params

# Unpack Petin's parameters
R_petin, x_petin, y_petin, z_petin, vx_petin, vy_petin, vz_petin = petin_params

# Calculate the relative velocity between the balls
relative_vx = vx_petin - vx_colin
relative_vy = vy_petin - vy_colin
relative_vz = vz_petin - vz_colin

# Calculate the relative distance between the balls
relative_x = x_petin - x_colin
relative_y = y_petin - y_colin
relative_z = z_petin - z_colin

# Calculate the coefficients for a quadratic equation
a = relative_vx**2 + relative_vy**2 + relative_vz**2
b = 2 * (relative_x * relative_vx + relative_y * relative_vy + relative_z * relative_vz)
c = relative_x**2 + relative_y**2 + relative_z**2 - (R_colin + R_petin)**2

# Calculate the discriminant
discriminant = b**2 - 4 * a * c

# Check if the balls collide or not
if discriminant >= 0:
    # Calculate the collision time
    t = (-b - math.sqrt(discriminant)) / (2 * a)

    # Calculate the collision point coordinates
    collision_x = x_colin + vx_colin * t
    collision_y = y_colin + vy_colin * t
    collision_z = z_colin + vz_colin * t

    # Write output to file
    with open('output.txt', 'w') as f:
        f.write("YES\n")
        f.write("{:.5f} {:.5f} {:.5f}".format(collision_x, collision_y, collision_z))
else:
    # Calculate the minimum distance between the balls
    min_distance = math.sqrt(relative_x**2 + relative_y**2 + relative_z**2) - (R_colin + R_petin)

    # Write output to file
    with open('output.txt', 'w') as f:
        f.write("NO\n")
        f.write("{:.5f}".format(min_distance))
