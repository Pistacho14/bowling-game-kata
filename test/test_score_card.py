import pytest
from src.score_card import ScoreCard

@pytest.mark.extra_rolls
def test_frames_extra_roll():
    pins = "1212121212121212129/1"
    score_card = ScoreCard(pins)
    score_card._split_frames()
    frames = score_card.get_frames()
    assert frames == [
        ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'],
        ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'],
        ['9', '/', '1']
    ]

@pytest.mark.state_n
def test_frames_rolls():
    pins = "1212121212121212129-"
    score_card = ScoreCard(pins)
    score_card._split_frames()
    frames = score_card.get_frames()
    assert frames == [
        ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'],
        ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'],
        ['9', '0']
    ]

@pytest.mark.state_n
def test_numerical_frames_rolls():
    pins = "1212121212121212129-"
    score_card = ScoreCard(pins)
    score_card._split_frames()
    frames = score_card.get_clean_frames()
    assert frames == [
        [1, 2], [1, 2], [1, 2], [1, 2], [1, 2],
        [1, 2], [1, 2], [1, 2], [1, 2],
        [9, 0]
    ]

@pytest.mark.state_n
def test_numerical_frames_rolls_strike():
    pins = "X12X1212121212129-"
    score_card = ScoreCard(pins)
    score_card._split_frames()
    frames = score_card.get_clean_frames()
    assert frames == [
        [10], [1, 2], [10], [1, 2], [1, 2],
        [1, 2], [1, 2], [1, 2], [1, 2],
        [9, 0]
    ]

@pytest.mark.state_n
def test_numerical_frames_rolls_spare():
    pins = "1/121/1212121212129-"
    score_card = ScoreCard(pins)
    score_card._split_frames()
    frames = score_card.get_clean_frames()
    assert frames == [
        [1, 9], [1, 2], [1, 9], [1, 2], [1, 2],
        [1, 2], [1, 2], [1, 2], [1, 2],
        [9, 0]
    ]
    
@pytest.mark.state_n
def test_hitting_pins_regular():
    pins, total = "12345123451234512345", 60
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.state_n
def test_symbol_zero():
    pins, total = "9-9-9-9-9-9-9-9-9-9-", 90
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

    pins, total = "9-3561368153258-7181", 82
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.spare
def test_spare_not_extra():
    pins, total = "9-3/613/815/-/8-7/8-", 121
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.strike
def test_strike():
    pins, total = "X9-9-9-9-9-9-9-9-9-", 100
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

    pins, total = "X9-X9-9-9-9-9-9-9-", 110
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.strike
def test_two_strikes():
    pins, total = "XX9-9-9-9-9-9-9-9-", 120
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.strike
def test_three_strikes():
    pins, total = "XXX9-9-9-9-9-9-9-", 141
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.extra_rolls
def test_one_pin_in_extra_roll():
    pins, total = "9-3/613/815/-/8-7/8/8", 131
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

    pins, total = "5/5/5/5/5/5/5/5/5/5/5", 150
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.extra_rolls
def test_two_strikes_in_extra_rolls():
    pins, total = "9-9-9-9-9-9-9-9-9-XXX", 111
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.extra_rolls
def test_one_strike_in_extra_roll():
    pins, total = "8/549-XX5/53639/9/X", 149
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.extra_rolls
def test_spare_in_extra_roll():
    pins, total = "X5/X5/XX5/--5/X5/", 175
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total

@pytest.mark.extra_rolls
def test_triple_strike_before_extra_rolls():
    pins, total = "XXXXXXXXXXXX", 300
    score_card = ScoreCard(pins)
    assert score_card.score_calculator() == total
