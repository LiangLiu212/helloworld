# Using spack to install HelloWorld

This `HelloWorld` project is written in `c++` and compiled by `cmake`. You can install it outside `spack` by

```
$ git clone https://github.com/LiangLiu212/helloworld.git
$ mkdir build install
$ cd build
$ cmake ../helloworld -DCMAKE_INSTALL_PREFIX=/path/to/instll
$ make && make install
```

## Create a package for `HelloWorld`

- You need to fork spack-packages, and clone it from your reposi
```
$ spack create https://github.com/LiangLiu212/helloworld/archive/refs/tags/V-1.0.tar.gz
```
- Then configure Spack to use your local repository:
```
$ spack repo set --destination ~/spack-packages builtin
$ spack repo ls
[+] builtin    v2.2    /root/spack/spack-packages/repos/spack_repo/builtin
```

- Create a packaging for `HelloWorld`

```
$ spack create https://github.com/LiangLiu212/helloworld/archive/refs/tags/V-1.0.tar.gz
```

- Edit the spack package by
```
$ spack edit helloworld
```
- Install the spack package by 
```
$ spack install helloworld
```