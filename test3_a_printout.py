import hw01  # Import the module here
import sys

def test3_a_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 3: a = 100" in captured.out, "Tip: check the printout for a is EXACT"
