import ROOT
import os
import glob

__all__ = [ "ROOT", "graphics" ]

FSROOT_DIR = os.path.expandvars("${FSROOT}")

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