import argparse
import re
import subprocess
import json
import urllib.request

margins = [5, 20, 10, 10]


def define_autonomous_system(ip: str):
    response = urllib.request.urlopen(f'https://ipinfo.io/{ip}/json')
    data = json.loads(response.read())

    if 'bogon' in data and data['bogon']:
        return 'bogon', '-', '-'

    autonomous_system = ''
    country = ''
    provider = ''
    if 'country' in data:
        country = data['country']
    if 'org' in data:
        match_as = re.search(re.compile(r'\bAS\d+'), data['org'])
        autonomous_system = match_as.group(0)[2:] if match_as is not None else ''
        provider = data['org'].replace(autonomous_system, '') if match_as is not None else data['org']
    return autonomous_system, country, provider


def trace_system(ip, max_hops):
    try:
        nodes = perform_a_trace(ip, max_hops)
        if len(nodes) == 0:
            raise Exception('Произошла непредвиденная ошибка, '
                            'проверьте введённый вами ip на корректность, '
                            'а подключение к интернету на наличие')
        print_start_line()
        for number, node in enumerate(nodes):
            result = define_autonomous_system(node)
            print_result_line(number, node, result)
    except Exception as e:
        print(str(e))


def print_result_line(number: int, ip: str, result):
    print(f'{number:<{margins[0]}}'
          f'{ip:<{margins[1]}}'
          f'{result[0]:<{margins[2]}}'
          f'{result[1]:<{margins[3]}}'
          f'{result[2]}')


def print_start_line() -> None:
    print('№' + ' ' * (margins[0] - 1) +
          'IP' + ' ' * (margins[1] - 2) +
          'AS' + ' ' * (margins[2] - 2) +
          'Country' + ' ' * (margins[3] - 7) +
          'Provider')


def perform_a_trace(ip: str, max_hops: int):
    traceroute = get_traceroute(ip, max_hops)
    ips = parse_traceroute(traceroute)
    return ips


def parse_traceroute(traceroute: str):
    lines = traceroute.split('\n')
    result = []
    for line in lines[2:]:
        ip = re.search(re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'), line)
        if ip is not None:
            result.append(ip.group(0))
    return result


def get_traceroute(ip: str, max_hops: int):
    traceroute = subprocess.Popen(['tracert', '-d', '-h', str(max_hops), ip], stdout=subprocess.PIPE)
    return traceroute.communicate()[0].decode('866')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="Ip for tracert")
    parser.add_argument("--max_hops", help="Max hops for tracert", type=int, default=30)
    args = parser.parse_args()

    trace_system(args.ip, args.max_hops)
