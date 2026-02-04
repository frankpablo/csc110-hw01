import hw01  # Import the module here
import sys

def test1_a_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: a = 1.5" in captured.out, "Tip: check the printout for a is EXACT"