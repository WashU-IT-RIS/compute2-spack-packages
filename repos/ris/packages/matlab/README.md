# matlab

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

