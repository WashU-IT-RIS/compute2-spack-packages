# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import subprocess

from spack.package import *

class Matlab(Package):
    """MATLAB (MATrix LABoratory) is a multi-paradigm numerical computing
    environment and fourth-generation programming language. A proprietary
    programming language developed by MathWorks, MATLAB allows matrix
    manipulations, plotting of functions and data, implementation of
    algorithms, creation of user interfaces, and interfacing with programs
    written in other languages, including C, C++, C#, Java, Fortran and Python.

    Note: MATLAB is licensed software. You will need to create an account on
    the MathWorks homepage and download MATLAB yourself. Spack will search your
    current directory for the download file. Alternatively, add this file to a
    mirror so that Spack can find it. For instructions on how to set up a
    mirror, see https://spack.readthedocs.io/en/latest/mirrors.html"""

    homepage = "https://www.mathworks.com/products/matlab.html"
    manual_download = True

    maintainers("ris")

    version("R2024b", sha256="65f2798a35212890801a91379d390a757a8e1768d41f1f07a63d5506ac10f9e6")  # update 5
    version("R2024a", sha256="d62123ebef6378a3f9c09dc5d92dd8220df091e3a7d4559fc918c698a05edcda")  # update 3
    version("R2019b", sha256="d60787263afb810283b7820c4c8d9cb1f854c7cb80f47e136643fd95bf5fbd59")
    version("R2018b", sha256="8cfcddd3878d3a69371c4e838773bcabf12aaf0362cc2e1ae7e8820845635cac")
    version("R2016b", sha256="a3121057b1905b132e5741de9f7f8350378592d84c5525faf3ec571620a336f2")
    version("R2015b", sha256="dead402960f4ab8f22debe8b28a402069166cd967d9dcca443f6c2940b00a783")

    variant(
        "mode",
        default="interactive",
        values=("interactive", "silent", "automated"),
        description="Installation mode (interactive, silent, or automated)",
    )

    variant(
        "key", default="<installation-key-here>", description="The file installation key to use"
    )

    # Licensing
    license_required = True
    license_comment = "#"
    license_files = ["licenses/license.dat"]
    license_vars = ["LM_LICENSE_FILE"]
    license_url = "https://www.mathworks.com/help/install/index.html"

    extendable = True

    def url_for_version(self, version):
        ris_mirror = "/storage2/fs1/RIS-Services/Active/compute2-private/spack/mirrors/matlab"
        return "file://{0}/matlab_{1}_glnxa64.zip".format(ris_mirror, version)

    def install(self, spec, prefix):
        config = {
            "destinationFolder": prefix,
            "mode": spec.variants["mode"].value,
            "fileInstallationKey": spec.variants["key"].value,
            "licensePath": self.global_license_file,
            "agreeToLicense": "yes",
        }

        # Store values requested by the installer in a file
        with open("spack_installer_input.txt", "w") as input_file:
            for key in config:
                input_file.write("{0}={1}\n".format(key, config[key]))

        # Run silent installation script
        # Full path required
        input_file = join_path(self.stage.source_path, "spack_installer_input.txt")
        subprocess.call(["./install", "-inputFile", input_file])

    # Unnecessary after 2023+
    # https://spackpm.slack.com/archives/C5W7NKZJT/p1695860122711089?thread_ts=1695848883.510809&cid=C5W7NKZJT
    #@run_after("install")
    #def post_install(self):
    #    # Fix broken link
    #    with working_dir(self.spec.prefix.bin.glnxa64):
    #        os.unlink("libSDL2.so")
    #        os.symlink("libSDL2-2.0.so.0.2.1", "libSDL2.so")

    #    # Fix to random exceptions when changing display settings
    #    # https://www.mathworks.com/matlabcentral/answers/373897-external-monitor-throws-java-exception
    #    java_opts = os.path.join(self.spec.prefix.bin.glnxa64, "java.opts")
    #    with open(java_opts, "w") as out:
    #        out.write("-Dsun.java2d.xrender=false\n")
