# matlab

### Summary
The current matlab `package.py` file was copied from the v0.23.1 builtin Spack repo and modified to install from a central RIS repository. Normally the installation looks for install media within the user's `$HOME` dir.

Existing `*.patch` files are a work in progress attempt from @gunnarwustl to import the standard `package.py` from the builtin repo at runtime and patch it for RIS uses. This is in effort to maintain only the patch files rather than a discrete repository of Spack files.

### Quick-Start

1. View package information
    ```bash
    # default version (highest version)
    spack info matlab
    # ris repo
    spack info ris.matlab
    # builtin repo
    spack info builtin.matlab
    ```

1. Obtain the FIK (File Installation Key) relevant to the version you wish to install.

1. Install package from specific repo.
    ```bash
    # mode=silent allows for unattended install
    # <FILE_INSTALLATION_KEY> must be replaced witha valid FIK or install will fail
    spack install ris.matlab@<version> key=<FILE_INSTALLATION_KEY> mode=silent
    ```

