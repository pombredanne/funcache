# -*- coding: utf-8 -*-
"""
:Module: ````
:Author: `Adrian Letchford <http://www.dradrian.com>`_
:Organisation: `Warwick Business School <http://www.wbs.ac.uk/>`_, `University of Warwick <http://www.warwick.ac.uk/>`_.
:Created On: Sun Mar 22 18:28:08 2015
"""

# Import build in modules
import sys

# Import external modules

# Import custom modules
sys.path.append('../funcache')
from funcache import Cache, function2name

#------------------------------------------------------------------------------
# Program Start
#------------------------------------------------------------------------------

#cache = Cache('mycache')

def func(d, b='l'):
    return {'one': d}
    
#cache.run(func, 2, b='8')
#
#name = function2name(func, 2, b='8')
#
#print name
#
#print cache.is_cached(name)
