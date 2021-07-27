from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name = 'pynode_next',
    version = '0.1.0',
    author_email="darcy@darcylf.me",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ehne/PyNode-Next",
    packages = ['pynode_next'],
    install_requires=[
        'algorithmX',
    ],
    python_requires='>=3',
)

# notes so that e remembers how to do pypi
# 1. make sure you've got the env open
# 2. run python3 setup.py bdist_wheel
# 3a. to test, run pip install . 
# 3b. to publish, run twine upload --skip-existing dist/*