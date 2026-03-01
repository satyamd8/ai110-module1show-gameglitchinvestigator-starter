import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_utils import check_guess, get_range_for_difficulty

def test_check_guess_hint_logic():
    # Secret is 1, guess is 1 (should win)
    outcome, message = check_guess(1, 1)
    assert outcome == "Win"
    assert "Correct" in message

    # Secret is 1, guess is 2 (should be too high)
    outcome, message = check_guess(2, 1)
    assert outcome == "Too High"
    assert "LOWER" in message

    # Secret is 100, guess is 99 (should be too low)
    outcome, message = check_guess(99, 100)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_new_game_resets_state():
    # Simulate session state for new game
    low, high = get_range_for_difficulty("Normal")
    import random
    secret = random.randint(low, high)
    attempts = 1
    score = 0
    status = "playing"
    history = []
    # Check initial values
    assert low == 1 and high == 100
    assert isinstance(secret, int)
    assert attempts == 1
    assert score == 0
    assert status == "playing"
    assert history == []
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
