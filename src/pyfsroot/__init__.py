import ROOT
import os
import glob
import platform

__all__ = [ "ROOT", "graphics" ]

FSROOT_DIR = os.path.expandvars("${FSROOT}")

if FSROOT_DIR == "${FSROOT}":
    raise EnvironmentError("Must have $FSROOT environment variable set!")

# Set the FSRoot load method. The methods are:
# (1) Load via many .so files. (Not compatible with macOS.)
# (2) Load via single .so file and many .h files. (Default, best compatibility)
# By default, use 2 if running on macOS, otherwise use 1 (should be faster)
FSROOT_LOAD_METHOD = 1
if platform.system() == "Darwin":
    FSROOT_LOAD_METHOD = 2

# Method 1: Load FSRoot using individual shared object libraries.
if FSROOT_LOAD_METHOD == 1:

    FSROOT_MODULES = glob.glob(os.path.join(FSROOT_DIR, "**/*_C.so"), recursive=True)

    for module in FSROOT_MODULES:
        # Load the module
        ROOT.gSystem.Load(module)
        # Add the module name to the list of globals. This will enable it to be 
        # imported in shorthand, allowing the user to import FSRoot classes in a
        # familiar way. So consider:
        #    from PyFSRoot import FSHistogram
        dir, fi = os.path.split(module)
        module_name = fi[:-5]
        try:
            globals()[module_name] = getattr(ROOT, module_name)
            __all__.append(module_name)
        except AttributeError:
            pass

# Method 2: Load FSRoot using a single shared object library. Required
# to function on macOS. This method requires an FSRoot version with a 
# commit hash more recent than d807cc763a7977dac17386725908c20816d8df5f.
elif FSROOT_LOAD_METHOD == 2:

    ROOT.gROOT.ProcessLine(f".include {FSROOT_DIR}")
    ROOT.gInterpreter.AddIncludePath(f"{FSROOT_DIR}")

    ROOT.gSystem.AddDynamicPath(f"{FSROOT_DIR}/lib")
    ROOT.gSystem.Load("libFSRoot.so")

    FSROOT_MODULES = glob.glob(os.path.join(FSROOT_DIR, "**/*.h"), recursive=True)

    for module in FSROOT_MODULES:
        # Include the module
        ROOT.gInterpreter.ProcessLine(f"#include \"{module}\"")
        # Add the module name to the list of globals. This will enable it to be 
        # imported in shorthand, allowing the user to import FSRoot classes in a
        # familiar way. So consider:
        #    from PyFSRoot import FSHistogram
        dir, fi = os.path.split(module)
        module_name = fi[:-2]
        try:
            globals()[module_name] = getattr(ROOT, module_name)
            __all__.append(module_name)
        except AttributeError:
            pass

else:
    raise ValueError("Invalid FSROOT_LOAD_METHOD. Only change this if you know what you are doing!")