import imageio
import sys


def make_gif(filepath):
    images = []
    filenames = ['{}_{}.png'.format(filepath, num) for num in range(0, 50)]
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('/gifs/{}.gif'.format(filename), images)


if __name__ == '__main__':
    filepath = sys.argv[1]
    make_gif(filepath)
