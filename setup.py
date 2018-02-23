# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='foo',
    version='0.0.0',
    extras_require={'testing': ['pytest >= 3.0.0',
                                    'pytest-cov',
                                    'pytest-timeout',
                                    'pytest-xdist'],
                        'docs': ['sphinx >= 1.6.3, < 2',
                                 'towncrier >= 17.8.0']}

)

