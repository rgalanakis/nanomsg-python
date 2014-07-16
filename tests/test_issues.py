from . import nanomsg, unittest

class Issue22Test(unittest.TestCase):
    def test_issue22(self):
        s1 = nanomsg.Socket(nanomsg.REQ)
        s2 = nanomsg.Socket(nanomsg.REP)

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
