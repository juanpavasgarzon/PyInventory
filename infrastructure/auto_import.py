import importlib
import pkgutil


def auto_import_endpoints(package_name: str):
    for _, module_name, _ in pkgutil.iter_modules(importlib.import_module(package_name).__path__):
        full_module_name = f"{package_name}.{module_name}"
        importlib.import_module(full_module_name)
