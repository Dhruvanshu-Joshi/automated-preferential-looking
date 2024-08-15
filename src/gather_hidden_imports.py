import importlib
import pkgutil

def get_all_submodules(module_name):
    module = importlib.import_module(module_name)
    package_path = module.__path__
    submodules = []
    for importer, modname, ispkg in pkgutil.walk_packages(path=package_path, prefix=module_name + '.'):
        submodules.append(modname)
    return submodules

def gather_hidden_imports(requirements_file='requirements.txt'):
    hidden_imports = []
    with open(requirements_file, 'r') as f:
        packages = f.read().splitlines()
        for package in packages:
            try:
                submodules = get_all_submodules(package)
                hidden_imports.extend(submodules)
            except Exception as e:
                print(f"Could not import {package}: {e}")
    return hidden_imports

if __name__ == "__main__":
    hidden_imports = gather_hidden_imports()
    with open('hidden_imports.txt', 'w') as f:
        for imp in hidden_imports:
            f.write(f"{imp}\n")
