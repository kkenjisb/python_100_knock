import ast
from pathlib import Path

from tests.conftest import assert_question_prints


def _parse_main(relative_path: str) -> ast.FunctionDef:
    source_path = Path(f"F:/kkenj/workspace/python_100_knock/{relative_path}")
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    return next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")


def test_q021() -> None:
    assert_question_prints("questions/q021_q030/q021.py", "q021", [(3,)])

    main_function = _parse_main("questions/q021_q030/q021.py")
    # len() を呼び出しているか
    has_len_call = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "len"
        for node in ast.walk(main_function)
    )
    # lst 変数に代入しているか
    has_lst_assign = any(
        isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "lst" for t in node.targets)
        for node in ast.walk(main_function)
    )
    assert has_lst_assign, "変数 lst にリストを代入してください"
    assert has_len_call, "len() 関数を使ってください"


def test_q022() -> None:
    assert_question_prints("questions/q021_q030/q022.py", "q022", [([1, 3],)])

    main_function = _parse_main("questions/q021_q030/q022.py")
    # .remove() または .pop() を呼び出しているか
    has_remove_or_pop = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in ("remove", "pop")
        for node in ast.walk(main_function)
    )
    assert has_remove_or_pop, "remove() か pop() を使ってリストから要素を削除してください"


def test_q023() -> None:
    assert_question_prints("questions/q021_q030/q023.py", "q023", [([1, 2, 3, 4],)])

    main_function = _parse_main("questions/q021_q030/q023.py")
    # + 演算子 (BinOp with Add) か extend() を使っているか
    has_list_concat = any(
        isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add)
        for node in ast.walk(main_function)
    )
    has_extend = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "extend"
        for node in ast.walk(main_function)
    )
    assert has_list_concat or has_extend, "+ 演算子か extend() を使ってリストを結合してください"


def test_q024() -> None:
    assert_question_prints("questions/q021_q030/q024.py", "q024", [("xは10より大きい",)])

    main_function = _parse_main("questions/q021_q030/q024.py")
    # if 文が存在するか
    has_if = any(isinstance(node, ast.If) for node in ast.walk(main_function))
    # x > 10 のような比較が存在するか
    has_gt_compare = any(
        isinstance(node, ast.Compare)
        and any(isinstance(op, ast.Gt) for op in node.ops)
        for node in ast.walk(main_function)
    )
    assert has_if, "if 文を使ってください"
    assert has_gt_compare, "> 演算子を使った比較を行ってください"


def test_q025() -> None:
    assert_question_prints("questions/q021_q030/q025.py", "q025", [("xは5より大きいが、10以下",)])

    main_function = _parse_main("questions/q021_q030/q025.py")
    # elif に相当する: If ノードの orelse に別の If ノードが入っているか
    has_elif = any(
        isinstance(node, ast.If)
        and len(node.orelse) == 1
        and isinstance(node.orelse[0], ast.If)
        for node in ast.walk(main_function)
    )
    # else に相当する: If ノードの orelse が空でなく、中身が If ではないか
    has_else = any(
        isinstance(node, ast.If)
        and len(node.orelse) > 0
        and not isinstance(node.orelse[0], ast.If)
        for node in ast.walk(main_function)
    )
    assert has_elif, "elif を使って条件分岐してください"
    assert has_else, "else を使って条件分岐してください"


def test_q026() -> None:
    assert_question_prints("questions/q021_q030/q026.py", "q026", [(False,), (False,), (False,), (True,), (True,)])

    main_function = _parse_main("questions/q021_q030/q026.py")
    # 比較演算子 >, >=, ==, <=, < をすべて使っているか
    ops_used: set[type] = set()
    for node in ast.walk(main_function):
        if isinstance(node, ast.Compare):
            for op in node.ops:
                ops_used.add(type(op))
    required_ops = {ast.Gt, ast.GtE, ast.Eq, ast.LtE, ast.Lt}
    missing = required_ops - ops_used
    assert not missing, f"比較演算子 {[op.__name__ for op in missing]} が使われていません"


def test_q027() -> None:
    assert_question_prints("questions/q021_q030/q027.py", "q027", [(True,)])

    main_function = _parse_main("questions/q021_q030/q027.py")
    # in 演算子を使っているか
    has_in = any(
        isinstance(node, ast.Compare)
        and any(isinstance(op, ast.In) for op in node.ops)
        for node in ast.walk(main_function)
    )
    assert has_in, "in 演算子を使ってください"


def test_q028() -> None:
    assert_question_prints("questions/q021_q030/q028.py", "q028", [(True,)])

    main_function = _parse_main("questions/q021_q030/q028.py")
    # is None の比較が存在するか
    has_is_none = any(
        isinstance(node, ast.Compare)
        and any(isinstance(op, ast.Is) for op in node.ops)
        and any(isinstance(c, ast.Constant) and c.value is None for c in node.comparators)
        for node in ast.walk(main_function)
    )
    # None への変数代入が存在するか
    has_none_assign = any(
        isinstance(node, ast.Assign)
        and isinstance(node.value, ast.Constant)
        and node.value.value is None
        for node in ast.walk(main_function)
    )
    assert has_none_assign, "変数に None を代入してください"
    assert has_is_none, "is 演算子を使って None との比較を行ってください"


def test_q029() -> None:
    assert_question_prints("questions/q021_q030/q029.py", "q029", [(False,), (True,)])

    main_function = _parse_main("questions/q021_q030/q029.py")
    # and 演算子を使っているか
    has_and = any(
        isinstance(node, ast.BoolOp) and isinstance(node.op, ast.And)
        for node in ast.walk(main_function)
    )
    # or 演算子を使っているか
    has_or = any(
        isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or)
        for node in ast.walk(main_function)
    )
    assert has_and, "and 演算子を使ってください"
    assert has_or, "or 演算子を使ってください"


def test_q030() -> None:
    assert_question_prints("questions/q021_q030/q030.py", "q030", [])

    main_function = _parse_main("questions/q021_q030/q030.py")
    has_none_assignment = any(
        isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) and node.value.value is None
        for node in ast.walk(main_function)
    )
    has_is_none_check = any(
        isinstance(node, ast.Compare)
        and any(isinstance(operator, ast.Is) for operator in node.ops)
        and any(isinstance(comparator, ast.Constant) and comparator.value is None for comparator in node.comparators)
        for node in ast.walk(main_function)
    )

    assert has_none_assignment
    assert has_is_none_check