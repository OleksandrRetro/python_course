import re
import socket


class IPValidation(object):
    """
    Create function for IP validation using [re] and [socket.inet_aton]
    """

    @staticmethod
    def check_ip_using_re(ip_address: str) -> bool:
        valid_ip_regex: str = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        if re.search(valid_ip_regex, ip_address):
            return True
        else:
            return False

    @staticmethod
    def check_ip_using_inet_aton(ip_address: str) -> bool:
        try:
            socket.inet_aton(ip_address)
            return True
        except socket.error:
            return False


if __name__ == '__main__':
    assert IPValidation.check_ip_using_inet_aton('') is False
    assert IPValidation.check_ip_using_inet_aton('192.168.0.1') is True
    assert IPValidation.check_ip_using_inet_aton('0.0.0.1') is True
    assert IPValidation.check_ip_using_re('10.100.500.32') is False
    assert IPValidation.check_ip_using_re(str(700)) is False
    assert IPValidation.check_ip_using_re('127.0.1') is False
