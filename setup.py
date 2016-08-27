from setuptools import find_packages, setup
from jsonquery import __version__

def read_file(path):
    result = []
    try:
        with open(path) as f:
            result = f.readlines()
    except Exception as err:
        pass
    return result

install_requires = read_file('requirements.txt')
tests_require = read_file('test-requirements.txt')

name = 'json-query'

setup(
    name=name,
    version=__version__,
    description='JSON Query tools',
    author='Alexey Dubkov',
    author_email='alexey.dubkov@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="jsonquery.tests",
    entry_points={
        "console_scripts":[
            'json-query = jsonquery.jsonquery:main',
        ]
    },
)
