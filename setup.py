
from setuptools import setup


def readme():
    with open('README.md', 'r', encoding="utf-8") as f:
        return f.read()


def package_description():
    text = open('README.md', 'r', encoding="utf-8").read()
    startpos = text.find('## Introduction')
    return text[startpos:]


def install_requirements():
    return [
        package_string.strip()
        for package_string in open('requirements.txt', 'r', encoding="utf-8")
    ]


setup(name='mogutda',
      version="0.4.0a1",
      description="Topological Data Analysis in Python",
      long_description=package_description(),
      long_description_content_type='text/markdown',
      classifiers=[
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Scientific/Engineering :: Physics",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: Information Technology",
          "Intended Audience :: Science/Research"
      ],
      keywords="mogutda numerics topology data",
      url="https://github.com/stephenhky/MoguTDA",
      author="Kwan-Yuet Ho",
      author_email="stephenhky@yahoo.com.hk",
      license='MIT',
      packages=['mogutda',],
      install_requires=install_requirements(),
      include_package_data=True,
      test_suite="test",
      zip_safe=False)

