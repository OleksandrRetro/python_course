import importlib.resources


class ImportLibTask(object):
    """
    Using library [importlib] crate a function to return package path if it installed,
    and [Package not found.] if not.
    """

    @staticmethod
    def get_package_path(package_name: str) -> str:
        try:
            return str(importlib.resources.files(package_name))
        except ModuleNotFoundError:
            return f"Package [{package_name}] not found."


if __name__ == '__main__':
    print(ImportLibTask.get_package_path("importlib"))
    print(ImportLibTask.get_package_path("adsfas123dgfa"))
