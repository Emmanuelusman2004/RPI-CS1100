import math

def find_volume_sphere(radius):
    volume_sphere = 4/3 * math.pi * (radius)**3
    return volume_sphere
    
def find_volume_cube(edge_length):
    volume_cube = edge_length**3
    return volume_cube
    
radius = input("Enter the gum ball radius (in.) => ")
print(radius)

sales = input("Enter the weekly sales => ")
print(sales)

sales = int(sales)

radius = float(radius)

total_gumballs = 1.25 * (sales)
total_gumballs = math.ceil(total_gumballs)

balls_per_edge = total_gumballs ** (1/3)
balls_per_edge = math.ceil(balls_per_edge)
diameter = 2 * radius
edge_length = balls_per_edge * diameter

target_sales = total_gumballs

volume_gumball = find_volume_sphere(radius)

gumballs_in_machine = (balls_per_edge)**3

extra_gumballs = gumballs_in_machine - target_sales
extra_gumballs = int(extra_gumballs)

wasted_area_target = find_volume_cube(edge_length) - (target_sales * volume_gumball)
wasted_area_full = find_volume_cube(edge_length) - (gumballs_in_machine * volume_gumball)

print("")

print("The machine needs to hold " + str(balls_per_edge) + " gum balls along each edge.")
print("Total edge length is " + format(edge_length, ".2f") + " inches.")
print("Target sales were " + str(target_sales) + ", but the machine will hold "  + str(extra_gumballs) + " extra gum balls.")
print("Wasted space is " + format(wasted_area_target, ".2f") + " cubic inches with the target number of gum balls,")
print("or " + format(wasted_area_full, ".2f") + " cubic inches if you fill up the machine.")
