import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="relind8lib",
    version="1.0.0",
    author="Sequent Microsystems",
    author_email="evanone@163.com",
    description="A set of functions to control Sequent Microsystems 8-Relay board",
	license='MIT',
    url="https://www.sequentmicrosystems.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2/3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
