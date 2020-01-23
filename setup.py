from setuptools import setup

setup(name="System-info",
      version="0.1",
      description="Basic system information for COMP30670",
      url="https://github.com/omijoshi09/System-info.git",
      author="Omkar Joshi",
      author_email="omkar.joshi@ucd.ie",
      licence="GPL3",
      packages=['System-info'],
      entry_points={
        'console_scripts':['comp30670_systeminfo=System-info.main:main']
        }
      )
