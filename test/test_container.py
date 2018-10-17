from phoopy.kernel import Container


class TestContainer(object):
    def test_init(self):
        assert Container() is not None
