# jdk

### Summary

This `package.py` for the Oracle JDK was copied directly from v0.23.1 of Spack's builtin repo. This was **ONLY** done due to oracle's download links **ONLY** providing a link to the latest version.

The hash of the v21 of the JDK has changed since Spack was last updated. This is due to the expected version changing from 21.0.2 to something like 21.0.7+. It is unclear if this "issue" effects JDK 17 as well.

Expect to have to keep ammending this hash as Oracle JDK updates come out and we have to reinstall the Spack env.

### Quick-Start

1. View package information
    ```bash
    # default version (highest version)
    spack info jdk
    # ris repo
    spack info ris.jdk
    # builtin repo
    spack info builtin.jdk
    ```

1. Edit the version in the RIS repo if needed
    ```
    spack edit ris.jdk
    ```

1. Install package from specific repo
    ```bash
    spack install ris.jdk@21
    ```
