from os import path

import pytest

from day1 import read_data, count_increases, count_sliding_window

@pytest.fixture
def dummy_file():
    script_dir = path.dirname(path.realpath(__file__))
    file = open(path.join(script_dir, "test.txt"), "r").read().splitlines()
    return file

def test_part_1_count_increases_small():
    file = """199
    200
    208
    210
    200
    207
    240
    269
    260
    263""".splitlines()
    data = read_data(file)
    assert count_increases(data) == 7
    assert count_increases(count_sliding_window(data)) == 5

def test_part2_count_sliding_window(dummy_file: list[str]):
    assert count_sliding_window(dummy_file) == [607, 618, 618, 617,
                                            647, 716, 769, 792]
