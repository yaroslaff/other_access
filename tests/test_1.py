import os
from other_access import oaccess


def test_user():
    assert oaccess('/etc/shadow', os.R_OK | os.W_OK, 'root') == True

def test_group():
    assert oaccess('/etc/shadow', os.R_OK, 'nobody', ['shadow']) == True

def test_other():
    assert oaccess('/etc/shadow', os.R_OK, 'nobody') == False
    assert oaccess('/etc/shadow', os.F_OK, 'nobody') == True
