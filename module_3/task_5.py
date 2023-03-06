import os
import grp
import pwd

from prettytable import PrettyTable


class UnixLsLaOnPython(object):
    """
    Create analog of [Unix ls -la] using Python.
    Use [os.listdir], [os.stat], [pwd] and [grp]

    pip install prettytable
    Cell names: Mode, Owner, Group, Size, File name
    """

    @staticmethod
    def generate_table(data_list: list) -> None:
        table: PrettyTable = PrettyTable()
        table.field_names = ["Mode", "Owner", "Group", "Size", "File name"]
        for item in data_list:
            table.add_row(item)
        print(table)

    @staticmethod
    def do_ls_la():
        table_list: list = []
        for item in os.listdir('.'):
            file_info_list: list = []
            for st_mode in os.stat(item):
                file_info_list.append(st_mode)
                print(f"{item} - {st_mode}")

    @staticmethod
    def os_stat():
        stat_info = os.stat('/path')
        uid = stat_info.st_uid
        gid = stat_info.st_gid
        print(uid, gid)

        user = pwd.getpwuid(uid)[0]
        group = grp.getgrgid(gid)[0]
        print(user, group)


if __name__ == '__main__':
    # UnixLsLaOnPython.generate_table([["sdfs", "sdfs", "sdfs", "sdfs", "sdfs"]])
    UnixLsLaOnPython.os_stat()

