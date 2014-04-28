# coding=utf-8
__author__ = 'krishnab'

"""
    Kulldorff clustering module
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains a function to pass data to R and then get the
    clustering results back into python. I use the SpatialEpi R package and
    use the rpy2 interface between python and R.

    :copyright: Krishna Bhogaonker, 2014
    :license: license_name, see LICENSE for more details
"""

# ImportsI would

import rpy2.robjects as robjects
from rpy2.robjects.packages import importr


def kulldorff(geo, cases, population, n_simulations, plt):
    """
    This function will create a numpy array for a grid that contains the
    geometry info for each pixel and the event counts per pixel.

    parameters:

    geo: matrix: n x 2 table of (x,y)-coordinates for area centroid.
    cases: int vector: case counts for all n areas
    population: int vector: aggregated population counts for all n areas
    n_simulations: int: the number of Monte Carlo simulations to run
    plt: boolean: flag for whether to plot the histogram of MC samples.

    returns:

    most.likely.cluster: information on the most likely cluster
    secondary.clusters: information on secondary clusters
    type: type of likelihood
    log.lkhd: log-likelihood of each zone considered
    simulated.log.lkhd: n.simulations MC samples of the log-likelihood of
    the most likely cluster.

    most.likely.cluster and secondary.clusers returns
    location.IDs.included: ID’s of areas in cluster, in order of distance
    population: population of cluster
    number.of.cases: number of cases in cluster
    expected.cases: expected number of cases in cluster
    SMR: estimated SMR of cluster
    log.likelihood.ratio: log-likelihood of cluster
    monte.carlo.rank: rank of lkhd of cluster within Monte Carlo simulated values
    p.value: Monte Carlo p-value returns:
    """

    f = importr("SpatialEpi")
    expected_cases = "NULL"
    pop_upper_bound = 1000000
    apha = 0.95


    res = f.kulldorff(geo, cases, population,expected_cases, pop_upper_bound,
                      n_simulations, apha, plt)

    return res




class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        self.t = create_grid(1,5,1,5,1)
        self.assertEqual(self.t.shape, (16,12))
    def test2(self):
        self.t = create_grid(1,5,1,5,1)
        self.assertEqual(self.t[1][0], 2.0)


if __name__ == '__main__':
    unittest.main()