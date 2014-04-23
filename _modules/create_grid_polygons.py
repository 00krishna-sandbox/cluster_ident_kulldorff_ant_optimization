__author__ = 'krishnab'

"""
    create grid and polygons module
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains functions to create a spatial grid, attach points
    to the grid, and identify adjacency between the polygons in the grid.

    :copyright: Krishna Bhogaonker, 2014
    :license: license_name, see LICENSE for more details
"""
import numpy as np
import unittest
import pandas
from scipy.stats import expon
from scipy.stats import uniform

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

    """

    # Create a meshgrid for faster vectorized function processing
    x = np.arange(xmin, xmax, inc)
    y = np.arange(ymin, ymax, inc)
    xy = np.meshgrid(x, y)
    xx, yy = np.meshgrid(x,y)
    # create the results grid
    count_grid = np.zeros(shape=(len(x) * len(y), 10))

    # set the original left coordinates equal to the first column of the result
    # grid.

    count_grid[:,0] = count_grid[:,4] = xx.flat[:]
    count_grid[:,1] = count_grid[:,3] = yy.flat[:]

    # set the right bottom coordinate based upon the increment
    count_grid[:,2] = count_grid[:,6] = (xx + inc).flat[:]
    count_grid[:,5] = count_grid[:,7] = (yy + inc).flat[:]

    # create index for pixels
    count_grid[:,8] = np.arange(0,len(x)*len(y),1)
    # return count_grid with full results.
    return count_grid


def get_counts_per_pixel(data, increment):
    """
    This function will take a set of event data, create a grid, and aggregate
    the event counts by grid pixel.

    parameters:

    data: numpy.array - a numpy array with data

    returns:

    numpy array with a column for.

    leftbx - float - the left bottom x-coordinate of the pixel



    """
