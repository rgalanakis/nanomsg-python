from . import nanomsg, unittest, SOCKET_ADDRESS


class TestPairSockets(unittest.TestCase):
    def test_send_recv(self):
        with nanomsg.Socket(nanomsg.PAIR) as s1:
            with nanomsg.Socket(nanomsg.PAIR) as s2:
                s1.bind(SOCKET_ADDRESS)
                s2.connect(SOCKET_ADDRESS)

                sent = b'ABC'
                s2.send(sent)
                recieved = s1.recv()
        self.assertEqual(sent, recieved)

    def test_send_recv_with_embeded_nulls(self):
        with nanomsg.Socket(nanomsg.PAIR) as s1:
            with nanomsg.Socket(nanomsg.PAIR) as s2:
                s1.bind(SOCKET_ADDRESS)
                s2.connect(SOCKET_ADDRESS)

                sent = b'ABC\x00DEFEDDSS'
                s2.send(sent)
                recieved = s1.recv()
        self.assertEqual(sent, recieved)

    def test_send_recv_large_message(self):
        with nanomsg.Socket(nanomsg.PAIR) as s1:
            with nanomsg.Socket(nanomsg.PAIR) as s2:
                s1.bind(SOCKET_ADDRESS)
                s2.connect(SOCKET_ADDRESS)

                sent = b'B' * (1024 * 1024)
                s2.send(sent)
                recieved = s1.recv()
        self.assertEqual(sent, recieved)
