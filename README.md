# compute2-spack-packages
Primary RIS Spack package repository


## Summary
This repository is designed to be consumed directly via URL by Spack v1.0+ as a remote [Git-based Repository](https://spack.readthedocs.io/en/latest/repositories.html#git-based-repositories).

It is structured as a mono-repo to allow easier tracking of any needed packages for compute2 domains other than RIS.

## Quick-Start

1. Add the repository
    ```
    spack repo add --name compute2-spack-packages https://github.com/washu-it-ris/compute2-spack-packages.git
    ```
1. Update local cache
    ```
    spack repo update
    ```
1. Confirm repos now show up
   ```
   spack repo list
   ```
   ```
   [root@519139a6a2a5 ~]# spack repo list
   [+] washu_it_ris.ris    v2.0    /root/.spack/package_repos/aozlvq7/repos/spack_repo/washu_it_ris/ris
   [+] builtin             v2.2    /root/.spack/package_repos/fncqgg4/repos/spack_repo/builtin
   ```
