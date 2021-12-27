from hashish import __version__
from hashish import hashish
from elftools.common.exceptions import ELFError

import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_invalid_file():
    with open('tests/wrong_elf_file','rb') as f:
        with pytest.raises(Exception) as exc_info:
            hashish.hash_section(f,".data")

        exception_raised = exc_info.value

def test_invalid_section():
    with open('tests/simple_c_program','rb') as f:
        with pytest.raises(Exception) as exc_info:
            hashish.hash_section(f,".wathever")

        exception_raised = exc_info.value

def test_normal_behaviour():
    with open('tests/simple_c_program','rb') as f:
        hash = hashish.hash_section(f,".data")
    assert hash=='c8362a4e583ef4a36986019d0aecf8b2a1a692c6d8c78b8bb2999d0e2a987aac'
