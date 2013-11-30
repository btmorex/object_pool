from setuptools import find_packages, setup

import object_pool

setup(name='object_pool',
      version=object_pool.__version__,
      url='https://github.com/btmorex/object_pool',
      description='thread-safe python object pool',
      license='MIT',
      author='Avery Fay',
      author_email='avery@shadypixel.com',
      packages=find_packages(exclude=['object_pool.test']),
      test_suite='object_pool.test',
)
