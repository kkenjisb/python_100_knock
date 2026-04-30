from unittest.mock import patch

from tests.conftest import load_question_main, load_question_module


def test_q051() -> None:
    _, main = load_question_main("questions/q051_q060/q051.py", "q051")
    expected_calls = [
        (f"{left} × {right} = {left * right}",)
        for left in range(1, 10)
        for right in range(1, 10)
    ]

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == expected_calls


def test_q052() -> None:
    _, main = load_question_main("questions/q051_q060/q052.py", "q052")
    expected_calls = [(number,) for number in range(1, 100) if "3" in str(number)]

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == expected_calls


def test_q053() -> None:
    _, main = load_question_main("questions/q051_q060/q053.py", "q053")
    numbers = []
    value = 1
    while len(numbers) < 100:
        if "3" in str(value):
            numbers.append((value,))
        value += 1

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == numbers


def test_q054() -> None:
    _, main = load_question_main("questions/q051_q060/q054.py", "q054")
    expected_calls = [(value,) for value in [2, 4, 6, 8, 10, 12, 14, 16, 18]]

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == expected_calls


def test_q055() -> None:
    _, main = load_question_main("questions/q051_q060/q055.py", "q055")
    expected = [[f"{row}-{column}" for column in range(10)] for row in range(10)]

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with(expected)


def test_q056() -> None:
    _, main = load_question_main("questions/q051_q060/q056.py", "q056")

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with({"0": "0x30", "@": "0x40", "P": "0x50"})


def test_q057() -> None:
    _, main = load_question_main("questions/q051_q060/q057.py", "q057")
    expected_calls = [("h", 1), ("e", 1), ("l", 2), ("o", 1)]

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == expected_calls


def test_q058() -> None:
    _, main = load_question_main("questions/q051_q060/q058.py", "q058")

    with patch("builtins.print") as mock_print:
        main()

    mock_print.assert_called_once_with("1&2&3&5&7")


def test_q059() -> None:
    _, main = load_question_main("questions/q051_q060/q059.py", "q059")

    with patch("builtins.print") as mock_print:
        main()

    calls = [call.args for call in mock_print.call_args_list]
    assert calls[:2] == [(2,), (4,)]
    assert calls[2] == (6,)
    assert "NoneType" in str(calls[3][0])
    assert calls[4] == (10,)


def test_q060() -> None:
    _, main = load_question_main("questions/q051_q060/q060.py", "q060")
    expected_calls = [
        ("0001", "田中"),
        ("0002", "山田"),
        ("0003", "小林"),
        ("0005", "佐々木"),
        ("0007", "中村"),
        ("0010", "近藤"),
    ]

    with patch("builtins.print") as mock_print:
        main()

    assert [call.args for call in mock_print.call_args_list] == expected_calls


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
    module.SimpleClass.count = 0
    module.SimpleClass("A")
    module.SimpleClass("B")
    assert module.SimpleClass.count == 2

    with patch("builtins.print") as mock_print:
        module.SimpleClass.print_count()

    mock_print.assert_called_once_with(2)