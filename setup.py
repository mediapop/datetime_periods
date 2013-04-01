# -*- encoding: utf-8 -*-
from distutils.core import setup

setup(
    name='datetime_periods',
    version='1.0.0',
    url='https://github.com/mediapop/datetime_periods',
    author='Björn Andersson / Media Pop',
    author_email='bjorn@mediapop.co',
    description='Create time periods as easy as a snap with your finger',
    license='BSD',
    long_description=open('README.rst').read(),
    packages=['datetime_periods'],
    package_data={
        '': ['README.rst']
    },
    include_package_data=True,
    install_requires=[
        'python-dateutil>=2.1',
        'datetime_truncate>=1.0.0',
    ],
    test_suite='nose.collector',
    tests_require=['nose>=1.2.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
