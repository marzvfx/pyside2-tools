import setuptools

with open('README.md') as fh:
    long_desc = fh.read()

setuptools.setup(
    name="pyside2-tools",
    version="2.0.1",
    author="Various",
    author_email="None",
    description="tools for PySide2",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)