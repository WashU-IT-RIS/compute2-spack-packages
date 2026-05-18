# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack.package import *


class Basespace(Package):
    """The BaseSpace Sequence Hub CLI supports scripting and
    programmatic access to BaseSpace Sequence Hub for automation, bulk operations,
    and other routine functions.

    The BaseSpace CLI v1.0 and higher is supported by the illumina support team:
    techsupport@illumina.com.
    It can be used independently or in conjunction with BaseMount."""

    homepage = "https://developer.basespace.illumina.com"

    version(
        "1.7.0",
        sha256="c14413894d669f6d250bd8b7916760727f3136f874615665f9f8eb9c7600fad1",
        url="https://launch.basespace.illumina.com/CLI/latest/amd64-linux/bs",
        expand=False,
    )

    def install(self, spec, prefix):
        command_name = "bs"
        mkdirp(prefix.bin)
        install(command_name, prefix.bin)
        # Sets 755 (rwxr-xr-x)
        cmd = prefix.bin.join(command_name)
        os.chmod(cmd, 0o755)
