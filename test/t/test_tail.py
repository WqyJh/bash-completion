import pytest


class TestTail:

    @pytest.mark.complete("tail --",
                          skipif="! tail --help &>/dev/null")
    def test_1(self, completion):
        assert completion
