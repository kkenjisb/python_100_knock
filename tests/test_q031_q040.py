import ast
from pathlib import Path

from tests.conftest import assert_question_prints


def _parse_main(relative_path: str) -> ast.FunctionDef:
    source_path = Path(f"F:/kkenj/workspace/python_100_knock/{relative_path}")
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    return next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")


def test_q031() -> None:
    assert_question_prints("questions/q031_q040/q031.py", "q031", [(1,), (2,), (3,)])

    main_function = _parse_main("questions/q031_q040/q031.py")
    # for ループが存在するか
    has_for = any(isinstance(node, ast.For) for node in ast.walk(main_function))
    # リスト変数への代入が存在するか
    has_list_assign = any(
        isinstance(node, ast.Assign) and isinstance(node.value, ast.List)
        for node in ast.walk(main_function)
    )
    assert has_list_assign, "リストを変数に代入してください"
    assert has_for, "for ループを使ってください"


def test_q032() -> None:
    assert_question_prints("questions/q031_q040/q032.py", "q032", [(number,) for number in range(10)])

    main_function = _parse_main("questions/q031_q040/q032.py")
    # for ループが存在するか
    has_for = any(isinstance(node, ast.For) for node in ast.walk(main_function))
    # range() 呼び出しが存在するか
    has_range = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "range"
        for node in ast.walk(main_function)
    )
    assert has_for, "for ループを使ってください"
    assert has_range, "range() 関数を使ってください"


def test_q033() -> None:
    assert_question_prints("questions/q031_q040/q033.py", "q033", [(number,) for number in range(6)])

    main_function = _parse_main("questions/q031_q040/q033.py")
    # for ループが存在するか
    has_for = any(isinstance(node, ast.For) for node in ast.walk(main_function))
    # break 文が存在するか
    has_break = any(isinstance(node, ast.Break) for node in ast.walk(main_function))
    assert has_for, "for ループを使ってください"
    assert has_break, "break を使ってください"


def test_q034() -> None:
    assert_question_prints(
        "questions/q031_q040/q034.py", "q034", [(number,) for number in range(10) if number != 5]
    )

    main_function = _parse_main("questions/q031_q040/q034.py")
    # for ループが存在するか
    has_for = any(isinstance(node, ast.For) for node in ast.walk(main_function))
    # continue 文が存在するか
    has_continue = any(isinstance(node, ast.Continue) for node in ast.walk(main_function))
    assert has_for, "for ループを使ってください"
    assert has_continue, "continue を使ってください"


def test_q035() -> None:
    assert_question_prints("questions/q031_q040/q035.py", "q035", [(number,) for number in range(10, 0, -1)])

    main_function = _parse_main("questions/q031_q040/q035.py")
    # while ループが存在するか
    has_while = any(isinstance(node, ast.While) for node in ast.walk(main_function))
    assert has_while, "while ループを使ってください"


def test_q036() -> None:
    assert_question_prints("questions/q031_q040/q036.py", "q036", [((1, 2, 3),), (1,)])

    main_function = _parse_main("questions/q031_q040/q036.py")
    # タプルリテラルへの代入が存在するか
    has_tuple_assign = any(
        isinstance(node, ast.Assign) and isinstance(node.value, ast.Tuple)
        for node in ast.walk(main_function)
    )
    # 変数 tpl への代入が存在するか
    has_tpl_assign = any(
        isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "tpl" for t in node.targets)
        for node in ast.walk(main_function)
    )
    assert has_tpl_assign, "変数 tpl にタプルを代入してください"
    assert has_tuple_assign, "タプルを使ってください"


def test_q037() -> None:
    assert_question_prints("questions/q031_q040/q037.py", "q037", [((1, 2, 3, 4),), (4,)])

    main_function = _parse_main("questions/q031_q040/q037.py")
    # + 演算子でタプルを結合しているか
    has_tuple_concat = any(
        isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add)
        for node in ast.walk(main_function)
    )
    # len() 呼び出しが存在するか
    has_len = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "len"
        for node in ast.walk(main_function)
    )
    assert has_tuple_concat, "+ 演算子でタプルを結合してください"
    assert has_len, "len() 関数を使ってください"


def test_q038() -> None:
    assert_question_prints("questions/q031_q040/q038.py", "q038", [([1, 2, 3],), ([2, 3],)])

    main_function = _parse_main("questions/q031_q040/q038.py")
    # .add() 呼び出しが存在するか
    has_add = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "add"
        for node in ast.walk(main_function)
    )
    # .remove() または .discard() 呼び出しが存在するか
    has_remove = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in ("remove", "discard")
        for node in ast.walk(main_function)
    )
    # sorted() 呼び出しが存在するか
    has_sorted = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "sorted"
        for node in ast.walk(main_function)
    )
    assert has_add, ".add() メソッドを使って要素を追加してください"
    assert has_remove, ".remove() か .discard() メソッドを使って要素を削除してください"
    assert has_sorted, "sorted() を使って出力してください"


def test_q039() -> None:
    assert_question_prints("questions/q031_q040/q039.py", "q039", [([1, 2, 3, 4, 5],), ([3],)])

    main_function = _parse_main("questions/q031_q040/q039.py")
    # 和集合: | 演算子 または .union()
    has_union = any(
        (isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr))
        or (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "union"
        )
        for node in ast.walk(main_function)
    )
    # 共通部分: & 演算子 または .intersection()
    has_intersection = any(
        (isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitAnd))
        or (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "intersection"
        )
        for node in ast.walk(main_function)
    )
    # sorted() 呼び出しが存在するか
    has_sorted = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "sorted"
        for node in ast.walk(main_function)
    )
    assert has_union, "| 演算子か .union() を使って和集合を求めてください"
    assert has_intersection, "& 演算子か .intersection() を使って共通部分を求めてください"
    assert has_sorted, "sorted() を使って出力してください"


def test_q040() -> None:
    assert_question_prints("questions/q031_q040/q040.py", "q040", [(1,), (2,), (3,)])

    main_function = _parse_main("questions/q031_q040/q040.py")
    # for ループが存在するか
    has_for = any(isinstance(node, ast.For) for node in ast.walk(main_function))
    # sorted() 呼び出しが存在するか
    has_sorted = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "sorted"
        for node in ast.walk(main_function)
    )
    assert has_for, "for 文を使ってください"
    assert has_sorted, "sorted() を使って順に出力してください"