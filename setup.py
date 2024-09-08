from setuptools import setup, find_packages

setup(
    name='totara',
    version='0.1.0',
    description='Totara paas client library for totara-paas-cli tool (tcs)',
    author='Totara-PaaS-team',
    author_email='totara-paas@totara.com',
    packages=find_packages(include=['totara', 'totara.misc']),
    install_requires=[
        'pytz~=2024.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
