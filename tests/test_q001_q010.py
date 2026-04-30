import ast
from pathlib import Path

from tests.conftest import assert_question_prints


def _parse_main(relative_path: str) -> ast.FunctionDef:
    source_path = Path(f"F:/kkenj/workspace/python_100_knock/{relative_path}")
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    return next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")


def test_q001() -> None:
    assert_question_prints("questions/q001_q010/q001.py", "q001", [("Hello, World!",)])


def test_q002() -> None:
    assert_question_prints("questions/q001_q010/q002.py", "q002", [(1,), (2,), (3,)])


def test_q003() -> None:
    assert_question_prints("questions/q001_q010/q003.py", "q003", [(123, "Hello")])

    main_function = _parse_main("questions/q001_q010/q003.py")
    print_calls = [
        node for node in ast.walk(main_function) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print"
    ]

    assert len(print_calls) == 1
    assert len(print_calls[0].args) == 2


def test_q004() -> None:
    assert_question_prints("questions/q001_q010/q004.py", "q004", [(1,), (3,)])


def test_q005() -> None:
    assert_question_prints("questions/q001_q010/q005.py", "q005", [])


def test_q006() -> None:
    assert_question_prints("questions/q001_q010/q006.py", "q006", [(10,)])

    main_function = _parse_main("questions/q001_q010/q006.py")
    assigned_names = {
        target.id
        for node in ast.walk(main_function)
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
    }

    assert "x" in assigned_names


def test_q007() -> None:
    assert_question_prints("questions/q001_q010/q007.py", "q007", [(3,)])

    main_function = _parse_main("questions/q001_q010/q007.py")
    x_assignments = [
        node
        for node in ast.walk(main_function)
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "x" for target in node.targets)
    ]

    assert x_assignments
    assert any(isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.Add) for node in x_assignments)


def test_q008() -> None:
    assert_question_prints("questions/q001_q010/q008.py", "q008", [("12",)])

    main_function = _parse_main("questions/q001_q010/q008.py")
    x_assignments = [
        node
        for node in ast.walk(main_function)
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "x" for target in node.targets)
    ]

    assert x_assignments
    assert any(isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.Add) for node in x_assignments)


def test_q009() -> None:
    assert_question_prints("questions/q001_q010/q009.py", "q009", [("10",), (10,)])

    main_function = _parse_main("questions/q001_q010/q009.py")
    call_names = [
        node.func.id
        for node in ast.walk(main_function)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    ]

    assert "str" in call_names
    assert "int" in call_names


def test_q010() -> None:
    assert_question_prints("questions/q001_q010/q010.py", "q010", [("1\n2\n3",)])