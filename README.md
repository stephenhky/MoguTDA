# `mogutda`: Topological Data Analysis in Python

[![Build Status](https://travis-ci.org/stephenhky/MoguTDA.svg?branch=master)](https://travis-ci.org/stephenhky/MoguTDA)
[![GitHub release](https://img.shields.io/github/release/stephenhky/MoguTDA.svg?maxAge=3600)](https://github.com/stephenhky/MoguTDA/releases)

## Introduction

`mogutda` contains Python codes that demonstrate the numerical calculation
of algebraic topology in an application to topological data analysis
(TDA). Its core code is the numerical methods concerning implicial complex,
and the estimation of homology and Betti numbers.

Topological data analysis aims at studying the shapes of the data, and
draw some insights from them. A lot of machine learning algorithms deal
with distances, which are extremely useful, but they miss the
information the data may carry from their geometry.

## History

The codes in this package were developed as a demonstration of a few posts of my blog.
It was not designed to be a Python package but a pedagogical collection of codes.
(See: [PyTDA](https://github.com/stephenhky/PyTDA).)
However, the codes and the blog posts have been unexpectedly popular. Therefore,
I modularized the code into the package [`mogu`](https://pypi.org/project/mogu/).
(or corresponding repository: [MoguNumerics](https://github.com/stephenhky/MoguNumerics))
However, `mogu` is simply a collection of unrelated numerical routines with a lot of
dependencies, but the part of TDA can be quite independent.

In order to provide other researchers and developers an independent package, which is compact (without
unecessary alternative packages to load), and efficient, I decided to modularize
the codes of TDA separately, and name this package `mogutda`.

## Prerequisite

It runs under Python 2.7, 3.5, 3.6, and 3.7.

Release 0.1.5 can work under `numpy`>0.16.0, but previous
release will constitute error under the new `numpy`.

## Simple Tutorial: Simplicial Complex

You can install by:

```
pip install -U mogutda
```

To establish a simplicial complex for a torus, type

```
import numpy as np
from mogutda import SimplicialComplex

torus_sc = [(1,2,4), (4,2,5), (2,3,5), (3,5,6), (5,6,1), (1,6,2), (6,7,2), (7,3,2),
            (1,3,4), (3,4,6), (4,6,7), (4,5,7), (5,7,1), (7,3,1)]
torus_c = SimplicialComplex(simplices=torus_sc)
```

To retrieve its Betti numbers, type:

```
print(torus_c.betti_number(0))   # print 1
print(torus_c.betti_number(1))   # print 2
print(torus_c.betti_number(2))   # print 1
```

## Demo Codes and Blog Entries

Codes in this repository are demo codes for a few entries of my blog,
[Everything about Data Analytics](https://datawarrior.wordpress.com/),
and the corresponding entries are:

* [Starting the Journey of Topological Data Analysis (TDA)](https://datawarrior.wordpress.com/2015/08/03/tda-1-starting-the-journey-of-topological-data-analysis-tda/) (August 3, 2015)
* [Constructing Connectivities](https://datawarrior.wordpress.com/2015/09/14/tda-2-constructing-connectivities/) (September 14, 2015)
* [Homology and Betti Numbers](https://datawarrior.wordpress.com/2015/11/03/tda-3-homology-and-betti-numbers/) (November 3, 2015)
* [Topology in Physics and Computing](https://datawarrior.wordpress.com/2015/11/10/mathanalytics-6-topology-in-physics-and-computing/) (November 10, 2015)
* [Persistence](https://datawarrior.wordpress.com/2015/12/20/tda-4-persistence/) (December 20, 2015)
* [Topological Phases](https://datawarrior.wordpress.com/2016/10/06/topological-phases/) (October 6, 2016)
* [moguTDA: Python package for Simplicial Complex](https://datawarrior.wordpress.com/2018/07/02/mogutda-python-package-for-simplicial-complex/) (July 2, 2018)

## Wolfram Demonstration
Richard Hennigan put a nice Wolfram Demonstration online explaining what
the simplicial complexes are, and how homologies are defined:

* [Simplicial Homology of the Alpha Complex](http://demonstrations.wolfram.com/SimplicialHomologyOfTheAlphaComplex/)

## News

* 02/20/2019: `mogutda` 0.1.5 released.
* 12/31/2018: `mogutda` 0.1.4 released.
* 07/18/2018: `mogutda` 0.1.3 released.
* 07/02/2018: `mogutda` 0.1.2 released.
* 06/13/2018: `mogutda` 0.1.1 released.
* 06/11/2018: `mogutda` 0.1.0 released.

## Other TDA Packages

It is recommended that for real application, you should use the following packages
for efficiency, because my codes serve the pedagogical purpose only.

### C++
* [Dionysus](http://www.mrzv.org/software/dionysus/)
* [PHAT](https://bitbucket.org/phat-code/phat)

### Python
* [Dionysus](http://www.mrzv.org/software/dionysus/python/overview.html)

### R
* [TDA](https://cran.r-project.org/web/packages/TDA/index.html) (article: [\[arXiv\]](http://arxiv.org/abs/1411.1830))

## Contributions

If you want to contribute, feel free to fork the repository, and submit
a pull request whenever you are ready.

If you spot any bugs or issues, go to the [Issue](https://github.com/stephenhky/MoguTDA) page.

I may not approve pull request immediately if your suggested change is big.
If you want to incorporate something big, please discuss with me first.

## References
* Afra J. Zomorodian. *Topology for Computing* (New York, NY: Cambridge University Press, 2009). [\[Amazon\]](https://www.amazon.com/Computing-Cambridge-Monographs-Computational-Mathematics/dp/0521136091)
* Afra J. Zomorodian. "Topological Data Analysis," *Proceedings of Symposia in Applied Mathematics* (2011). [\[link\]](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.261.1298)
* Afra Zomorodian, Gunnar Carlsson, “Computing Persistent Homology,” *Discrete Comput. Geom.* 33, 249-274 (2005). [\[pdf\]](http://geometry.stanford.edu/papers/zc-cph-05/zc-cph-05.pdf)
* Gunnar Carlsson, “Topology and Data”, *Bull. Amer. Math. Soc.* 46, 255-308 (2009). [\[link\]](http://www.ams.org/journals/bull/2009-46-02/S0273-0979-09-01249-X/)
* Jeffrey Ray, Marcello Trovati, "A Survey of Topological Data Analysis (TDA) Methods Implemented in Python," in *Advances in Intelligent Networking and Collaborative Systems*, Springer (2018).
* P. Y. Lum, G. Singh, A. Lehman, T. Ishkanov, M. Vejdemo-Johansson, M. Alagappan, J. Carlsson, G. Carlsson, “Extracting insights from the shape of complex data using topology”, *Sci. Rep.* 3, 1236 (2013). [\[link\]](http://www.nature.com/srep/2013/130207/srep01236/full/srep01236.html)
* Robert Ghrist, “Barcodes: The persistent topology of data,” *Bull. Amer. Math. Soc.* 45, 1-15 (2008). [\[pdf\]](http://www.ams.org/journals/bull/2008-45-01/S0273-0979-07-01191-3/S0273-0979-07-01191-3.pdf)

## Links

* PyPI: [https://pypi.org/project/mogutda/](https://pypi.org/project/mogutda/)
* Documentation: [https://mogutda.readthedocs.io/](https://mogutda.readthedocs.io/)
* Bug Reports: [https://github.com/stephenhky/MoguTDA/issues](https://github.com/stephenhky/MoguTDA/issues)
