#!/usr/bin/python2 -O

import qubes.vm.netvm

class AdminVM(qubes.vm.netvm.NetVM):
    def __init__(self, D):
        super(AdminVM, self).__init__(D)