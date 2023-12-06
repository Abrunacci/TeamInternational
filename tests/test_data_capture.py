from data_capture import DataCapture


def test_data_capture_with_example():
    capture = DataCapture()
    for number in [3, 9, 3, 4, 6]:
        capture.add(number)
    stats = capture.build_stats()
    assert stats.less(4) == 2
    assert stats.between(3, 6) == 4
    assert stats.greater(4) == 2


def test_data_capture_with_errors():
    capture = DataCapture()
    for number in ["a", 1254, -3, 4, 6]:
        capture.add(number)
    assert capture.data == [4, 6]


def test_stats_less_with_wrong_inputs():
    capture = DataCapture()
    for number in [3, 9, 3, 4, 6]:
        capture.add(number)
    stats = capture.build_stats()
    for _input in ["a", 1254, -3]:
        assert stats.less(_input) is None


def test_stats_greater_with_wrong_inputs():
    capture = DataCapture()
    for number in [3, 9, 3, 4, 6]:
        capture.add(number)
    stats = capture.build_stats()
    for _input in ["a", 1254, -3]:
        assert stats.greater(_input) is None


def test_stats_between_with_wrong_inputs():
    capture = DataCapture()
    for number in [3, 9, 3, 4, 6]:
        capture.add(number)
    stats = capture.build_stats()
    for _input in [("a", 23), (1253, 4), (-3, 10), (10, 2)]:
        assert stats.between(_input[0], _input[1]) is None
