import matplotlib.pyplot as plt
import numpy as np

def main():
    x_max = 6
    y_max = 6
    coords = read_file()
    for i in coords:
        print(i)
    square = rad_calc(coords, x_max, y_max)
    #print(square[0].shape)
    for x in range(0, x_max):
        for y in range(0, y_max):
            print(square[x][y], end = " ")
        print(end = "\n")
    data = square.reshape(square.shape[0]*square.shape[1])
    plotting(square, x_max, y_max)
    histogram(data)

def read_file(file_name="input.txt"):
    coords = list()
    for line in open(file_name):
        line = line.rstrip('\n')
        vals = line.split(" ")
        coords.append(np.array([float(vals[0]), float(vals[1]), float(vals[2])]))
    return coords

def rad_calc(coords, x_max, y_max):
    square = np.zeros((x_max, y_max))
    for x in range(0, x_max):
        for y in range(0, y_max):
            r = list()
            for sprayer in coords:
                d_x = (x + 1) - sprayer[0]
                d_y = (y + 1) - sprayer[1]
                r.append(d_x**2+d_y**2)
            for i in range(0, len(r)):
                intensity = coords[i][2]/(1+(r[i]))
                square[x][y] += intensity
    return square

def plotting(square, x_max, y_max):
    x = np.arange(0, x_max + 1, 1)  # len = 11
    y = np.arange(0, y_max + 1, 1)  # len = 7

    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, square)
    ax.set_aspect('equal')
    plt.pcolor(square, cmap = plt.get_cmap('viridis', 11))
    plt.colorbar()
    plt.show()

def compute_histogram_bins(data, desired_bin_size):
    min_val = np.min(data)
    max_val = np.max(data)
    min_boundary = 0
    max_boundary = max_val - max_val % desired_bin_size + desired_bin_size
    n_bins = int((max_boundary - min_boundary) / desired_bin_size) + 1
    num_bins = np.linspace(min_boundary, max_boundary, n_bins)
    return num_bins

def histogram(data):
    desired_bin_size = 0.1
    num_bins = compute_histogram_bins(data, desired_bin_size)
    n, bins, patches = plt.hist(data, num_bins, facecolor='green', alpha=1)
    plt.xlabel('intensity')
    plt.ylabel('count')
    plt.title('intensity distribution')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
