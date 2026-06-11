from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *

class W2rapContigger(CMakePackage):
    """An Illumina PE genome contig assembler, can handle large (17Gbp)
    complex (hexaploid) genomes."""

    homepage = 'https://bioinfologics.github.io'
    git = 'https://github.com/bioinfologics/w2rap-contigger.git'
    url = 'https://github.com/bioinfologics/w2rap-contigger/archive/refs/heads/master.zip'

    license("MIT")

    version("master", branch="master")
    # depends_on("cmake", type=("build"))
    depends_on("cmake@3.30.9", type=("build"))
    # depends_on("gcc@12.2.0", type=("build"))
    depends_on("gcc", type=("build"))
    depends_on("jemalloc", type=("build", "run"))

    def cmake_args(self):
        return ["-DCMAKE_CXX_COMPILER=g++"]

    def make(self, spec, prefix):
        args = ["j", "4"]
        make(*args)
