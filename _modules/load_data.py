__author__ = 'krishnab'


"""
    load_data module
    ~~~~~~~~~~~~~

    This module contains code to generate some test data for the cluster
    identification algorithm. This module will also import the iraq and syria
    data for testing.

    :copyright: Krishna Bhogaonker, 2014
    :license: license_name, see LICENSE for more details
"""
import numpy as np
import unittest
import pandas
from scipy.stats import expon
from scipy.stats import uniform


def generate_random_exponential_timeseries(dlamb, ndays=100, num=100):
    """
    This function will generate some random exponential 2d data
    in a time series.

    parameters:

    dlamb: float - the exponential lambda parameter

    ndays: int - number of days in the time series

    num: int - total number of locations

    returns:

    numpy array of coordinates with day index

    """

    a = np.zeros([ndays*num, 3])
    b = np.array(range(0, ndays))
    b = np.repeat(b, num)
    a[:,0] = b

    for row in a:
        row[1] = expon.rvs(loc=0, scale = dlamb)
        row[2] = expon.rvs(loc=0, scale = dlamb)

    return a

def generate_random_uniform_timeseries(rmin, rmax, ndays=100, num=100):
    """
    This function will generate some random uniform 2d data
    in a time series.

    parameters:

    rmin: int - the minimum value of the range

    rmax: int - the maximum value of the range

    ndays: int - number of days in the time series

    num: int - total number of locations

    returns:

    numpy array of coordinates with day index

    """

    # First create an empty array of the proper size

    a = np.zeros([ndays*num, 3])
    b = np.array(range(0, ndays))
    b = np.repeat(b, num)
    a[:,0] = b

    for row in a:
        row[1] = uniform.rvs(rmin, rmax)
        row[2] = uniform.rvs(rmin, rmax)

    return a


def generate_random_exponential_data(dlamb, num = 100):
    """
    This function will generate some random exponential 2d data. There is
    no time series information here. This is just a one-time bunch of points.

    parameters:

    dlamb: float - the exponential lambda parameter

    num: int - total number of coordinates

    returns:

    numpy array of coordinates.

    """

    xcoord = expon.rvs(loc=0, scale = dlamb, size = num)
    ycoord = expon.rvs(loc=0, scale = dlamb, size = num)

    return np.asarray(zip(xcoord, ycoord), dtype=np.float64)

def generate_random_uniform_data(rmin, rmax,num = 100):
    """
    This function will generate some uniform 2d data. There is
    no time series information here. This is just a one-time bunch of points.

    parameters:

    rmin: positive int - the min value of the generated data

    rmax: positive int - the max value of the generated data

    num: int - total number of coordinates

    returns:

    numpy array of coordinates.

    """

    xcoord = uniform.rvs(rmin, rmax, size = num)
    ycoord = uniform.rvs(rmin, rmax, size = num)

    return np.asarray(zip(xcoord, ycoord), dtype = np.float64)


def load_iraq_data():
    """
    This function will load the iraq incident csv file into a numpy array.

    parameters:

    None

    returns:

    numpy array of iraq data.

    """
    df = pandas.read_csv("../_data/iraqdeathswiki.csv")
    return df.values

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        self.t = generate_random_exponential_timeseries(10, 5, 5)
        self.assertEqual(self.t.shape, (25,3))
    def test2(self):
        self.t = generate_random_uniform_timeseries(0,100,6,6)
        self.assertEqual(self.t.shape, (36,3))


if __name__ == '__main__':
    unittest.main()
