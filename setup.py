# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages
from os.path import join, abspath, dirname, normpath

with open(join(dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(join(dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

tests_require = ["edc_test_utils"]
with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    for line in f:
        tests_require.append(line.strip())

# allow setup.py to be run from any path
os.chdir(normpath(join(abspath(__file__), os.pardir)))

setup(
    name='meta-ae',
    version=VERSION,
    author=u'Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/meta-trialtrial/meta-ae',
    license='GPL license, see LICENSE',
    description='Adverse Event models and handling.',
    long_description=README,
    zip_safe=False,
    keywords='django meta adverse event',
    install_requires=[
        #         'meta-lists',
        #         'meta-permissions',
        #         'meta-prn',
        #         'meta-rando',
        #         'meta-sites',
        #         'meta-subject',
        'django-collect-offline',
        'django-collect-offline-files',
        'edc-action-item',
        'edc-form-describer',
        'edc-reportable',
        'edc-subject-dashboard',
        'edc_metadata',
        'edc_model',
        'edc_notification',
        'edc_sites',
        'edc_utils',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires=">=3.7",
    tests_require=tests_require,
    test_suite='runtests.main',
)
