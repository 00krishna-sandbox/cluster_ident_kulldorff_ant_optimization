Cluster Identification using Kulldorff Method with Ant Colony Optimization
==========================================================================

This project develops some modules to find event clusters in a given dataset.
The goal is to determine both the existence and location of event clusters
as well as the shape of those clusters.

The challenge of cluster analysis is to first determine whether clustering
exists. There are a couple of different approaches to this type of analysis. I
use the Kulldorff-Nagarwala method: spatial scan statistic. This approach is
good for identifying the location of clusters, however it is not as good at
determining the tendency for clustering in a given dataset. Alternative methods
of determining clustering tendency are also provided.

The second part of the package provides a method to identify cluster shape.
Using some recent work in Ant Colony Optimization methods (Dorigo & Stutzle,
2004) and (Pei, et al., 2013), the package can determine the shape of clusters.

Dependencies
------------
python: numpy 1.8
python: unittest
python: rpy2
R: R-3.1.0
R: SpatialEpi-1.1 package


