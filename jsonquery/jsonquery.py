import argparse
import json
import sys

STATUS_OK  = 0
STATUS_ERR = 1

class JSONQuery(object):

    def __init__(self):
        self.args = self._parse_arguments()
        self.status = STATUS_OK

    def main(self):
        res = self._query()
        self._print(res)
        sys.exit(self.status)

    def _parse_arguments(self):
        parser = argparse.ArgumentParser(description='Query key from json')
        parser.add_argument('key', nargs='*', default='')
        parser.add_argument('-d', '--delimiter', default='.')
        args = parser.parse_args()
        return vars(args)

    def _query(self):
        data = json.loads(sys.stdin.read())
        keys = self.args['key']
        values = []

        for key in keys:
            value = self._get(data, key)
            values.append(value)

        if not keys:
            values = [self._get(data, '.')]

        return values

    def _get(self, data, key):
        delimiter = self.args['delimiter']
        parts = key.split(delimiter)
        parts = filter(lambda x: x != '', parts)
        res = data

        for level, part in enumerate(parts):
            if level != 0 and isinstance(res, dict) and part == '':
                res = res.keys()
                break

            if isinstance(res, (list, tuple)):
                try:
                    part = int(part)
                except ValueError:
                    print("Invalid key value. List index must be an integer: " + delimiter.join(parts[:level]) + '.N')
                    sys.exit(STATUS_ERR)

            try:
                res = res[part]
            except KeyError:
                self.status = STATUS_ERR
                res = filter(lambda x: x.startswith(part), res.keys())
                if not res:
                    sys.exit(self.status)
            except TypeError:
                sys.exit(STATUS_ERR)

        if isinstance(res, dict) and len(self.args['key']) and key[-1] == '.':
            res = res.keys()

        return res

    def _print(self, values):
        for v in values:
            if isinstance(v, (list)):
                self._print(v)
            else:
                if isinstance(v, dict):
                    v = json.dumps(v, sort_keys=True, indent=4, separators=(',', ':'))
                print(v)

def main():
    json_query = JSONQuery()
    json_query.main()
