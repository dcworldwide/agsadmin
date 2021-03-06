from setuptools import setup, find_packages

with open('agsadmin/_version.py') as fin: exec(fin)
with open('requirements.txt') as fin: requirements = [s.strip() for s in fin.readlines()]
with open('README.rst') as fin: long_description = fin.read()

packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
	
setup(
    name = "agsadmin",
    version = __version__,
    packages = packages,
    
    #dependencies
    install_requires = requirements,
    
    #misc files to include
    package_data = {
        "": ["LICENSE"]
    },
    
    #PyPI MetaData
    author = __author__,
    description = "ArcGIS Server REST Admin API Proxy",
    long_description = long_description,
    license = "BSD 3-Clause",
    keywords = "arcgis esri",
    url = "https://github.com/DavidWhittingham/agsadmin",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7"
    ),
    
    zip_safe = False
)
