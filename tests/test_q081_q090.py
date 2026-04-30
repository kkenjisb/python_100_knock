from __future__ import annotations

import csv
from pathlib import Path
from unittest.mock import patch

import pytest

from tests.conftest import load_question_main, load_question_module


def test_q081(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q081_q090/q081.py", "q081")
    target = tmp_path / "test.txt"
    target.write_text("Hello", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    main()

    assert not target.exists()


def test_q082(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q081_q090/q082.py", "q082")
    monkeypatch.chdir(tmp_path)

    main()

    assert (tmp_path / "test.csv").read_text(encoding="utf-8").splitlines() == [
        "1,2,3",
        "4,5,6",
        "7,8,9",
    ]


def test_q083(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q081_q090/q083.py", "q083")
    (tmp_path / "test.csv").write_text("1,2,3\n4,5,6\n7,8,9\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == [
        (["1", "2", "3"],),
        (["4", "5", "6"],),
        (["7", "8", "9"],),
    ]


def test_q084(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q081_q090/q084.py", "q084")
    monkeypatch.chdir(tmp_path)

    main()

    assert (tmp_path / "test.csv").read_text(encoding="utf-8").splitlines() == [
        "id,name",
        "0001,admin",
        "0002,guest",
        "0003,test",
    ]


def test_q085(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _, main = load_question_main("questions/q081_q090/q085.py", "q085")
    (tmp_path / "test.csv").write_text("id,name\n0001,admin\n0002,guest\n0003,test\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == [
        ({"id": "0001", "name": "admin"},),
        ({"id": "0002", "name": "guest"},),
        ({"id": "0003", "name": "test"},),
    ]


def test_q086(monkeypatch: pytest.MonkeyPatch) -> None:
    module, main = load_question_main("questions/q081_q090/q086.py", "q086")
    monkeypatch.setattr(module.sys, "argv", ["q086.py", "sample"])

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with("sample")


def test_q087() -> None:
    _, main = load_question_main("questions/q081_q090/q087.py", "q087")

    with patch("builtins.input", return_value="abc") as mock_input, patch("builtins.print") as mock_print:
        main()

    mock_input.assert_called_once_with("文字を入力してください")
    mock_print.assert_called_once_with("abc")


def test_q088() -> None:
    module = load_question_module("questions/q081_q090/q088.py", "q088")

    with patch("builtins.print") as mock_print, patch.object(module, "pprint") as mock_pprint:
        module.main()

    assert mock_print.call_count == 1
    assert mock_pprint.call_count == 1


def test_q089() -> None:
    module = load_question_module("questions/q081_q090/q089.py", "q089")

    with patch.object(module, "showinfo") as mock_showinfo, patch.object(module, "askyesno") as mock_askyesno:
        module.main()

    mock_showinfo.assert_called_once_with("タイトル", "メッセージ")
    mock_askyesno.assert_called_once_with("タイトル", "メッセージ")


def test_q090(caplog: pytest.LogCaptureFixture) -> None:
    _, main = load_question_main("questions/q081_q090/q090.py", "q090")

    with caplog.at_level("INFO"):
        main()

    messages = [record.getMessage() for record in caplog.records]
    assert "正常終了しました" in messages
    assert "予期せぬエラーが発生しました" in messages