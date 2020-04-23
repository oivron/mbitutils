import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mbitutils",
    version="0.0.2",
    author="Øivind Rønning, Statped",
    author_email="oiron@statped.no",
    description="Extra modules for the BBC micro:bit and Bit:bot.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oivron/mbitutils",
    packages=setuptools.find_packages(include=['bitbot', 'music', 'speech']),
    classifiers=[
        "Development Status :: 3 - Alpha"
        "Intended Audience :: Education"
        "Operating System :: Microsoft :: Windows :: Windows 10"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='micro:bit Bit:bot',
    #package_dir={'': 'mbitutils'},
    py_modules=['bitbot', 'music', 'speech'],
    python_requires='>=3.6',
    install_requires=['uflash', 'microfs', 'pylint'],
)