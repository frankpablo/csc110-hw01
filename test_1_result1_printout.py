import hw01  # Import the module here
import sys

def test_1_result1_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: result = 3.0" in captured.out, "Tip: check the printout for part1's result is EXACT"