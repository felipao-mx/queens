from utilities.columnutilities import numToString
# import pytest

# # @pytest.mark.parametrize("testVal,expected",
# #                          [
# #                              (1, "A"),
# #                              (2, "B"),
# #                              (3, "C")
# #                          ])

def test_numToColumn():
    testVal = 2
    expected = "B"
    assert numToString(testVal) == expected
