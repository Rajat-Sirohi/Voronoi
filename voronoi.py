from PIL import Image
import numpy as np
import subprocess

def data_to_pixels(data):
    pixels = []
    for i in range(height,0,-1):
        for j in range(width):
            pixels.append(data[j][i-1])
    return pixels

def distance(p1,p2):
    p = 1
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    return (abs(dx)**p+abs(dy)**p)**(1/p)

def nearSite(p,r):
    for s in sites:
        if distance(p,s) < r:
            return True
    return False

width = 1000
height = 1000
show_progress = True

# randomly generate sites
if show_progress:
    print("Processing sites...")
num_sites = 20
sites = []
for i in range(num_sites):
    x = np.random.randint(0,width)
    y = np.random.randint(0,height)
    sites.append((x,y))

# initialize arrays
if show_progress:
    print("Initializing arrays...")
points = []
voronoi = []
data = []
for x in range(width):
    voronoi.append([])
    data.append([])
    for y in range(height):
        points.append((x,y))
        voronoi[x].append([])
        data[x].append([])

# compute voronoi[] array which gives value of nearest site at each point
if show_progress:
    print("Computing voronoi diagram...")
for p in points:
    voronoi[p[0]][p[1]] = 0
    mindist = distance(p,sites[0])
    for i in range(1,num_sites):
        tempdist = distance(p,sites[i])
        if tempdist < mindist:
            mindist = tempdist
            voronoi[p[0]][p[1]] = i

# generate random colors for voronoi cells
if show_progress:
    print("Generating random colors...")
site_color = (0,0,0)
colors = []
for i in range(num_sites):
    r = int(np.random.random()*255)
    g = int(np.random.random()*255)
    b = int(np.random.random()*255)
    colors.append((r,g,b))

# use voronoi[] to construct pixel-by-pixel data[]
if show_progress:
    print("Generating pixel data...")
near_distance = np.sqrt(width*height/10000)
for x in range(width):
    for y in range(height):
        if nearSite((x,y), near_distance):
            data[x][y] = site_color
        else:
            data[x][y] = colors[voronoi[x][y]]

# convert pixel data[] into readable format for PIL
if show_progress:
    print("Converting pixel data...")
pixels = data_to_pixels(data)

img = Image.new('RGB', (width,height))
img.putdata(pixels)
img.save('output.png')

print("DONE!")

subprocess.run(["mpv", "output.png"])
