from . import nanomsg, unittest, SOCKET_ADDRESS


class TestPubSubSockets(unittest.TestCase):
    def test_subscribe_works(self):
        with nanomsg.Socket(nanomsg.PUB) as s1:
            with nanomsg.Socket(nanomsg.SUB) as s2:
                s1.bind(SOCKET_ADDRESS)
                s2.connect(SOCKET_ADDRESS)
                s2.set_string_option(
                    nanomsg.SUB, nanomsg.SUB_SUBSCRIBE, 'test')
                s1.send('test')
                s2.recv()
                s1.send('a') # should not get received
                expected = b'test121212'
                s1.send(expected)

                actual = s2.recv()

                self.assertEquals(expected, actual)
