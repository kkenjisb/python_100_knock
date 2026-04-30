from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType


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