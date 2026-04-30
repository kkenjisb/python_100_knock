from unittest.mock import patch

import pytest

from tests.conftest import load_question_main


def _numbers_with_three(limit: int) -> list[tuple[int]]:
    return [(number,) for number in range(1, limit) if "3" in str(number)]


@pytest.mark.parametrize(
    ("relative_path", "module_name", "expected_calls"),
    [
        pytest.param("questions/q021_q030/q021.py", "q021", [(3,)], id="q021"),
        pytest.param("questions/q021_q030/q022.py", "q022", [([1, 3],)], id="q022"),
        pytest.param("questions/q021_q030/q023.py", "q023", [([1, 2, 3, 4],)], id="q023"),
        pytest.param("questions/q021_q030/q024.py", "q024", [("xは10より大きい",)], id="q024"),
        pytest.param("questions/q021_q030/q025.py", "q025", [("xは5より大きいが、10以下",)], id="q025"),
        pytest.param("questions/q021_q030/q026.py", "q026", [(False,), (False,), (False,), (True,), (True,)], id="q026"),
        pytest.param("questions/q021_q030/q027.py", "q027", [(True,)], id="q027"),
        pytest.param("questions/q021_q030/q028.py", "q028", [(True,)], id="q028"),
        pytest.param("questions/q021_q030/q029.py", "q029", [(False,), (True,)], id="q029"),
        pytest.param("questions/q021_q030/q030.py", "q030", [], id="q030"),
        pytest.param("questions/q031_q040/q031.py", "q031", [(1,), (2,), (3,)], id="q031"),
        pytest.param("questions/q031_q040/q032.py", "q032", [(number,) for number in range(10)], id="q032"),
        pytest.param("questions/q031_q040/q033.py", "q033", [(number,) for number in range(6)], id="q033"),
        pytest.param("questions/q031_q040/q034.py", "q034", [(number,) for number in range(10) if number != 5], id="q034"),
        pytest.param("questions/q031_q040/q035.py", "q035", [(number,) for number in range(10, 0, -1)], id="q035"),
        pytest.param("questions/q031_q040/q036.py", "q036", [((1, 2, 3),), (1,)], id="q036"),
        pytest.param("questions/q031_q040/q037.py", "q037", [((1, 2, 3, 4),), (4,)], id="q037"),
        pytest.param("questions/q031_q040/q038.py", "q038", [([1, 2, 3],), ([2, 3],)], id="q038"),
        pytest.param("questions/q031_q040/q039.py", "q039", [([1, 2, 3, 4, 5],), ([3],)], id="q039"),
        pytest.param("questions/q031_q040/q040.py", "q040", [(1,), (2,), (3,)], id="q040"),
        pytest.param("questions/q041_q050/q041.py", "q041", [("guest",)], id="q041"),
        pytest.param("questions/q041_q050/q042.py", "q042", [("id", "0001"), ("name", "guest")], id="q042"),
        pytest.param("questions/q041_q050/q043.py", "q043", [([2, 4, 6, 8],)], id="q043"),
        pytest.param("questions/q041_q050/q044.py", "q044", [("1& 2& 3",)], id="q044"),
        pytest.param("questions/q041_q050/q045.py", "q045", [(["1", " 2", " 3"],), ("1& 2& 3",)], id="q045"),
        pytest.param("questions/q041_q050/q046.py", "q046", [(30,), (10 / 3,), (10 // 3,), (10 % 3,)], id="q046"),
        pytest.param("questions/q041_q050/q047.py", "q047", [(3,)], id="q047"),
        pytest.param("questions/q041_q050/q048.py", "q048", [("ゼロ除算エラーが発生しました",)], id="q048"),
    ],
)
def test_q021_q048_outputs(relative_path: str, module_name: str, expected_calls: list[tuple]) -> None:
    _, main = load_question_main(relative_path, module_name)

    with patch("builtins.print") as mock_print:
        main()

    actual_calls = [call.args for call in mock_print.call_args_list]
    assert actual_calls == expected_calls


def test_q049() -> None:
    _, main = load_question_main("questions/q041_q050/q049.py", "q049")

    with patch("builtins.print") as mock_print:
        main()

    actual_calls = [call.args for call in mock_print.call_args_list]
    assert len(actual_calls) == 1
    assert len(actual_calls[0]) == 1
    assert "NoneType" in str(actual_calls[0][0])


def test_q050() -> None:
    _, main = load_question_main("questions/q041_q050/q050.py", "q050")

    with pytest.raises(ValueError, match="負の値が入力されました"):
        main()