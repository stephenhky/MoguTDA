
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='mogutda',
      version="0.1.2",
      description="Topological Data Analysis in Python",
      long_description="Topological Data Analysis in Python: Simplicial Complex",
      classifiers=[
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Scientific/Engineering :: Physics",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: MIT License",
      ],
      keywords="mogutda numerics topology",
      url="https://github.com/stephenhky/MoguTDA",
      author="Kwan-Yuet Ho",
      author_email="stephenhky@yahoo.com.hk",
      license='MIT',
      packages=['mogutda',],
      install_requires=[
          'numpy', 'scipy', 'networkx>=2.0',
      ],
      tests_require=[
          'unittest2',
      ],
      include_package_data=True,
      test_suite="test",
      zip_safe=False)

