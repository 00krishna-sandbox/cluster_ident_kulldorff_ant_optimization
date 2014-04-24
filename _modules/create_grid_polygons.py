__author__ = 'krishnab'

"""
    create grid and polygons module
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains functions to create a spatial grid, attach points
    to the grid, and identify adjacency between the polygons in the grid.

    :copyright: Krishna Bhogaonker, 2014
    :license: license_name, see LICENSE for more details
"""

## Import appropriate modules
import numpy as np
import unittest


def create_grid(xmin, xmax, ymin, ymax, inc):
    """
    This function will create a numpy array for a grid that contains the
    geometry info for each pixel and the event counts per pixel.

    parameters:

    xmin: float - the minimum x coord for the grid.

    xmax: float - the maximum x coord for the grid.

    ymin: float - the minimum y coord for the grid.

    ymax: float - the maximum y coord for the grid.

    inc: float - the grid size x, y increment. This is a
    square grid so the increment is the same in x, y
    direction

    returns:

    numpy array with a column for.

    leftbx - float - the left bottom x-coordinate of the pixel

    leftby - float - the left bottom y-coordinate of the pixel

    rightbx - float - the right bottom x-coordinate of the pixel

    rightby - float - the right bottom y-coordinate of the pixel

    lefttx - float - the left top x-coordinate of the pixel

    leftty - float - the left top y-coordinate of the pixel

    righttx - float - the right top x-coordinate of the pixel

    rightty - float - the right top y-coordinate of the pixel

    index - int - the pixel index.

    count - int - the event count for the pixel

    centroidx - float - the x-coordinate of the pixel centroid

    centroidy - float - the y-coordinate of the pixel centroid

    """

    # Create a meshgrid for faster vectorized function processing
    x = np.arange(xmin, xmax, inc)
    y = np.arange(ymin, ymax, inc)
    xy = np.meshgrid(x, y)
    xx, yy = np.meshgrid(x,y)
    # create the results grid
    count_grid = np.zeros(shape=(len(x) * len(y), 12), dtype=np.float64)

    # set the original left coordinates equal to the first column of the result
    # grid.

    count_grid[:,0] = count_grid[:,4] = xx.flat[:]
    count_grid[:,1] = count_grid[:,3] = yy.flat[:]

    # set the right bottom coordinate based upon the increment
    count_grid[:,2] = count_grid[:,6] = (xx + inc).flat[:]
    count_grid[:,5] = count_grid[:,7] = (yy + inc).flat[:]

    # create index for pixels
    count_grid[:,8] = np.arange(0,len(x)*len(y),1)

    # generate the centroisds for each pixel

    count_grid[:, 10] = count_grid[:,0] + np.asarray([float(inc)/2.])
    count_grid[:, 11] = count_grid[:,1] + np.asarray([float(inc)/2.])
    # return count_grid with full results.
    return count_grid


def get_counts_per_pixel(data, increment):
    """
    This function will take a set of event data, create a grid, and aggregate
    the event counts by grid pixel.

    parameters:

    data: numpy.array - a numpy array with data

    increment: float - the x and y increment for the grid

    data shape:

    data[0] - float - x-coordinate
    data[1] - float - y-coordinate

    returns:

    numpy array from the create_grid function. But, the count column
    will be filled in.

    """

    # First create the grid to fill

    # first get the range of the grid

    xmin = np.amin(data[:,0])
    xmax = np.amax(data[:,0])
    ymin = np.amin(data[:,1])
    ymax = np.amax(data[:,1])

    g = create_grid(xmin, xmax, ymin, ymax, increment)

    # Sort the data along the x column (axis = 0)
    data.sort(axis = 0)

    # Count the number of records that fall into each bin and save those
    # numbers to the 9th column of the grid array.

    for i in xrange(g.shape[0] + 1):
        g[i, 9] = sum(np.logical_and(np.logical_and(data[:,0] > g[i,0], data[:,0]< g[i,2]),
                       np.logical_and(data[:,1] > g[i,1],data[:,1] < g[i,5])))

    return g

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        self.t = create_grid(1,5,1,5,1)
        self.assertEqual(self.t.shape, (16,12))
    def test2(self):
        self.t = create_grid(1,5,1,5,1)
        self.assertEqual(self.t[1][0], 2.0)


if __name__ == '__main__':
    unittest.main()
