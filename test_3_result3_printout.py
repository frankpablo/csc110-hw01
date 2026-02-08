import hw01  # Import the module here
import sys

def test_3_result3_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 3: result = 7" in captured.out, "Tip: check the printout for part3's result is EXACT"
