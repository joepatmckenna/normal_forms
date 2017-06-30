from setuptools import setup

setup(
    name='normal_forms',
    version='0.1',
    description='Normal forms of dynamical systems',
    url='https://github.com/joepatmckenna/normal',
    author='Joseph P. McKenna',
    author_email='joepatmckenna@gmail.com',
    license='MIT',
    packages=['normal_forms'],
    install_requires=['numpy', 'sympy'],
    zip_safe=False)
