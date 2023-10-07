# The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.
# storage_efficiency =
# volume
# surface_area

'''volume = π radius2 height

surface_area = 2π radius (radius + height)'''


import math

# def compute_volume(pi, r, h):
#     volume = pi * (r**2) * h
#     return volume

# def compute_surface_area(pi, r, h):
#     surface_area = (2 * pi * r) * (r + h)
#     return surface_area

# def main():
#     pi = math.pi
#     r = 6
#     h = 5

#     volume = compute_volume(pi, r, h)
#     surface_area = compute_surface_area(pi, r, h)

#     storage_efficiency = volume / surface_area
#     return storage_efficiency

# result = main()
# print(f"Storage Efficiency: {result}")


import math

def main():
    can_specs = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16},
        {"name": "#1 Tall", "radius": 7.78, "height": 11.91},
        {"name": "#2", "radius": 8.73, "height": 11.59},
        {"name": "#2.5", "radius": 10.32, "height": 11.91},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78},
        {"name": "#5", "radius": 13.02, "height": 14.29},
        {"name": "#6Z", "radius": 5.4, "height": 8.89},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62},
        {"name": "#10", "radius": 15.72, "height": 17.78},
        {"name": "#211", "radius": 6.83, "height": 12.38},
        {"name": "#300", "radius": 7.62, "height": 11.27},
        {"name": "#303", "radius": 8.1, "height": 11.11},
    ]

    for can in can_specs:
        name = can["name"]
        radius = can["radius"]
        height = can["height"]
        volume = compute_volume(radius, height)
        surf_area = compute_surface_area(radius, height)
        storage_efficiency = volume / surf_area
        print(f"{name} {storage_efficiency:.2f}")

def compute_volume(radius, height):
    """Compute and return the volume of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area

# Start this program by calling the main function.
if __name__ == "__main__":
    main()

