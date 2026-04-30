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
