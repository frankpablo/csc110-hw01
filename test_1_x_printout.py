import hw01  # Import the module here
import sys

def test_1_x_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: x = 27" in captured.out, "Tip: check the printout for x is EXACT"
