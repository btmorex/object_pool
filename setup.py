from setuptools import find_packages, setup

import object_pool

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = None

setup(name='object_pool',
      version=object_pool.__version__,
      description='thread-safe python object pool',
      long_description=long_description,
      author='Avery Fay',
      author_email='avery@shadypixel.com',
      url='https://github.com/btmorex/object_pool',
      packages=find_packages(),
      test_suite='object_pool.test',
      license='MIT')
