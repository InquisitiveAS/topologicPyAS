__author__ = "Abhishek Shinde"
__contact__ = "arabhishek1091@gmail.com"


import topologicpy
import topologic_core 
from topologicpy.Vertex import Vertex
from topologicpy.Edge import Edge
from topologicpy.Wire import Wire 
from topologicpy.Face import Face
from topologicpy.Shell import Shell
from topologicpy.Cell import Cell
from topologicpy.CellComplex import CellComplex
from topologicpy.Cluster import Topology
from topologicpy.Dictionary import Dictionary
from topologicpy.Graph import Graph



"""
Always print the output and then look at the documentation
from topologicpy.Class import Class - syntax of the TopologicPy
"""

cc = CellComplex.Prism()
decomp = CellComplex.Decompose()
outer_walls = decomp['externalVerticalFaces']
apertures = []

