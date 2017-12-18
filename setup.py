from setuptools import setup, find_packages

setup(name='matze',
      version='0.1.0',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'matze = matze.backend.server:run'
          ]
      },
      )
