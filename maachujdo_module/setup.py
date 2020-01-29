import setuptools
from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name='maachujdo',
        version='1.1.35',
        url='https://github.com/nu11secur1ty/maachujdo',
        author='Ventsislav Varbanovski @nu11secur1ty',
        author_email='venvaropt@gmail.com',
        description="HTTP Sniff Login",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license='MIT',
        packages=['maachujdo'],
        zip_safe=False,
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
        python_requires='>=3.7',

        entry_points = {
          'console_scripts': ['cool-cmd=maachujdo.__main__:main'],
      }
)
