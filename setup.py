# !/usr/bin/env python

# 
# (C) Copyright IBM Corporation 2013
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the Eclipse Public License.
# 
import os
import sys
from setuptools import setup, Extension

includeDir = os.path.join(sys.prefix, 'include')
includeDirs = [i for i in (os.path.join(includeDir, i) for i in os.listdir(includeDir)) if os.path.isdir(i)] + [includeDir]
setup(name='pythonlsf',
      version='1.0.1',
      description='Python binding for Platform LSF APIs',
      license='LGPL',
      keywords='LSF,Grid,Cluster,HPC',
      url='http://www.platform.com',
      ext_package='pythonlsf',
      ext_modules=[Extension('_lsf', ['pythonlsf/lsf.i'],
                             include_dirs=includeDirs,
                             library_dirs=[os.environ['LSF_LIBDIR']],
                             swig_opts=['-I' + os.environ['LSF_LIBDIR'] + '/../../include/lsf/'],
                             extra_compile_args=['-m64', '-I' + os.environ['LSF_LIBDIR'] + '/../../include/lsf/'],
                             extra_link_args=['-m64'],
                             libraries=['c', 'nsl', 'lsbstream', 'lsf', 'bat', 'rt',
                                        'fairshareadjust'])],
      py_modules=['pythonlsf.lsf'],
      classifiers=["Development Status :: 2 - Pre-Alpha",
                   "License :: OSI Approved :: Eclipse Public License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Internet",
                   "Topic :: Scientific/Engineering",
                   "Topic :: Software Development",
                   "Topic :: System :: Distributed Computing",
                   "Topic :: Utilities",
                   ],
      )
