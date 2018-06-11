
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='mogutda',
      version="0.1.0",
      description="Topological Data Analysis in Python",
      long_description="Topological Data Analysis in Python: Simplicial Xomplex",
      classifiers=[
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Programming Language :: Python :: 2.7",
          "License :: OSI Approved :: MIT License",
      ],
      keywords="mogutda numerics topology",
      url="https://github.com/stephenhky/MoguNumerics",
      author="Kwan-Yuet Ho",
      author_email="stephenhky@yahoo.com.hk",
      license='MIT',
      packages=['mogutda',],
      # package_data={'mogu': ['finance/binomial/*.f90', 'finance/binomial/*.pyf',
      #                        'dynprog/*.c', 'dynprog/*.i', 'dynprog/*.h',],
      #               'test': ['*.csv']},
      # setup_requires=['numpy',],
      install_requires=[
          'numpy', 'scipy', 'numba',  'networkx>=2.0',
      ],
      tests_require=[
          'unittest2',
      ],
      # scripts=['bin/concatenate_dict', 'bin/mogu_minerule', 'bin/price_option', 'bin/mogu_sammon'],
      # ext_modules = [Extension( 'binomialtree', sources=['mogu/finance/binomial/binomialtree.f90',
      #                                                    'mogu/finance/binomial/binomialtree.pyf'] ),
      #                Extension( '_dldist', sources=['mogu/dynprog/dldist_wrap.c',
      #                                               'mogu/dynprog/dldist.c']),
      #                ],
      include_package_data=True,
      test_suite="test",
      zip_safe=False)

