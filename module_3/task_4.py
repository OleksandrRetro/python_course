import fnmatch
import os


class UnixFindOnPython(object):
    """
    Create analog of [Unix find] using Python.
    Use [os.walk], [os.path.join], [fnmatch].
    Use shell-pattern
    """

    @staticmethod
    def list_files(file_path: str, file_pattern: str):
        for root, dirs, files in os.walk(file_path):
            for file_name in fnmatch.filter(files, file_pattern):
                print(os.path.join(root, file_name))


if __name__ == '__main__':
    root_dir: str = "../"
    pattern: str = "*.py"
    UnixFindOnPython().list_files(root_dir, pattern)
