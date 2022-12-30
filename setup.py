from setuptools import setup

setup(
    name='algolab',
    version='1.11',
    description='Algolab Python code for BIST trading',
    author='Atilla Yurtseven',
    author_email='quant@atilla.io',
    url='https://github.com/atillayurtseven/AlgoLab',
    packages=['algolab'],
    install_requires=['certifi==2022.9.24', 'charset-normalizer==2.1.1', 'idna==3.4', 'numpy==1.23.3', 'pandas==1.5.0', 'pycryptodome==3.16.0', 'python-dateutil==2.8.2', 'pytz==2022.4', 'requests==2.28.1', 'six==1.16.0', 'urllib3==1.26.12', 'websocket-client==1.4.1'],
)