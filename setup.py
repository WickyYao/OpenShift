from setuptools import setup

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Wicky Yao',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask>=0.7.2',
                        'flask-babel',
                        'flask-wtf',
                        'markdown',
                        'flup',
                        'redis'],
     )
