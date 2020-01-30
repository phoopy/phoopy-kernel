# Documentation

## Usage

## Methods

### _Kernel.\_\_init\_\_(environment, debug)_
Constructor
```python
from phoopy.kernel import Kernel

kernel = Kernel('dev', True)
```

### _Kernel.get_environment()_
```python
from phoopy.kernel import Kernel

kernel = Kernel('dev', True)
kernel.get_environment() # ~> dev
```

### _Kernel.boot()_
```python
from phoopy.kernel import Kernel

kernel = Kernel('dev', True)
kernel.boot()
```

### _Kernel.get_root_dir()_
Returns the `root` directory

### _Kernel.get_app_dir()_
Returns the `app` directory

### _Kernel.get_var_dir()_
Returns the `var` directory

### _Kernel.get_parameter(key)_
Returns the parameters as dict

### _Kernel.get_container()_
Returns the Container object

### _Container.\_\_init\_\_()_
```python
from phoopy.kernel import Container

container = Container()
```

### _Container.\_\_setitem\_\_(key, item)_
Add a container item
```python
from phoopy.kernel import Container

container = Container()
container['hello_world'] = lambda container: 'Hello World'
```

### _Container.keys()_
Returns all keys

### _Container.get(key)_
Returns a container item or Raise an exception

### _Container.get_tagged_entries(tag_name)_
Returns all container items that has a given tag

### _Bundle.\_\_init\_\_()_
```python
from phoopy.kernel import Bundle

bundle = Bundle()
```

### _Bundle.get_name()_
Returns the Bundle Class name

### _Bundle.get_bundle_dir()_
Returns the Bundle root directory

### _Bundle.service_path()_
Should be implemented in order to return a service path if it is necessary

### _Bundle.set_kernel(_kernel)_
Set Kernel

### _Bundle.get_kernel(_kernel)_
Get Kernel

### _Bundle.set_container(_container)_
Set Container

### _Bundle.get_container()_
Get Container

### _Bundle.setup()_
Should be implemented in order to setup some needed stuff it it is necessary
