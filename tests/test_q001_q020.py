from unittest.mock import patch

import pytest

from tests.conftest import load_question_main


@pytest.mark.parametrize(
    ("relative_path", "module_name", "expected_calls"),
    [
        pytest.param("questions/q001_q010/q001.py", "q001", [("Hello, World!",)], id="q001"),
        pytest.param("questions/q001_q010/q002.py", "q002", [(1,), (2,), (3,)], id="q002"),
        pytest.param("questions/q001_q010/q003.py", "q003", [(123, "Hello")], id="q003"),
        pytest.param("questions/q001_q010/q004.py", "q004", [(1,), (3,)], id="q004"),
        pytest.param("questions/q001_q010/q005.py", "q005", [], id="q005"),
        pytest.param("questions/q001_q010/q006.py", "q006", [(10,)], id="q006"),
        pytest.param("questions/q001_q010/q007.py", "q007", [(3,)], id="q007"),
        pytest.param("questions/q001_q010/q008.py", "q008", [("12",)], id="q008"),
        pytest.param("questions/q001_q010/q009.py", "q009", [("10",), (10,)], id="q009"),
        pytest.param("questions/q001_q010/q010.py", "q010", [("1\n2\n3",)], id="q010"),
        pytest.param("questions/q011_q020/q011.py", "q011", [(r"C:\test",)], id="q011"),
        pytest.param("questions/q011_q020/q012.py", "q012", [(r"C:\test",)], id="q012"),
        pytest.param("questions/q011_q020/q013.py", "q013", [("Hello, Python!",)], id="q013"),
        pytest.param("questions/q011_q020/q014.py", "q014", [(6,)], id="q014"),
        pytest.param("questions/q011_q020/q015.py", "q015", [("Py",)], id="q015"),
        pytest.param("questions/q011_q020/q016.py", "q016", [(None,)], id="q016"),
        pytest.param("questions/q011_q020/q017.py", "q017", [(int,), (float,), (str,), (bool,)], id="q017"),
        pytest.param("questions/q011_q020/q018.py", "q018", [([1, 2, 3],), (1,)], id="q018"),
        pytest.param("questions/q011_q020/q019.py", "q019", [([1, 2],)], id="q019"),
        pytest.param("questions/q011_q020/q020.py", "q020", [([1, 2, 3, 4],)], id="q020"),
    ],
)
def test_q001_q020_print_outputs(relative_path: str, module_name: str, expected_calls: list[tuple]) -> None:
    _, main = load_question_main(relative_path, module_name)

    with patch("builtins.print") as mock_print:
        main()

    actual_calls = [call.args for call in mock_print.call_args_list]
    assert actual_calls == expected_calls