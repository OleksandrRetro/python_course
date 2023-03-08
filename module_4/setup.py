from distutils.core import setup

"""
Create [setup.py] file to install the project.
"""

setup(name='Python_Course',
      version='1.0',
      description='Python course description here.',
      author='Some Person',
      author_email='some@user.email',
      packages=['module_2',
                'module_3',
                'module_4',
                'utils'
                ],
      )

# python module_4/setup.py sdist
# python module_4/setup.py install
# pip uninstall Python-Course
