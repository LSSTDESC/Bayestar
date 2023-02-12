from setuptools import find_packages
from setuptools import setup

setup(name='bayestar',
      version='0.1',
      description='Automatically Differentiable Bayesian Survey Simulation',
      url='https://github.com/LSSTDESC/Bayestar',
      author='LSST DESC',
      license='MIT',
      packages=find_packages(),
      use_scm_version=True,
      setup_requires=["setuptools_scm"])