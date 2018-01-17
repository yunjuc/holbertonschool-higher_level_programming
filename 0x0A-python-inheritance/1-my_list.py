#!/usr/bin/python3


class MyList(list):
    '''define MyList class based on list'''

    def print_sorted(self):
        '''print sorted list'''
        print(sorted(self))
