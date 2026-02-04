import hw01  # Import the module here
import sys

def test2_y_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 2: y = -3" in captured.out, "Tip: check the printout for y is EXACT"
