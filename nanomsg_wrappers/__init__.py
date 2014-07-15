from __future__ import division, absolute_import, print_function, unicode_literals

from platform import python_implementation
import pkgutil
import sys
import warnings

_choice = None

def set_wrapper_choice(name):
    global _choice
    _choice = name

def _imp(name):
    __import__(name)
    return sys.modules[name]

def load_wrapper():
    if _choice is not None:
        return _imp('_nanomsg_' + _choice)
    default = get_default_for_platform()
    try:
        return _imp('_nanomsg_' + default)
    except ImportError:
        warnings.warn(("Could not load the default wrapper for your platform: "
                       "%s, performance may be affected!") % (default,))
    return _imp('_nanomsg_ctypes')

def get_default_for_platform():
    if python_implementation() == 'CPython':
        return 'cpy'
    else:
        return 'ctypes'


def list_wrappers():
    return [module_name.split('_',2)[-1] for _, module_name, _ in
     pkgutil.iter_modules() if module_name.startswith('_nanomsg_')]
