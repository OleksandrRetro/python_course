import argparse
import importlib.resources
import logging
from pathlib import Path


class LoggingAndArgParse:
    """
    Logging config class.
    """

    def __add_stream_handler(self, logger: logging, log_level: logging = logging.DEBUG) -> logging:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
        stream_handler.setLevel(log_level)
        logger.addHandler(stream_handler)
        return logger

    def __add_file_handler(self, logger: logging, log_path: Path, log_level: logging = logging.INFO) -> logging:
        file_handler = logging.FileHandler(log_path, mode='w')
        file_handler.setFormatter(logging.Formatter(
            fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M'))
        file_handler.setLevel(log_level)
        logger.addHandler(file_handler)
        return logger

    def create_logger(self, root_dir: Path, caller_name: str, log_levels: dict) -> logging:
        log_path = root_dir / f'{caller_name}.log'
        logger = logging.getLogger(caller_name)
        logger.setLevel(logging.DEBUG)
        self.__add_file_handler(logger=logger, log_path=log_path, log_level=log_levels['file_level'])
        self.__add_stream_handler(logger=logger, log_level=log_levels['console_level'])
        return logger


class ImportLibTask3:
    """
    [Importlib task]
    Using library [importlib] crate a function to return package path if it installed,
    and [Package not found.] if not.

    Create logging in console and in file at the same time for [Importlib task].
    If package not found - ERROR level.
    If package was found - package description (method __doc__) in WARNING, path in INFO, version in DEBUG.
    Use [argparse] library to set the log level for console and file independently.
    """

    def get_package_path(self, package_name: str) -> str:
        log = ImportLibTask3.log_init()
        try:
            log.info(importlib.resources.files(package_name))
            log.debug(importlib.resources.files(package_name))
            log.warning(package_name.__doc__)
            log.error("error - class")
            return str(importlib.resources.files(package_name))
        except ModuleNotFoundError:
            log.error(f"Package [{package_name}] not found.")
            return f"Package [{package_name}] not found."

    @staticmethod
    def log_init() -> logging:
        levels: dict = {
            'critical': logging.CRITICAL,
            'error': logging.ERROR,
            'warn': logging.WARNING,
            'warning': logging.WARNING,
            'info': logging.INFO,
            'debug': logging.DEBUG
        }
        parser = argparse.ArgumentParser(description='Log levels parser from terminal.')
        parser.add_argument('-fl', '--file_level', help='File log level.', choices=levels.keys(), required=True)
        parser.add_argument('-cl', '--console_level', help='Console log level.', choices=levels.keys(), required=True)
        args: dict = vars(parser.parse_args())
        args['file_level'] = levels.get(args['file_level'].lower())
        args['console_level'] = levels.get(args['console_level'].lower())
        return LoggingAndArgParse().create_logger(Path.cwd(), ImportLibTask3.__name__, args)


if __name__ == '__main__':
    # Run from current folder using command - python task_3.py -fl=debug -cl=info
    ImportLibTask3().get_package_path("importlib")


