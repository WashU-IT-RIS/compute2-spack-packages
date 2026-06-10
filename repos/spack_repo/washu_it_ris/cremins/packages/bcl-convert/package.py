# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import subprocess
from spack.package import *


class BclConvert(Package):
    """The Illumina BCL Convert is a standalone local software app
    that converts the Binary Base Call (BCL) files produced by Illumina sequencing systems
    to FASTQ files.

    BCL Convert also provides adapter handling (through masking and trimming) and
    UMI trimming and produces metric outputs."""

    homepage = "https://support.illumina.com/sequencing/sequencing_software/bcl-convert.html"
    # Add EULA / License declaration
    license_url = "https://www.illumina.com/content/dam/illumina-marketing/documents/terms-conditions/united-states/illumina-software-subscription-agreement_11-08-2024.pdf"

    version(
        "3.8.2",
        sha256 = "f3ef20cd67ce8f076faec865b1d16e31081ae1ed71a8b2ed1d1a20c765764185",
        url = "https://support.illumina.com/content/dam/illumina-support/documents/downloads/software/BCLConvert/v3/bcl-convert-3.8.2_12_g85770e0b-2.el7.x86_64.rpm",
        expand = False,
    )

    def install(self, spec, prefix):
        rpm_file = self.stage.archive_file
        if not rpm_file or not os.path.exists(rpm_file):
            raise InstallError("No RPM archive file found in the Spack stage")

        mkdirp(prefix)
        print(f"Extracting {rpm_file} to {prefix} using rpm2cpio and cpio...")

        rpm_proc = subprocess.Popen(["rpm2cpio", rpm_file], stdout=subprocess.PIPE)
        cpio_proc = subprocess.Popen(
            ["cpio", "-idmv", "-D", str(prefix)],
            stdin=rpm_proc.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )   

        rpm_proc.stdout.close()
        _, cpio_stderr = cpio_proc.communicate()
        rpm_rc = rpm_proc.wait()

        if rpm_rc != 0:
            raise InstallError(f"rpm2cpio failed with exit code {rpm_rc}")
        if cpio_proc.returncode != 0:
            raise InstallError(
                "cpio extraction failed with exit code {0}: {1}".format(
                    cpio_proc.returncode, cpio_stderr.strip()
                )
            )

        source_bin = os.path.join(prefix, "usr", "bin")
        target_bin = os.path.join(prefix, "bin")
        if not os.path.isdir(source_bin):
            raise InstallError("Expected directory missing after extraction: {0}".format(source_bin))
        if not os.path.lexists(target_bin):
            os.symlink(source_bin, target_bin)

