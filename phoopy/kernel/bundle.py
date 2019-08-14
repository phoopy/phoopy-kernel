from os import path
import sys


class Bundle(object):
    def __init__(self):
        self.kernel = None
        self.container = None
        pass

    def get_name(self):
        return self.__class__.__name__

    def get_bundle_dir(self):
        return path.dirname(path.realpath(sys.modules[self.__class__.__module__].__file__))

    def service_path(self):
        # return an yaml file path
        pass

    def set_kernel(self, _kernel):
        self.kernel = _kernel

    def get_kernel(self, _kernel):
        return self.kernel

    def set_container(self, _container):
        self.container = _container

    def get_container(self):
        return self.container

    def setup(self):
        pass
