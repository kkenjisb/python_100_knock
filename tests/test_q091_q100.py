from __future__ import annotations

from pathlib import Path
from pprint import pformat
from unittest.mock import patch

import pytest

from tests.conftest import load_question_main, load_question_module


def test_q091(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q091_q100/q091.py", "q091")
    monkeypatch.chdir(tmp_path)

    main()

    expected_lines = [
        f"{left} × {right} = {left * right}"
        for left in range(1, 10)
        for right in range(1, 10)
        if "3" in str(left * right)
    ]
    assert (tmp_path / "output.txt").read_text(encoding="utf-8").splitlines() == expected_lines


def test_q092() -> None:
    module = load_question_module("questions/q091_q100/q092.py", "q092")
    assert module.find_numbers(1, 20) == {3, 13}


def test_q093() -> None:
    _, main = load_question_main("questions/q091_q100/q093.py", "q093")
    inputs = iter(["12", "3"])
    expected = []
    value = 1
    while len(expected) < 10:
        if "3" in str(value):
            expected.append((value,))
        value += 1

    with patch("builtins.input", side_effect=lambda _: next(inputs)), patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == expected


def test_q094() -> None:
    _, main = load_question_main("questions/q091_q100/q094.py", "q094")

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == [
        (("001", "004", {5}),),
        (("002", "002", {9}),),
        (("002", "004", {2}),),
    ]


def test_q095() -> None:
    _, main = load_question_main("questions/q091_q100/q095.py", "q095")

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == [
        ("is",),
        ("a",),
        ("that",),
        ("lets",),
        ("you",),
        ("work",),
        ("and",),
        ("more",),
    ]


def test_q096() -> None:
    module = load_question_module("questions/q091_q100/q096.py", "q096")
    assert module.reverse_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert module.reverse_dict({"a": 1, "b": 1}) is None


def test_q097(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q091_q100/q097.py", "q097")
    data_dir = tmp_path / "questions" / "data"
    data_dir.mkdir(parents=True)
    (data_dir / "q097_input.txt").write_text("banana\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == [
        ("b", 1),
        ("a", 3),
        ("n", 2),
        ("\n", 1),
    ]


def test_q098() -> None:
    module = load_question_module("questions/q091_q100/q098.py", "q098")
    instance = module.StringJoiner()
    instance.append(1)
    instance.append(None)
    instance.append(2)
    assert instance.join("&") == "1&2"

    with patch("builtins.print") as mock_print:
        module.main()

    mock_print.assert_called_once_with("1&2&3&5&7")


def test_q099() -> None:
    module, main = load_question_main("questions/q091_q100/q099.py", "q099")
    expected_audit = [
        {"index": 0, "from": 1, "to": 2},
        {"index": 2, "from": 3, "to": 6},
        {"index": 3, "from": None, "to": 0},
        {"index": 4, "from": 5, "to": 10},
        {"index": 5, "from": None, "to": 0},
        {"index": 6, "from": 7, "to": 14},
    ]

    with patch.object(module, "pprint") as mock_pprint:
        result = main()

    assert result == [2, 2, 6, 0, 10, 0, 14]
    mock_pprint.assert_called_once_with(expected_audit)


def test_q100(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q091_q100/q100.py", "q100")
    sample = (Path(__file__).resolve().parents[1] / "questions" / "data" / "q100_input.csv").read_text(encoding="utf-8")
    data_dir = tmp_path / "questions" / "data"
    data_dir.mkdir(parents=True)
    (data_dir / "q100_input.csv").write_text(sample, encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == [
        ("0003",),
        ("0004",),
        ("0005",),
        ("0005",),
    ]