import os
import unittest

from nanomsg_wrappers import set_wrapper_choice, get_default_for_platform
set_wrapper_choice(os.environ.get('NANOMSG_PY_TEST_WRAPPER',
                                  get_default_for_platform()))
import nanomsg
from nanomsg import (
    PAIR,
    Socket,
    LINGER,
    SOL_SOCKET,
REQ,
REP
)

class Issue22Test(unittest.TestCase):
    def test_issue22(self):
        s1 = Socket(REQ)
        s2 = Socket(REP)

        s1.bind('inproc://hello')
        s2.bind('inproc://hi')
        s1.close()

        def assertRaises(func, *args):
            with self.assertRaises(nanomsg.NanoMsgSocketClosedError):
                func(*args)

        assertRaises(s1.connect, 'inproc://hi')
        assertRaises(s1.bind, 'inproc://hello')
        assertRaises(s1.send, 'hi')
        assertRaises(s1.recv)
