from setuptools import setup

setup(
    name='normal_forms',
    version='0.3',
    description='Normal forms of dynamical systems',
    keywords='normal form differential equation dynamical system bifurcation',
    url='https://joepatmckenna.github.io/normal_forms/html',
    author='Joseph P. McKenna',
    author_email='joepatmckenna@gmail.com',
    license='MIT',
    packages=['normal_forms'],
    install_requires=['numpy', 'sympy','copy'],
    zip_safe=False)
