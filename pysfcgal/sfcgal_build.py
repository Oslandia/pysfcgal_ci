import os
import platform
from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source(
    "pysfcgal._sfcgal",
    r"""
#include <stdlib.h>
#include <SFCGAL/capi/sfcgal_c.h>
""",
    libraries=[
        "SFCGAL" if "SFCGAL_LIBNAME" not in os.environ else os.environ["SFCGAL_LIBNAME"]
    ],
    library_dirs=[]
    if "LIBPATH" not in os.environ
    else os.environ["LIBPATH"].split(os.pathsep),
    include_dirs=[]
    if "INCLUDE_PATH" not in os.environ
    else os.environ["INCLUDE_PATH"].split(os.pathsep),
)

# Required until Alpha Shapes bug is not fixed on MSVC
compiler = platform.python_compiler()

sfcgal_c_file = "sfcgal_def_msvc.c" if ('MSC' in compiler) else "sfcgal_def.c"

with open(os.path.join(os.path.dirname(__file__), sfcgal_c_file), "r") as f:
    sfcgal_def = f.read()

ffibuilder.cdef(sfcgal_def)

if __name__ == "__main__":
    help(ffibuilder.compile)
    ffibuilder.compile(verbose=True)
