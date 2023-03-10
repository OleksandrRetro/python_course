import os
import pwd

from prettytable import PrettyTable


class UnixLsLaOnPython:
    """
    Create analog of [Unix ls -la] using Python.
    Use [os.listdir], [os.stat], [pwd] and [grp]

    pip install prettytable
    Cell names: Mode, Owner, Group, Size, File name
    """

    def generate_table(self, table_instance: PrettyTable, data_list: list) -> PrettyTable:
        table_instance.field_names = ["Mode", "Owner", "Group", "Size", "File name"]
        table_instance.add_row(data_list)
        return table_instance


if __name__ == '__main__':
    instance: UnixLsLaOnPython = UnixLsLaOnPython()
    table: PrettyTable = PrettyTable()
    path: str = '.'
    for item in os.listdir(path):
        stat_info = os.stat(path)
        uid = stat_info.st_uid
        instance.generate_table(table, [stat_info.st_mode,
                                        pwd.getpwuid(uid).pw_name,
                                        pwd.getpwuid(uid).pw_gid,
                                        stat_info.st_size,
                                        item])
    print(table)
