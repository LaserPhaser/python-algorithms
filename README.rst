|Build Status| |Coverage Status| |Maintainability| |Codacy| |Documentation Status|

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
-  `Heap sort <algorithms/sorting/heap_sort.py>`__

Algorithms on Graphs
~~~~~~~~~~~~~~~~~~~~


-  `DFS (Depth first search) <algorithms/graphs/dfs.py>`__
-  `BFS (Breadth first search) <algorithms/graphs/bfs.py>`__
-  `Dijkstra (priority queue) <algorithms/graphs/dijkstra.py>`__
-  `Bidirectional Dijkstra (priority queues) <algorithms/graphs/bidi_dijkstra.py>`__
-  `Cycle detection (DFS) <algorithms/graphs/dfs_cycle_detection.py>`__
-  `SCC (Strongly connected components) <algorithms/graphs/strongly_connected.py>`__
-  `Topological Sort <algorithms/graphs/topological_sort.py>`__
-  `Bipartite <algorithms/graphs/bipartite.py>`__
-  `Bellman-Ford algorithm (negative cycle detection) <algorithms/graphs/bellman_ford.py>`__
-  Kruskal algorithm for connecting points
-  A* (potential function - euclidean distance)
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
.. |Maintainability| image:: https://api.codeclimate.com/v1/badges/b911a106363fd033ed21/maintainability
    :target: https://codeclimate.com/github/ArseniyAntonov/python-algorithms/maintainability
.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/dbe5942aa3b44a4588346ea757c494de    
    :target: https://www.codacy.com/app/ArseniyAntonov/python-algorithms?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ArseniyAntonov/python-algorithms&amp;utm_campaign=Badge_Grade
