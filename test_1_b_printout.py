import hw01  # Import the module here
import sys

def test_1_b_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: b = 7" in captured.out, "Tip: check the printout for b is EXACT"