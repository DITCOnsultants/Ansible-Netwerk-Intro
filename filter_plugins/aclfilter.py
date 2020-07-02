#!/usr/bin/python
import re

class FilterModule(object):
    def filters(self):
        return {
            'parse_acl': self.parse_acl,
            'get_delete': self.get_delete,
            'get_append': self.get_append,
        }

    def parse_acl(self, a_variable):
        test = []
        regex_acl = re.compile("^\s+(\d+)\s+(permit|deny|remark)\s+(.*)")
        for item in a_variable.split('\n'):
            try:
                ace = regex_acl.search(item).groups()
                test.append(ace)
            except:
                pass

        return test
    
    def get_delete(self,_from,_to):
        to_delete = []
        for item in _from:
            if not item in _to:
                to_delete.append(item)
        return to_delete

    def get_append(self,_from,_to):
        to_append = []
        for item in _to:
            if not item in _from:
                to_append.append(item)
        return to_append