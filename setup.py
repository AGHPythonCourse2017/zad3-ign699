from setuptools import setup

setup(name='zad3',
      version='0.1',
      description='zad3',
      url='someurl',
      author='Jan Ignasik',
      author_email='mail@mail',
      license='MIT',
      packages=['zad3'],
      zip_safe=False,
      install_requires=[
          'requests',
          'bs4',
          'newspaper3k'
      ],
      include_package_data=True
)
