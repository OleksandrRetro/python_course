import importlib.resources


class ImportLibTask:
    """
    Using library [importlib] crate a function to return package path if it installed,
    and [Package not found.] if not.
    """

    def get_package_path(self, package_name: str) -> str:
        try:
            return str(importlib.resources.files(package_name))
        except ModuleNotFoundError:
            return f"Package [{package_name}] not found."


if __name__ == '__main__':
    instance: ImportLibTask = ImportLibTask()
    print(instance.get_package_path("importlib"))
    print(instance.get_package_path("adsfas123dgfa"))
