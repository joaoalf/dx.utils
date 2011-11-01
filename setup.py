# -*- coding: utf-8 -*-
# setup.py
from setuptools import setup

setup(
    name="dx.utils",
    version="1.0",
    description="dotX Utils",
    author=u"João Alfredo Gama Batista",
    author_email="joaoalf@dotx.com.br",
    url="http://www.dotx.com.br",
    namespace_packages=['dx',],
    package_dir={'': 'src'},
    include_package_data=True,
    py_modules=['dx.utils']
)
