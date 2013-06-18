# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


def read_relative_file(filename):
    """Returns contents of the given file, whose path is supposed relative
    to this module."""
    with open(join(dirname(abspath(__file__)), filename)) as f:
        return f.read()


LONG_DESC = "%s\r\n\r\n%s" % (read_relative_file('README.rst'),
                              read_relative_file('CHANGELOG'))


if __name__ == '__main__':  # ``import setup`` doesn't trigger setup().
    setup(name='django-runcommands',
          version=read_relative_file('VERSION').strip(),
          description="runcommands: execute system commands from views",
          long_description=LONG_DESC,
          classifiers=['Development Status :: 3 - Alpha',
                       'Environment :: Console',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: BSD License',
                       'Natural Language :: English',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 2',
                       'Programming Language :: Python :: 2.7',
                       'Programming Language :: Python :: 3',
                       'Programming Language :: Python :: 3.3',
                       ],
          keywords='system commands',
          author='Mathieu Agopian',
          author_email='mathieu.agopian@gmail.com',
          url='https://github.com/magopian/django-runcommands',
          license='BSD Licence',
          packages=find_packages(),
          include_package_data=True,
          zip_safe=False,
          install_requires=[]
    )
