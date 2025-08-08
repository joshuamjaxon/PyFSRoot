# PyFSRoot

PyFSRoot is a simple module for importing the FSRoot macros implemented in C++ by remitche66 within Python. Macros are automatically discovered and loaded with ROOT's Python interface; they are then aliased so that they may be invoked within Python in a familiar and efficient way. In addition, PyFSRoot is packaged with several quality-of-life functions built on top of FSRoot and the ROOT data analysis framework in order to simplify repetitive tasks.

## Dependencies

PyFSRoot has two primary dependencies:
1. [ROOT](https://root.cern/install/): A data analysis framework geared towards particle physics.
2. [FSRoot](): A set of macros and executables for ROOT that evaluates strings to analyze data organized into exclusive and inclusive final states.

If you're here, you more than likely have these dependencies already. However, if you're having trouble, you may wish to verify that your software versions are correct. While PyFSRoot should run without issue so long as FSRoot and the ROOT Python interface are operational, compatibility issues between these two projects are a common source of errors. Details on FSRoot compatibility with a given ROOT version can be found in the FSRoot documentation [here](https://github.com/remitche66/FSRoot/blob/master/Documentation/FSRoot.pdf). Your current version of root can be found by running
```root-config --version``` 
in your terminal with ROOT installed. 

To run PyFSRoot, you'll need to ensure that FSRoot is compatible with your current version of ROOT, and that your current version of ROOT is compatible with your Python installation. To check which version of Python ROOT requires, run 
```root-config --python-version```
in your terminal. Your Python version may likewise be checked by running 
```python --version```. 
If these two version numbers mismatch, the ROOT Python interface is likely to fail. To remedy this, please install the appropriate version of Python alongside your current Python installation.

## Accessing the FSRoot Objects

Loading PyFSRoot is straightforward. With the fewest possible keystrokes, include the following in your Python program:
```import pyfsroot```
This will automatically load the ROOT Python interface and all FSRoot modules. Then, to create a histogram in ROOT, for example:
```h1 = pyfsroot.ROOT.TH1F(...)```
or in FSRoot:
```h2 = pyfsroot.ROOT.FSModeHistogram.getTH1F(...)```.

However, this approach is kind of a mouthful, and gets old quick when the backbone of your analysis is formed from ROOT and FSRoot objects. PyFSRoot aliases FSRoot functions so that they do not need to be access from the Python ROOT interface and can be accessed directly from pyfsroot:
```h2 = pyfsroot.FSModeHistogram.getTH1F()```.
While some care should be taken by the user to not forget that the FSRoot objects are attributes of the ROOT module, writing this over and over again makes analysis code tedious and best and difficult to read at worst. Moreover, it adds an additional barrier to entry for the new Python FSRoot user. By aliasing the FSRoot objects in this way, usage is immediately familiar to any C++ FSRoot user. Note how
```
from pyfsroot import FSModeHistogram
h = FSModeHistogram.getTH1F(...)
```
translates quite directly from
```
#include "FSMode/FSModeHistogram.h"
TH1F* h = FSModeHistogram::getTH1F(...);
```

Lastly, the user may wish to import all FSRoot objects at once, in much the same way that FSRoot is loaded in its entirety by the ROOT interpreter at startup. This is readily achieved with the standard Python import all syntax:
```from pyfsroot import *```
And note that this will even import ROOT as well.

Warning: The current version of PyFSRoot does not properly handle FSRoot classes which are declared in bulk under a single header whose name is not shared by the class contained within, such as the classes defined within the `FSFitFunctions.h` header. These classes are the exception, but they are still quite useable! Simply access them the more verbose way, e.g. with `ROOT.FSFitPOLY`.

## Accessing the Additional QOL Functions

PyFSRoot has a straightforward purpose: to reduce the time spent coding analyses, so the user can get on with the business of doing physics. There are many ways to achieve this, but not all of these ways align well with the design goals of FSRoot. Thus, additional quality-of-life functions built on top of FSRoot can be found in the various submodules PyFSRoot. The functions included here have demonstrated themselves to be useful time and again, and are ideal for saving time and space.  For example, `pyfsroot.utils` contains useful functions for plotting lines and boxes on top of existing canvases, and for redrawing axes whose ticks have been overwritten by other geometry. 