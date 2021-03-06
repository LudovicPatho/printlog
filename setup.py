from setuptools import setup
import printlog
import os

setup(
    name = 'printlog',
    packages = ['printlog'],
    version = printlog.__version__,
    author = 'Patho Ludovic',
    author_email = 'ludovic.patho@gmail.com',
    maintainer = 'Ludovic Patho',
    maintainer_email = 'ludovic.patho@gmail.com',
    keywords = 'colour print log',
    license = 'GPL V3',
    platforms = 'ALL',
    description = 'Colorize your logs to spot them at a glance.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    classifiers = [
        'Topic :: Utilities',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: Debuggers'
    ]
)