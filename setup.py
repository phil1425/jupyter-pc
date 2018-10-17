from setuptools import setup


setup(name='jupyterpc',
      version='0.1.5',
      description='Some Functions for making Tables and Graphics in Jupyter',
      url='https://github.com/phil1425/jupyter-pc',
      author='Philipp Kollenz',
      author_email='philipp.kollenz@bombombox.net',
      license='MIT',
      install_requires=['uncertainties', 'scipy', 'jinja2', 'numpy'],
      packages=['jupyterpc'],
      zip_safe=False)
