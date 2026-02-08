import hw01  # Import the module here
import sys

def test_1_y_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: y = 1" in captured.out, "Tip: check the printout for y is EXACT"
