from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='cuansignal',
  version='1.1.1',
  description='A tool to predict when to buy or sell stocks',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/hisjam/cuansignal',  
  author='Achmad Hisyam',
  author_email='achmadhisyam@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Exponential Moving Average, Relative Strength Index, Stochastic, Bollinger Band,', 
  packages=find_packages(),
  install_requires=[''] 
)