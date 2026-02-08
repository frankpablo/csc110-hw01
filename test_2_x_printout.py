import hw01  # Import the module here
import sys

def test_2_x_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 2: x = 5" in captured.out, "Tip: check the printout for x is EXACT"
