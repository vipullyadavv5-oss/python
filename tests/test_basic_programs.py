import subprocess
import sys


def run_script(script_name, user_input):
    result = subprocess.run(
        [sys.executable, script_name],
        input=user_input,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def test_reverse_string_script():
    output = run_script("reverse_string.py", "python\n")
    assert "Reversed String:" in output
    assert "nohtyp" in output


def test_count_digits_script():
    output = run_script("count_digits.py", "12345\n")
    assert "Total Digits: 5" in output


def test_sum_of_digits_script():
    output = run_script("sum_of_digits.py", "12345\n")
    assert "Sum of Digits: 15" in output


def test_todo_cli_script():
    output = run_script("todo_cli.py", "1\nBuy milk\n2\n5\n")
    assert "TODO MENU" in output
    assert "Task added: Buy milk" in output
    assert "Your tasks:" in output
