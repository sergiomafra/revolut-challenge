import sys
sys.path.append('../classes')

from classes.Nest import Nest
from pytest import fixture


@fixture(scope='function')
def nest_instance():
    nest = Nest()
    return nest
