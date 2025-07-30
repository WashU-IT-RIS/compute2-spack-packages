# ucx

### Summary
Currently everything in this directory is directly copied from the builtin repo of Spack v1.0-beta (the develop branch on GitHub). This was with the aim of bumping our UCX version up slightly to the latest stable before the Spack v1.0 release. 

This change is not expected to be needed when Spack v1.0 goes live. The entire UCX directory can be deleted at that time.

### Quick-Start

1. View package information
    ```bash
    # default version (highest version)
    spack info ucx
    # ris repo
    spack info ris.ucx
    # builtin repo
    spack info builtin.ucx
    ```

1. Install package from specific repo
    ```bash
    spack install ris.ucx
    ```
