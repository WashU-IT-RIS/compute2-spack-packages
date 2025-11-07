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
    ```
   [root@519139a6a2a5 ~]# spack repo add --name compute2-spack-packages https://github.com/washu-it-ris/compute2-spack-packages.git
   remote: Enumerating objects: 21, done.
   remote: Counting objects: 100% (21/21), done.
   remote: Compressing objects: 100% (17/17), done.
   remote: Total 21 (delta 1), reused 14 (delta 0), pack-reused 0 (from 0)
   ==> Added repo to config with name 'compute2-spack-packages'.
   ```
1. Confirm repos now show up
   ```
   spack repo list
   ```
   ```
   [root@519139a6a2a5 ~]# spack repo list
   [+] washu_it_ris.ris       v2.0    /root/.spack/package_repos/aozlvq7/repos/spack_repo/washu_it_ris/ris
   [+] washu_it_ris.artsci    v2.0    /root/.spack/package_repos/aozlvq7/repos/spack_repo/washu_it_ris/artsci
   [+] builtin                v2.2    /root/.spack/package_repos/fncqgg4/repos/spack_repo/builtin
   ```
1. Update local cache as needed
    ```
    spack repo update
    ```
    ```
   [root@519139a6a2a5 ~]# spack repo update
   remote: Enumerating objects: 18, done.
   remote: Counting objects: 100% (18/18), done.
   remote: Compressing objects: 100% (7/7), done.
   remote: Total 11 (delta 1), reused 11 (delta 1), pack-reused 0 (from 0)
   ==> compute2-spack-packages: Updated sucessfully.
   ==> builtin: Already up to date.
    ```