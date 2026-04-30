from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from unittest.mock import patch

import pytest

from tests.conftest import load_question_main, load_question_module


def test_q071() -> None:
    _, main = load_question_main("questions/q071_q080/q071.py", "q071")

    with patch("builtins.print") as mock_print:
        main()

    printed_value = mock_print.call_args.args[0]
    assert str(printed_value).endswith("q071.py")


def test_q072() -> None:
    _, main = load_question_main("questions/q071_q080/q072.py", "q072")

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with(None)


def test_q073() -> None:
    _, main = load_question_main("questions/q071_q080/q073.py", "q073")

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with("直接実行")


def test_q074(monkeypatch: pytest.MonkeyPatch) -> None:
    module, main = load_question_main("questions/q071_q080/q074.py", "q074")

    class FixedDatetime(datetime):
        @classmethod
        def now(cls):
            return cls(2025, 4, 30, 12, 34, 56)

    monkeypatch.setattr(module, "datetime", module.datetime)
    monkeypatch.setattr(module.datetime, "datetime", FixedDatetime)
    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with(FixedDatetime(2025, 4, 30, 12, 34, 56))


def test_q075(monkeypatch: pytest.MonkeyPatch) -> None:
    module, main = load_question_main("questions/q071_q080/q075.py", "q075")

    class FixedDate(date):
        @classmethod
        def today(cls):
            return cls(2025, 4, 30)

    monkeypatch.setattr(module, "date", FixedDate)
    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with(FixedDate(2025, 4, 30))


def test_q076(monkeypatch: pytest.MonkeyPatch) -> None:
    module, main = load_question_main("questions/q071_q080/q076.py", "q076")

    class FixedDatetime(datetime):
        @classmethod
        def now(cls):
            return cls(2025, 4, 30, 12, 34, 56)

    monkeypatch.setattr(module.dt, "datetime", FixedDatetime)
    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with(FixedDatetime(2025, 4, 30, 12, 34, 56))


def test_q077(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q071_q080/q077.py", "q077")
    (tmp_path / "test.txt").write_text("hello", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with(True)


def test_q078(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q071_q080/q078.py", "q078")
    target = tmp_path / "test.txt"
    target.write_text("old", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    main()

    assert target.read_text(encoding="utf-8") == "Hello, World!"


def test_q079(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q071_q080/q079.py", "q079")
    target = tmp_path / "test.txt"
    target.write_text("old", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    main()

    assert target.read_text(encoding="utf-8") == "oldHello, World!"


def test_q080(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q071_q080/q080.py", "q080")
    target = tmp_path / "test.txt"
    target.write_text("Hello!", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with("Hello!")