import matplotlib.pyplot as plt
import numpy as np

def main():
    x_max = 3
    y_max = 3
    coords = read_file()
    for i in coords:
        print(i)
    square = rad_calc(coords, x_max, y_max)
    #print(square[0].shape)
    for x in range(0, x_max):
        for y in range(0, y_max):
            print(square[x][y], end = " ")
        print(end = "\n")
    plotting(square, x_max, y_max)

def read_file(file_name="input.txt"):
    coords = list()
    for line in open(file_name):
        line = line.rstrip('\n')
        vals = line.split(" ")
        coords.append(np.array([float(vals[0]), float(vals[1])]))
    return coords

def rad_calc(coords, x_max, y_max):
    square = np.zeros((x_max, y_max))
    for x in range(0, x_max):
        for y in range(0, y_max):
            r = list()
            for sprayer in coords:
                d_x = (x + 1) - sprayer[0]
                d_y = (y + 1) - sprayer[1]
                r.append(np.sqrt(d_x**2+d_y**2))
            for k in r:
                intensity = 1/(np.sqrt(1+(k)**2))
                square[x][y] += intensity
    return square

def plotting(square, x_max, y_max):
    x = np.arange(0, x_max + 1, 1)  # len = 11
    y = np.arange(0, y_max + 1, 1)  # len = 7

    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, square)
    plt.show()
    ax.set_aspect('equal')

if __name__ == "__main__":
    main()
