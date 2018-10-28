import importlib
import sys


class ModuleImporter:
    '''
    The ModuleImporter makes loading packages/modules from custom locations easier.
    Input Params:
        MODULE_PATH = '/path/to/module'. Note that spaces dont need to escaped
        MODULE_NAME = 'Name of module'
    Usage:
        the_module = ModuleImporter.module
    '''
    def __init__(self, MODULE_PATH, MODULE_NAME):
        self.MODULE_PATH = MODULE_PATH
        self.MODULE_NAME = MODULE_NAME
        self.IS_PACKAGE = True
        if self.MODULE_PATH.split('/')[-1] != '__init__.py':
            self.IS_PACKAGE = False
        spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
        module = importlib.util.module_from_spec(spec)
        if self.IS_PACKAGE:
            sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        self.module = module

        print(self.module)

    def module(self):
        return self.module
