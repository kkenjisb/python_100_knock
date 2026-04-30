from pathlib import Path
from unittest.mock import patch

from tests.conftest import WORKSPACE_ROOT, load_question_main, load_question_module


def test_q061() -> None:
    module = load_question_module("questions/q061_q070/q061.py", "q061")
    assert hasattr(module, "sample")

    with patch("builtins.print") as mock_print:
        module.sample()
    mock_print.assert_called_once_with("Hello World")

    _, main = load_question_main("questions/q061_q070/q061.py", "q061_main")
    with patch("builtins.print") as mock_print:
        main()
    assert [call.args for call in mock_print.call_args_list] == [("Hello World",)] * 3


def test_q062() -> None:
    module = load_question_module("questions/q061_q070/q062.py", "q062")
    assert hasattr(module, "greet")

    with patch("builtins.print") as mock_print:
        module.greet("テスト")
    mock_print.assert_called_once_with("こんにちは、テスト さん")


def test_q063() -> None:
    module, main = load_question_main("questions/q061_q070/q063.py", "q063")
    assert module.add(1, 2) == 3

    with patch("builtins.print") as mock_print:
        main()
    mock_print.assert_called_once_with(3)


def test_q064() -> None:
    module, main = load_question_main("questions/q061_q070/q064.py", "q064")
    assert hasattr(module, "welcome_message")

    with patch("builtins.print") as mock_print:
        main()
    assert [call.args for call in mock_print.call_args_list] == [
        ("ようこそ、ゲスト さん",),
        ("ようこそ、管理者 さん",),
    ]


def test_q065() -> None:
    module = load_question_module("questions/q061_q070/q065.py", "q065")
    assert hasattr(module, "print_args")

    with patch("builtins.print") as mock_print:
        module.print_args("A", "B", key1="X", key2="Y")

    assert [call.args for call in mock_print.call_args_list] == [
        (("A", "B"),),
        ({"key1": "X", "key2": "Y"},),
    ]


def test_q066() -> None:
    module = load_question_module("questions/q061_q070/q066.py", "q066")
    assert hasattr(module, "SimpleClass")

    with patch("builtins.print") as mock_print:
        module.SimpleClass("サンプル")

    mock_print.assert_called_once_with("名前が サンプル のオブジェクトを作成しました")


def test_q067() -> None:
    module = load_question_module("questions/q061_q070/q067.py", "q067")
    instance = module.SimpleClass("サンプル")
    assert instance.name == "サンプル"

    with patch("builtins.print") as mock_print:
        instance.print_name()

    mock_print.assert_called_once_with("サンプル")


def test_q068() -> None:
    module = load_question_module("questions/q061_q070/q068.py", "q068")
    assert hasattr(module, "SimpleClass"), "SimpleClass を定義してください"
    assert hasattr(module.SimpleClass, "count"), "クラス変数 count を定義してください"
    assert hasattr(module.SimpleClass, "print_count"), "クラスメソッド print_count を定義してください"

    # count がインスタンス生成ごとに増加するか確認
    initial_count = module.SimpleClass.count
    module.SimpleClass("A")
    module.SimpleClass("B")
    assert module.SimpleClass.count == initial_count + 2, "インスタンス生成のたびに count を増加させてください"

    with patch("builtins.print") as mock_print:
        module.SimpleClass.print_count()
    mock_print.assert_called_once_with(module.SimpleClass.count)


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
