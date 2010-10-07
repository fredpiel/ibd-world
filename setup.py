# Author: Anand Patil
# Date: 6 Feb 2009
# License: Creative Commons BY-NC-SA
####################################

from setuptools import setup
from numpy.distutils.misc_util import Configuration
import os
config = Configuration('ibdw',parent_package=None,top_path=None)

config.add_extension(name='cut_geographic',sources=['ibdw/cut_geographic.f'])

config.packages = ["ibdw"]
if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**(config.todict()))