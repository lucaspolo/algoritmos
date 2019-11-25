from collections import OrderedDict

from pytest import fixture

from graphs import calculate_degrees, topological_sorter


@fixture
def g():
    d = OrderedDict()
    d[1] = [2]
    d[2] = [4]
    d[3] = [2]
    d[4] = []

    return d


class TestCalculateDegree:

    def test_should_calculate_degree(
        self,
        g
    ):
        in_degree = calculate_degrees(g)

        assert in_degree[1] == 0
        assert in_degree[2] == 2
        assert in_degree[3] == 0
        assert in_degree[4] == 1


class TestTopologicalSorter:

    def test_should_return_in_topological_sort(
        self,
        g
    ):
        ordered = topological_sorter(g)

        assert ordered == [3, 2, 1, 4]
