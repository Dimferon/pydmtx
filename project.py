# This is the PyDmtx build script.
#
# Copyring (c) 2025 Dmitriy Strahov <dimka_strahov@mail.ru>
#
# This file is part of PyDmtx.

import glob
import os
import sys
import subprocess

from sipbuild import (Buildable, BuildableModule, Installable, Option,
        UserException, Project, Bindings, BuildableBindings, Builder)

# The min sip module ABI version needed.
ABI_VERSION = '12.11'

class PyDmtxProject(Project):
    """docstring for PyDmtxProject."""
    def __init__(self):
        """Initial the project."""
        super().__init__(abi_version=ABI_VERSION, sip_module="PyDmtx.sip")
        self.sip_files_dir = os.path.abspath(os.path.join(self.root_dir, 'sip'))

    def get_options(self):
        """ Return the sequence of configurable options. """

        # Get the standard options.
        options = super().get_options()

        # Add our new options.
        inc_dir_option = Option('dmtxwrapper_include_dir',
                help="the directory containing dmtxwrapper.h", metavar="DIR")
        options.append(inc_dir_option)

        lib_dir_option = Option('dmtxwrapper_library_dir',
                help="the directory containing the dmtxwrapper library",
                metavar="DIR")
        options.append(lib_dir_option)

        return options
    
    def apply_user_defaults(self, tool):
        """ Apply any user defaults. """

        # Ensure any user supplied include directory is an absolute path.
        if self.dmtxwrapper_include_dir is not None:
            self.dmtxwrapper_include_dir = os.path.abspath(self.dmtxwrapper_include_dir)

        # Ensure any user supplied library directory is an absolute path.
        if self.dmtxwrapper_library_dir is not None:
            self.dmtxwrapper_library_dir = os.path.abspath(self.dmtxwrapper_library_dir)

        # Apply the defaults for the standard options.
        super().apply_user_defaults(tool)

    def update(self, tool):
        """ Update the project configuration. """

        # Get the fib bindings object.
        fib_bindings = self.bindings['dmtxwrapper']

        # Use any user supplied include directory.
        if self.dmtxwrapper_include_dir is not None:
            fib_bindings.include_dirs = [self.dmtxwrapper_include_dir]

        # Use any user supplied library directory.
        if self.dmtxwrapper_library_dir is not None:
            fib_bindings.library_dirs = [self.dmtxwrapper_library_dir]

    def _build_dmtx(self):
        name = str(self.name).lower
        target_name = name
        print(target_name)
        
        cwd = os.path.abspath(self.project.root_dir);
        self.progress("Cmake configurate {0} ".format(name))
        subprocess.Popen(['cmake', '-S', '3rdparty/libdmtx', '-B', 'bin/Dmtx/libdmtx'], cwd=cwd, capture_output=True, check=True).wait();
        self.progress("Make build {0} ".format(name))
        subprocess.Popen(['cmake', '-S', 'dmtxwrapper', '-B', 'bin/dmtxwrapper'], cwd=cwd, capture_output=True, check=True).wait()

         # Check we have a shared interpreter library.
        if not self.py_pylib_shlib:
            self.progress("The {0} plugin was disabled because a shared Python library couldn't be found.".format(name))
            return     

        # Create the buildable and add it to the builder.
        buildable = Buildable(self, self.name)
        self.buildables.append(buildable)

        # The platform-specific name of the plugin file.
        
        if self.py_platform == 'win32':
            target_name = target_name  + '.dll'
        elif self.py_platform == 'darwin':
            target_name = 'lib' + target_name + '.dylib'
        else:
            target_name = 'lib' + target_name + '.so'

        # Create the corresponding installable.
        installable = Installable(target_name, name)
        buildable.installables.append(installable)

        # Create the .pro file.
        self.progress(
                "Generating the {0} file".format(target_name))

        root_plugin_dir = os.path.join(self.root_dir, name)