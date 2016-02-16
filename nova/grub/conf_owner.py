# -*- encoding: utf-8 -*-
'''
Setting the owner and group to root prevents non-root users from changing the
file.

:maintainer: HubbleStack
:maturity: 20160212
:depends: SaltStack
:platform: Linux
:compatibility: RedHat

'''
from __future__ import absolute_import
from audit import *
import logging


def __virtual__():
    if 'RedHat' in __salt__['grains.get']('os_family'):
        return True
    return False


def audit():
    if 'systemctl' in CHKCONFIG:
        ret = _stat('/boot/grub2/grub.cfg')
    elif 'chkconfig' in CHKCONFIG:
        ret = _stat('/etc/grub.conf')

    if '0 0' in ret:
        return True
    return False