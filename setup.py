from setuptools import setup

setup(name='pywp',
      version='1.0.2',
      description='Command line utilities to install WordPress.',
      author="Sohail Ahmed",
      author_email="meetsohailahmed@gmail.com",
      url="https://github.com/meetsohail/pywp",
      license="MIT",
      entry_points={
          'console_scripts': [
              'pywp = pywp.pywp:main'
          ],
      },
      packages=[
          'pywp'
      ],
      install_requires=[]
      )
