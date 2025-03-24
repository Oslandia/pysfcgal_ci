# Installation

## Install with pip

PySFCGAL is now accessible on the [Python Package Index (PyPI)](https://pypi.org/project/PySFCGAL/). You can install it in a Python virtual environment. For example, on Debian or Ubuntu systems, you might use the following steps:

- Create and activate a virtual environment
- Use pip to install PySFCGAL from PyPI

```bash
python -m .venv
source .venv/bin/activate
pip install pysfcgal
```

## Install from scratch

### Build dependencies

The dependencies required for the build are:

- gmp
- boost
- mpfr
- cmake
- cgal*

Install SFCGAL with your package manager (apt, yum, pacman, pkg, etc) or with the sources if your system doesn't offer the package.

Example for debian/ubuntu users:

```shell
apt install -y cmake libgmp-dev libmpfr-dev libboost-dev libboost-timer-dev libboost-test-dev
```

### CGAL

To be done if your distribution does not provide the updated package (minimum `5.6`), otherwise you can skip this step.

```shell
wget "https://github.com/CGAL/cgal/releases/download/v5.6/CGAL-5.6.tar.xz" -O CGAL-5.6.tar.xz
tar xJf CGAL-5.6.tar.xz
```

Remember your path to CGAL - we'll need it later. Example: `/home/foo/CGAL-5.6`.

### SFCGAL

Clone [SFCGAL](https://gitlab.com/sfcgal/SFCGAL) and place yourself in the `SFCGAL` folder:

```shell
git clone git@gitlab.com:sfcgal/SFCGAL.git && cd SFCGAL
```

Then build SFCGAL considering the path to CGAL:

```shell
cmake -GNinja -S . -B build -DSFCGAL_BUILD_TESTS=ON -DCGAL_DIR=/home/foo/CGAL-5.6
cmake --build build
```

The build includes can be found here: `/home/foo/SFCGAL/build/src`

You may optionally install SFCGAL to your system through:

```shell
cmake --install build
```

### PySFCGAL

#### Build the python module

To start you have to clone [pysfcgal](https://gitlab.com/sfcgal/pysfcgal) and place yourself in the `pysfcgal` folder:

```shell
git clone git@gitlab.com:sfcgal/pysfcgal.git && cd pysfcgal
```

Then install the Python binding through:

```shell
env CFLAGS=-I/home/foo/SFCGAL/build/include LDFLAGS=-L/home/foo/SFCGAL/build/src python3 setup.py build install --user
```

Where:

- `LDFLAGS` is the path where to find `libSFCGAL.so`
- `CFLAGS` is the path where the build includes are located

#### Add the build source link of SFCGAL into the ld file (on Debian/Ubuntu)

The Pysfcgal installation ends with the modification of your `LD_LIBRARY_PATH` variable:

```shell
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/foo/SFCGAL/build/src
```

Alternatively, you may create a ldconfig file as follows:

```shell
echo "/home/foo/SFCGAL/build/src" >> /etc/ld.so.conf.d/sfcgal.conf
```

and run this command to apply the changes:

```shell
sudo ldconfig
```

## How to build the documentation?

The project documentation is built with [MkDocs](https://www.mkdocs.org/).

You may built it locally by doing:

```bash
pip install -r requirements/documentation.txt
cd docs
mkdocs serve  # Serving on http://127.0.0.1:8000/
```
