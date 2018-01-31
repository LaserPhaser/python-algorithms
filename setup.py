import os

from Cython.Build import cythonize
from setuptools import setup, Extension


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


ext_modules = [Extension("algorithms.arithmetic.fib", ["algorithms/arithmetic/fib.pyx"])]
setup(
    name="python_algorithms",
    version="0.0.1",
    author="Arseniy Antonov",
    author_email="arseny.antonov@gmail.com",
    description=("Python algorithms"),
    license="MIT",
    keywords="algorithms graph arithmetic cython",
    packages=['algorithms', 'tests'],
    long_description=read('README.rst'),
    ext_modules=cythonize(ext_modules),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],

)
