import ast
from pathlib import Path
from unittest.mock import patch

import pytest

from tests.conftest import assert_question_prints, load_question_main


def _parse_main(relative_path: str) -> ast.FunctionDef:
    source_path = Path(f"F:/kkenj/workspace/python_100_knock/{relative_path}")
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    return next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")


def test_q041() -> None:
    assert_question_prints("questions/q041_q050/q041.py", "q041", [("guest",)])

    main_function = _parse_main("questions/q041_q050/q041.py")
    # 辞書リテラルへの代入が存在するか
    has_dict_assign = any(
        isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict)
        for node in ast.walk(main_function)
    )
    # キーアクセス (Subscript) または .get() が存在するか
    has_key_access = any(
        isinstance(node, ast.Subscript)
        or (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "get"
        )
        for node in ast.walk(main_function)
    )
    assert has_dict_assign, "辞書を変数に代入してください"
    assert has_key_access, "辞書からキーで値を取得してください"


def test_q042() -> None:
    assert_question_prints("questions/q041_q050/q042.py", "q042", [("id", "0001"), ("name", "guest")])

    main_function = _parse_main("questions/q041_q050/q042.py")
    # .items() メソッド呼び出しが存在するか
    has_items = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "items"
        for node in ast.walk(main_function)
    )
    # for ループが存在するか
    has_for = any(isinstance(node, ast.For) for node in ast.walk(main_function))
    assert has_items, ".items() を使ってキーと値を取得してください"
    assert has_for, "for 文を使って順に出力してください"


def test_q043() -> None:
    assert_question_prints("questions/q041_q050/q043.py", "q043", [([2, 4, 6, 8],)])

    main_function = _parse_main("questions/q041_q050/q043.py")
    # リスト内包表記が存在するか
    has_listcomp = any(isinstance(node, ast.ListComp) for node in ast.walk(main_function))
    assert has_listcomp, "リスト内包表記を使ってください"


def test_q044() -> None:
    assert_question_prints("questions/q041_q050/q044.py", "q044", [("1& 2& 3",)])

    main_function = _parse_main("questions/q041_q050/q044.py")
    # .replace() メソッド呼び出しが存在するか
    has_replace = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "replace"
        for node in ast.walk(main_function)
    )
    assert has_replace, ".replace() メソッドを使ってください"


def test_q045() -> None:
    assert_question_prints("questions/q041_q050/q045.py", "q045", [(["1", " 2", " 3"],), ("1& 2& 3",)])

    main_function = _parse_main("questions/q041_q050/q045.py")
    # .split() メソッド呼び出しが存在するか
    has_split = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "split"
        for node in ast.walk(main_function)
    )
    # .join() メソッド呼び出しが存在するか
    has_join = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "join"
        for node in ast.walk(main_function)
    )
    assert has_split, ".split() を使って文字列を分割してください"
    assert has_join, ".join() を使って文字列を結合してください"


def test_q046() -> None:
    assert_question_prints("questions/q041_q050/q046.py", "q046", [(30,), (10 / 3,), (10 // 3,), (10 % 3,)])

    main_function = _parse_main("questions/q041_q050/q046.py")
    ops_used: set[type] = set()
    for node in ast.walk(main_function):
        if isinstance(node, ast.BinOp):
            ops_used.add(type(node.op))
    required_ops = {ast.Mult, ast.Div, ast.FloorDiv, ast.Mod}
    missing = required_ops - ops_used
    assert not missing, f"演算子 {[op.__name__ for op in missing]} が使われていません"


def test_q047() -> None:
    assert_question_prints("questions/q041_q050/q047.py", "q047", [(3,)])

    main_function = _parse_main("questions/q041_q050/q047.py")
    # max() 呼び出しが存在するか
    has_max = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "max"
        for node in ast.walk(main_function)
    )
    assert has_max, "max() 関数を使ってください"


def test_q048() -> None:
    assert_question_prints("questions/q041_q050/q048.py", "q048", [("ゼロ除算エラーが発生しました",)])

    main_function = _parse_main("questions/q041_q050/q048.py")
    # try 文が存在するか
    has_try = any(isinstance(node, ast.Try) for node in ast.walk(main_function))
    # ZeroDivisionError を except しているか
    has_zero_div = any(
        isinstance(node, ast.ExceptHandler)
        and node.type is not None
        and isinstance(node.type, ast.Name)
        and node.type.id == "ZeroDivisionError"
        for node in ast.walk(main_function)
    )
    assert has_try, "try/except を使ってください"
    assert has_zero_div, "ZeroDivisionError を except してください"


def test_q049() -> None:
    _, main = load_question_main("questions/q041_q050/q049.py", "q049")

    with patch("builtins.print") as mock_print:
        main()

    actual_calls = [call.args for call in mock_print.call_args_list]
    assert len(actual_calls) == 1
    assert len(actual_calls[0]) == 1
    assert "NoneType" in str(actual_calls[0][0])

    main_function = _parse_main("questions/q041_q050/q049.py")
    # try 文が存在するか
    has_try = any(isinstance(node, ast.Try) for node in ast.walk(main_function))
    # TypeError を except しているか
    has_type_error = any(
        isinstance(node, ast.ExceptHandler)
        and node.type is not None
        and isinstance(node.type, ast.Name)
        and node.type.id == "TypeError"
        for node in ast.walk(main_function)
    )
    # None への代入が存在するか
    has_none_assign = any(
        isinstance(node, ast.Assign)
        and isinstance(node.value, ast.Constant)
        and node.value.value is None
        for node in ast.walk(main_function)
    )
    assert has_none_assign, "変数に None を代入してください"
    assert has_try, "try/except を使ってください"
    assert has_type_error, "TypeError を except してください"


def test_q050() -> None:
    _, main = load_question_main("questions/q041_q050/q050.py", "q050")

    with pytest.raises(ValueError, match="負の値が入力されました"):
        main()

    main_function = _parse_main("questions/q041_q050/q050.py")
    # raise ValueError が存在するか
    has_raise_value_error = any(
        isinstance(node, ast.Raise)
        and node.exc is not None
        and isinstance(node.exc, ast.Call)
        and isinstance(node.exc.func, ast.Name)
        and node.exc.func.id == "ValueError"
        for node in ast.walk(main_function)
    )
    # 負数判定の条件分岐が存在するか
    has_negative_check = any(
        isinstance(node, ast.Compare)
        and any(isinstance(op, ast.Lt) for op in node.ops)
        for node in ast.walk(main_function)
    )
    assert has_raise_value_error, "raise ValueError を使ってください"
    assert has_negative_check, "< 演算子で負の値を判定してください"