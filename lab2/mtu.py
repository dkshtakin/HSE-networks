import subprocess
import platform
from bisect import bisect_right
import argparse

class KeyWrap:
    def __init__(self, it, key):
        self.it = it
        self.key = key

    def __getitem__(self, i):
        return self.key(self.it[i])

    def __len__(self):
        return len(self.it)

def is_mtu_ok(host: str, mtu: int, c: int) -> bool:
    if platform.system() == "Windows":
        cmd = f'ping -l {mtu} -f {host} -n {1 if c is None else c}'
    else: # Linux
        cmd = f'ping -s {mtu} -M do {host} -c {1 if c is None else c}'
    cmd_result = subprocess.run(cmd, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
    if cmd_result.returncode == 2:
        print(cmd_result.stderr)
        exit(1)
    return not bool(cmd_result.returncode)

def find_mtu(host: str, c: int) -> int:
    mtus = [*range(0, 1473)]
    index = bisect_right(KeyWrap(mtus, key=lambda x: not is_mtu_ok(host, x, c)), 0)
    return mtus[index - 1]

def is_available(host: str) -> bool:
    return is_mtu_ok(host, 0, 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = 'python3 mtu.py')
    parser.add_argument('host', help='host address')
    parser.add_argument('-c', '--count', help='option of ping command: \
                        stop after sending count ECHO_REQUEST packets')
    args = parser.parse_args()
    if args.count is not None:
        if not args.count.isdigit():
            print(f'count \'{args.count}\': should be a positive integer number')
            exit(1)
        if not (1 < int(args.count) < 9223372036854775807):
            print(f'count \'{args.count}\': out of range: 1 <= value <= 9223372036854775807')
            exit(1)
    if not is_available(args.host):
        print(f'{args.host} unreachable')
        exit(1)
    mtu = find_mtu(args.host, args.count) + 28
    print(f'MTU {mtu}')