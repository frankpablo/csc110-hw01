import hw01  # Import the module here
import sys

def test3_b_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 3: b = 13" in captured.out, "Tip: check the printout for b is EXACT"
