from __future__ import annotations

import ast
from datetime import date, datetime
from pathlib import Path
from unittest.mock import patch

import pytest

from tests.conftest import WORKSPACE_ROOT, load_question_main


def test_q071() -> None:
    _, main = load_question_main("questions/q071_q080/q071.py", "q071")

    with patch("builtins.print") as mock_print:
        main()

    printed_value = mock_print.call_args.args[0]
    assert str(printed_value).endswith("q071.py")


def test_q072() -> None:
    # スクリプトとして直接実行した場合、__package__ は None になる
    module, main = load_question_main("questions/q071_q080/q072.py", "q072")
    module.__package__ = None

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with(None)


def test_q073() -> None:
    _, main = load_question_main("questions/q071_q080/q073.py", "q073")

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with("直接実行")


def test_q074() -> None:
    # import datetime して datetime.datetime.now() の結果を print する
    _, main = load_question_main("questions/q071_q080/q074.py", "q074")

    with patch("builtins.print") as mock_print:
        main()

    assert mock_print.call_count == 1
    assert isinstance(mock_print.call_args.args[0], datetime)


def test_q075() -> None:
    # from datetime import date して date.today() の結果を print する
    _, main = load_question_main("questions/q071_q080/q075.py", "q075")

    with patch("builtins.print") as mock_print:
        main()

    assert mock_print.call_count == 1
    assert isinstance(mock_print.call_args.args[0], date)


def test_q076() -> None:
    # import datetime as dt として dt.datetime.now() の結果を print する
    _, main = load_question_main("questions/q071_q080/q076.py", "q076")

    with patch("builtins.print") as mock_print:
        main()

    assert mock_print.call_count == 1
    assert isinstance(mock_print.call_args.args[0], datetime)


def test_q077(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q071_q080/q077.py", "q077")
    (tmp_path / "test.txt").write_text("hello", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with(True)

    source = (WORKSPACE_ROOT / "questions/q071_q080/q077.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    assert any(
        isinstance(node, ast.ImportFrom)
        and node.module == "pathlib"
        and any(alias.name == "Path" for alias in node.names)
        for node in ast.walk(tree)
    ), "pathlib モジュールから Path クラスをインポートしてください"


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