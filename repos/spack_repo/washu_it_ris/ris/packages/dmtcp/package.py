# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Dmtcp(Package):
    """DMTCP (Distributed MultiThreaded Checkpointing) transparently
    checkpoints a single-host or distributed computation in user-space --
    with no modifications to user code or to the O/S."""

    homepage = "https://dmtcp.sourceforge.net/"
    #url = "file:////storage2/fs1/RIS-Services/Active/compute2-public/spack/mirrors/dmtcp/dmtcp-4.0.0-x8664.tgz"
    manual_download = True

    license("LGPL-3.0-only")

    maintainers("jcaroline")
    version("4.0.0", sha256="eeb09d51891ae2dc7b625ce36c55a77a7b672ac6987c104e70cdb82782339e9e")

    def url_for_version(self, version):
        return "file://{0}/dmtcp-{1}-x8664.tgz".format(os.getcwd(), version)
    
    def install(self, spec, prefix):
        # This manually copies your pre-built files into the Spack prefix
        install_tree(".", prefix)
