import hw01  # Import the module here
import sys

def test1_x_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: x = 27" in captured.out, "Tip: check the printout for x is EXACT"

def test1_y_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: y = 1" in captured.out, "Tip: check the printout for y is EXACT"

def test1_a_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: a = 1.5" in captured.out, "Tip: check the printout for a is EXACT"

def test1_b_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: b = 7" in captured.out, "Tip: check the printout for b is EXACT"

def test1_c_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: c = -1" in captured.out, "Tip: check the printout for c is EXACT"

def test1_result1_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 1: result = 3.0" in captured.out, "Tip: check the printout for part1's result is EXACT"

def test2_x_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 2: x = 5" in captured.out, "Tip: check the printout for x is EXACT"

def test2_y_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 2: y = -3" in captured.out, "Tip: check the printout for y is EXACT"

def test2_result2_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 2: result = 2025" in captured.out, "Tip: check the printout for part2's result is EXACT"

def test3_a_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 3: a = 100" in captured.out, "Tip: check the printout for a is EXACT"

def test3_b_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 3: b = 13" in captured.out, "Tip: check the printout for b is EXACT"

def test3_result3_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 3: result = 7" in captured.out, "Tip: check the printout for part3's result is EXACT"

def test4_result4_printout(capsys):
    hw01.main()
    captured = capsys.readouterr()
    assert "Part 4: result = 9" in captured.out, "Tip: check the printout for part4's result is EXACT"
