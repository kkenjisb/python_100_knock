from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType
from unittest.mock import patch


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent


def load_question_module(relative_path: str, module_name: str) -> ModuleType:
    module_path = WORKSPACE_ROOT / relative_path
    spec = spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"module could not be loaded: {module_path}")

    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_question_main(relative_path: str, module_name: str):
    module = load_question_module(relative_path, module_name)
    assert hasattr(module, "main"), f"{relative_path} には main() を定義してください"
    return module, module.main


def assert_question_prints(relative_path: str, module_name: str, expected_calls: list[tuple]) -> None:
    _, main = load_question_main(relative_path, module_name)

    with patch("builtins.print") as mock_print:
        main()

    actual_calls = [call.args for call in mock_print.call_args_list]
    assert actual_calls == expected_calls