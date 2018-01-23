|Build Status| |Coverage Status| |Documentation Status|

python-algorithms
=================

python-algorithms project is a collection of algorithms and datastructures implemented on
``Python3.6`` You don’t need to install these project as a module (via
pip) because usually you just need only one algorithm instead of all
pack, so just copy and paste the source code. For easy navigation please
use links to the source code below.

Algorithms:
-----------------------

Arithmetic
~~~~~~~~~~

-  `GCD [Greatest Common Divisor] <algorithms/arithmetic/gcd.py>`__
-  `LCM [Least Common Multiple] <algorithms/arithmetic/lcm.py>`__

Greedy
~~~~~~

-  `Covering segments <algorithms/greedy/covering_segments.py>`__
-  `Fractional knapsack <algorithms/greedy/fractional_knapsack.py>`__

Search
~~~~~~

-  `Binary search <algorithms/search/binary_search.py>`__
-  `Closest pair <algorithms/search/closest_pair.py>`__
-  `Fibonacci [Recursive method] <algorithms/search/fibonacci.py>`__
-  `Fibonacci by Modulo [with Pisano period] <algorithms/search/fibonacci_modulo.py>`__
-  `Rabin-Karp algorithm <algorithms/search/rabinkarp.py>`__

Sorting
~~~~~~~

-  `Merge sort <algorithms/sorting/merge_sort.py>`__
-  `Quick sort with [Dutch National Flag Algorithm] optimization <algorithms/sorting/quick_sort.py>`__

Algorithms on Graphs
~~~~~~~~~~~~~~~~~~~~


-  `DFS (Depth first search) <algorithms/graphs/dfs.py>`__
-  `BFS (Breadth first search) <algorithms/graphs/bfs.py>`__
-  SCC (Strongly connected components)
-  Topological Sort
-  Bipartite (Algorithms based on BFS for check that grap is bipartite)
-  Bellman-Ford algorithm (and negative cycle detection based on this
   approach)
-  Bellman-Ford algorithm (and negative cycle detection based on this
   approach + infinity Arbitrage detection)
-  Kruskal algorithm for connecting points
-  Dijkstra (on priority queue)
-  Bidirectional Dijkstra (on priority queues)
-  AStar (potential function - euclidean distance)
-  `BST checker <algorithms/graphs/bst_check.py>`__

Dynamic Programming
~~~~~~~~~~~~~~~~~~~
-  `Knapsack <algorithms/dynamic_programming/knapsack.py>`__


Datastructures:
---------------

-  `Hash chain <algorithms/hash_tables/hash_chain.py>`__


Unsorted:
---------

-  Tree traversal methods (in/pre/post order recursive and iterative)
-  Rope data structure (heavyweight strings based on splay tree with
   iterative in order traversal)

.. |Build Status| image:: https://travis-ci.org/ArseniyAntonov/python-algorithms.svg?branch=master
    :target: https://travis-ci.org/ArseniyAntonov/python-algorithms
.. |Documentation Status| image:: https://readthedocs.org/projects/python-algorithms-doc/badge/?version=latest
    :target: http://python-algorithms-doc.readthedocs.io/en/latest/?badge=latest
.. |Coverage Status| image:: https://codecov.io/gh/ArseniyAntonov/python-algorithms/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ArseniyAntonov/python-algorithms