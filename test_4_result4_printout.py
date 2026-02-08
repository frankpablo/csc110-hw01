import hw01  # Import the module here
import sys

def test_4_result4_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 4: result = 9" in captured.out, "Tip: check the printout for part4's result is EXACT"
