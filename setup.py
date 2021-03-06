#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_namespace_packages

requirements = [
    'xbox-webapi>=1.1.8',
    'construct==2.10.56',
    'cryptography==2.8',
    'gevent==1.5a3',
    'dpkt',
    'marshmallow-objects',
    'Flask'
]

setup_requirements = [
    'pytest-runner'
]

test_requirements = [
    'pytest>=3'
]

setup(
    name="xbox-smartglass-core",
    version="1.2.2",
    author="OpenXbox",
    author_email="noreply@openxbox.org",
    description="A library to interact with the Xbox One gaming console via the SmartGlass protocol.",
    long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    long_description_content_type="text/x-rst",
    license="GPL",
    keywords="xbox one smartglass auxiliary fallout title stump tv streaming livetv rest api",
    url="https://github.com/OpenXbox/xbox-smartglass-core-python",
    python_requires=">=3.6",
    packages=find_namespace_packages(include=['xbox.*']),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=requirements,
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'xbox-cli=xbox.scripts.main_cli:main',
            'xbox-discover=xbox.scripts.main_cli:main_discover',
            'xbox-poweron=xbox.scripts.main_cli:main_poweron',
            'xbox-poweroff=xbox.scripts.main_cli:main_poweroff',
            'xbox-repl=xbox.scripts.main_cli:main_repl',
            'xbox-replserver=xbox.scripts.main_cli:main_replserver',
            'xbox-textinput=xbox.scripts.main_cli:main_textinput',
            'xbox-gamepadinput=xbox.scripts.main_cli:main_gamepadinput',
            'xbox-tui=xbox.scripts.main_cli:main_tui',
            'xbox-fo4-relay=xbox.scripts.main_cli:main_falloutrelay',
            'xbox-pcap=xbox.scripts.pcap:main',
            'xbox-recrypt=xbox.scripts.recrypt:main',
            'xbox-rest-server=xbox.scripts.rest_server:main'
        ]
    }
)
