import ast
from pathlib import Path

from tests.conftest import assert_question_prints


def _read_source(relative_path: str) -> str:
    source_path = Path(f"F:/kkenj/workspace/python_100_knock/{relative_path}")
    return source_path.read_text(encoding="utf-8")


def _parse_main(relative_path: str) -> ast.FunctionDef:
    tree = ast.parse(_read_source(relative_path))
    return next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")


def test_q011() -> None:
    assert_question_prints("questions/q011_q020/q011.py", "q011", [(r"C:\test",)])

    source = _read_source("questions/q011_q020/q011.py")
    assert '"C:\\test"' in source or "'C:\\\\test'" in source


def test_q012() -> None:
    assert_question_prints("questions/q011_q020/q012.py", "q012", [(r"C:\test",)])

    source = _read_source("questions/q011_q020/q012.py")
    assert 'r"C:\test"' in source or "r'C:\\test'" in source


def test_q013() -> None:
    assert_question_prints("questions/q011_q020/q013.py", "q013", [("Hello, Python!",)])

    main_function = _parse_main("questions/q011_q020/q013.py")
    assigned_names = {
        target.id
        for node in ast.walk(main_function)
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
    }
    f_strings = [node for node in ast.walk(main_function) if isinstance(node, ast.JoinedStr)]

    assert "name" in assigned_names
    assert f_strings


def test_q014() -> None:
    assert_question_prints("questions/q011_q020/q014.py", "q014", [(6,)])

    main_function = _parse_main("questions/q011_q020/q014.py")
    assert any(
        isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "len"
        for node in ast.walk(main_function)
    )


def test_q015() -> None:
    assert_question_prints("questions/q011_q020/q015.py", "q015", [("Py",)])

    main_function = _parse_main("questions/q011_q020/q015.py")
    assert any(
        isinstance(node, ast.Subscript)
        and isinstance(node.slice, ast.Slice)
        and isinstance(node.slice.upper, ast.Constant)
        and node.slice.upper.value == 2
        for node in ast.walk(main_function)
    )


def test_q016() -> None:
    assert_question_prints("questions/q011_q020/q016.py", "q016", [(None,)])

    main_function = _parse_main("questions/q011_q020/q016.py")
    assert any(
        isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) and node.value.value is None
        for node in ast.walk(main_function)
    )


def test_q017() -> None:
    assert_question_prints("questions/q011_q020/q017.py", "q017", [(int,), (float,), (str,), (bool,)])

    main_function = _parse_main("questions/q011_q020/q017.py")
    assigned_names = {
        target.id
        for node in ast.walk(main_function)
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
    }
    type_calls = [
        node for node in ast.walk(main_function) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "type"
    ]

    assert {"a", "b", "c", "d"}.issubset(assigned_names)
    assert len(type_calls) >= 4


def test_q018() -> None:
    assert_question_prints("questions/q011_q020/q018.py", "q018", [([1, 2, 3],), (1,)])

    main_function = _parse_main("questions/q011_q020/q018.py")
    assigned_names = {
        target.id
        for node in ast.walk(main_function)
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
    }
    subscripts = [node for node in ast.walk(main_function) if isinstance(node, ast.Subscript)]

    assert "lst" in assigned_names
    assert subscripts


def test_q019() -> None:
    assert_question_prints("questions/q011_q020/q019.py", "q019", [([1, 2],)])

    main_function = _parse_main("questions/q011_q020/q019.py")
    assigned_names = {
        target.id
        for node in ast.walk(main_function)
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
    }

    assert "lst" in assigned_names
    assert any(
        isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice)
        for node in ast.walk(main_function)
    )


def test_q020() -> None:
    assert_question_prints("questions/q011_q020/q020.py", "q020", [([1, 2, 3, 4],)])

    main_function = _parse_main("questions/q011_q020/q020.py")
    assigned_names = {
        target.id
        for node in ast.walk(main_function)
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
    }
    append_calls = [
        node
        for node in ast.walk(main_function)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "append"
    ]

    assert "lst" in assigned_names
    assert append_calls