import os
import imp
import pkg_resources

def __bootstrap__():
    global __bootstrap__, __loader__, __file__

    dll_path = os.path.join('build', 'lib.linux-x86_64-cpython-310', 'RegionGrowth.cpython-310-x86_64-linux-gnu.so') 
    __file__ = pkg_resources.resource_filename(__package__, dll_path)
    __loader__ = None; del __bootstrap__, __loader__
    imp.load_dynamic(__name__,__file__)
__bootstrap__()
