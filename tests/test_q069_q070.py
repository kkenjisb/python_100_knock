from pathlib import Path
from unittest.mock import patch

from tests.conftest import WORKSPACE_ROOT, load_question_main, load_question_module


def test_q069() -> None:
    import_test_path = WORKSPACE_ROOT / "questions/q061_q070/import_test.py"
    assert import_test_path.exists(), "questions/q061_q070/import_test.py を作成してください"

    module = load_question_module("questions/q061_q070/import_test.py", "q069_import_test")
    assert hasattr(module, "sample")

    with patch("builtins.print") as mock_print:
        module.sample()
    mock_print.assert_called_once_with("Hello World")

    _, main = load_question_main("questions/q061_q070/q069.py", "q069")
    with patch("builtins.print") as mock_print:
        main()
    mock_print.assert_called_once_with("Hello World")


def test_q070() -> None:
    package_root = WORKSPACE_ROOT / "questions/q061_q070/library_test"
    assert (package_root / "__init__.py").exists(), "questions/q061_q070/library_test/__init__.py を作成してください"
    assert (package_root / "import_test.py").exists(), "questions/q061_q070/library_test/import_test.py を作成してください"

    module = load_question_module("questions/q061_q070/library_test/import_test.py", "q070_import_test")
    assert hasattr(module, "sample")

    with patch("builtins.print") as mock_print:
        module.sample()
    mock_print.assert_called_once_with("Hello World")

    _, main = load_question_main("questions/q061_q070/q070.py", "q070")
    with patch("builtins.print") as mock_print:
        main()
    mock_print.assert_called_once_with("Hello World")