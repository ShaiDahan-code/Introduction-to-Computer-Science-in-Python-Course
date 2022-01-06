import random

import numpy as np
import matplotlib.pyplot as plt


def createMatbySpaces(lifes, rows, cols):
    """
    What the function does?
    -----------------------
    Creating a game world Life is separated by an equal distance from each other

    Parameters
    ----------
    lifes : Integer
        the number of life wanna create on start..
    rows : Integer
        How many rows in the world(matrix).
    cols : Integer
        How many cols in the world(matrix)..

    Returns
    -------
    mat : numpy matrix
        a Matrix Rows x Cols

    """

    mat = np.zeros([rows, cols])
    grid = rows * cols
    count = lifes
    space = int(grid / lifes)
    print(space)
    for i in range(0, grid, space):
        row = i // rows
        col = i % cols
        mat[row, col] = 1
    return mat


def createMatRandom(lifes, rows, cols):
    """
    What the function does?
    -----------------------
    Creating a game world Life is separated by an random distance from each other

    Parameters
    ----------
    lifes : Integer
        the number of life wanna create on start..
    rows : Integer
        How many rows in the world(matrix).
    cols : Integer
        How many cols in the world(matrix)..

    Returns
    -------
    mat : numpy matrix
        a Matrix Rows x Cols

    """
    mat = np.zeros((rows, cols), dtype=int)
    while lifes != 0:
        i = np.random.randint(0, rows)
        j = np.random.randint(0, cols)
        if mat[i, j] != 1:
            mat[i, j] = 1
            lifes -= 1
    return mat


def theGameOfLife(minNeighbor, maxNeighbor, lifesInStart, rows, cols):
    """
    The Game Of Life
    -----------------
    The Game of Life It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further 
    input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete
    and can simulate a universal constructor or any other Turing machine. 

    What the function does?
    -----------------------
    A function initializes a world with a certain amount of life and checks the legality of every living creature in the world if it can
    continue to live or die    
    And for places where there is no living creature checks whether it is possible to create life in the same location


    Parameters
    ----------
    minNeighbor : Integer
        The minimum amount of life needed around a living creature for the living creature to continue living
    maxNeighbor : TYPE
        The maximum amount of life needed around a living creature for the living creature to continue living
    lifesInStart : TYPE
        The amount of life at the beginning of the world boot
    rows : Integer
        How many rows in the world(matrix).
    cols : Integer
        How many cols in the world(matrix)..


    """
    world = createMatRandom(lifesInStart, rows, cols)

    plt.imshow(world, cmap='hot')
    plt.show()
    p = 0
    sum_of_alive = lifesInStart
    around_world = np.zeros([rows + 2, cols + 2])

    # Initializes the world environment
    around_world[1:-1,1:-1] = world
    around_world[0, 1:-1] = world[-1, :]
    around_world[-1, 1:-1] = world[0, :]
    around_world[1:-1, 0] = world[:, -1]
    around_world[1:-1, -1] = world[:, 0]

    #Divide the matrix into 8 matrices to calculate the legality of life in each organ
    right = around_world[1:-1, :-2]
    left = around_world[1:-1, 2:]
    up = around_world[:-2, 1:-1]
    down = around_world[2:, 1:-1]
    up_left = around_world[:-2, :-2]
    up_right = around_world[:-2, 2:]
    down_left = around_world[2:, :-2]
    down_right = around_world[2:, 2:]

    while True:
        plt.imshow(world, cmap='hot')
        plt.draw()
        plt.pause(0.001)
        plt.clf()

        sum_mat = np.array(right + left + up + down
                           + up_left + up_right
                           + down_left + down_right)


        world[sum_mat == maxNeighbor] = 1
        world[sum_mat < minNeighbor] = 0
        world[sum_mat > maxNeighbor] = 0


        around_world[1:-1, 1:-1] = world
        around_world[0, 1:-1] = world[-1, :]
        around_world[-1, 1:-1] = world[0, :]
        around_world[1:-1, 0] = world[:, -1]
        around_world[1:-1, -1] = world[:, -0]

        right = around_world[1:-1, :-2]
        left = around_world[1:-1, 2:]
        up = around_world[:-2, 1:-1]
        down = around_world[2:, 1:-1]
        up_left = around_world[:-2, :-2]
        up_right = around_world[:-2, 2:]
        down_left = around_world[2:, :-2]
        down_right = around_world[2:, 2:]



def main():
    theGameOfLife(2, 3, 20000, 256, 256)


if __name__ == '__main__':
    main()
