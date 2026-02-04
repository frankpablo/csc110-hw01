import hw01  # Import the module here
import sys

def test2_result2_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 2: result = 2025" in captured.out, "Tip: check the printout for part2's result is EXACT"
