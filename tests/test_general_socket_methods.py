from . import nanomsg, unittest, SOCKET_ADDRESS, LINGER_DEFAULT_VALUE


class TestGeneralSocketMethods(unittest.TestCase):
    def setUp(self):
        self.socket = nanomsg.Socket(nanomsg.PAIR)

    def tearDown(self):
        self.socket.close()

    def test_bind(self):
        endpoint = self.socket.bind(SOCKET_ADDRESS)

        self.assertIsNotNone(endpoint)

    def test_connect(self):
        endpoint = self.socket.connect(SOCKET_ADDRESS)

        self.assertIsNotNone(endpoint)

    def test_is_open_is_true_when_open(self):
        self.assertTrue(self.socket.is_open())

    def test_is_open_is_false_when_closed(self):
        self.socket.close()

        self.assertFalse(self.socket.is_open())

    def test_set_int_option(self):
        expected = 500

        self.socket.set_int_option(
            nanomsg.SOL_SOCKET, nanomsg.LINGER, expected)

        actual = self.socket.get_int_option(nanomsg.SOL_SOCKET, nanomsg.LINGER)
        self.assertEqual(expected, actual)

    def test_get_int_option(self):
        actual = self.socket.get_int_option(nanomsg.SOL_SOCKET, nanomsg.LINGER)

        self.assertEqual(LINGER_DEFAULT_VALUE, actual)
