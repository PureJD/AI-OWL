import random 


# Function to generate stars with velocity
def generate_stars(num_stars, width, height):
    stars = []
    for _ in range(num_stars):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(1, 2)
        # Random velocity for each star
        vx = random.uniform(-0.5, 0.5)
        vy = random.uniform(-0.5, 0.5)
        stars.append((x, y, size, vx, vy))
    return stars