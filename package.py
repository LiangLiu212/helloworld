# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install helloworld
#
# You can edit this file again by typing:
#
#     spack edit helloworld
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
import os
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Helloworld(CMakePackage):
    """Hellow, world! package used to learn the packaging in spack."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/LiangLiu212/helloworld"
    url = "https://github.com/LiangLiu212/helloworld/archive/refs/tags/V-1.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("Liang Liu")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.0", sha256="725351a0d6588a2c5d6896ee30f476cdf0d6305d63994f8047a6c16f2700fcc4")

    depends_on("cmake@3.31:", type="build")

    #depends_on("gcc", type="build")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    def setup_build_environment(self, env):
        gcc_prefix = self.spec["gcc"].prefix
        env.set("CC", os.path.join(gcc_prefix.bin, "gcc"))
        env.set("CXX", os.path.join(gcc_prefix.bin, "g++"))

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
