import pytest
from src.score_card import Score_card

@pytest.mark.state_n
def test_hitting_pins_regular():
    # Hitting pins total = 60
    pins = "12345123451234512345"
    total = 60
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.state_n
def test_symbol_zero():
    # test symbol
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    score_card = Score_card(pins)
    assert score_card == total

    pins = "9-3561368153258-7181"
    total = 82
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.spare
def test_spare_not_extra():
    # test spare not extra
    pins = "9-3/613/815/-/8-7/8-"
    total = 121
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.strike
def test_strike():
    # test strike
    pins = "X9-9-9-9-9-9-9-9-9-"
    total = 100
    score_card = Score_card(pins)
    assert score_card == total

    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.strike
def test_two_strikes():
    # two strikes in a row is a double
    pins = "XX9-9-9-9-9-9-9-9-"
    total = 120
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.strike
def test_three_strikes():
    # three strikes in a row is a triple
    pins = "XXX9-9-9-9-9-9-9-"
    total = 141
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.extra_rolls
def test_one_pin_in_extra_roll():
    # one pin in extra roll
    pins = "9-3/613/815/-/8-7/8/8"
    total = 131
    score_card = Score_card(pins)
    assert score_card == total

    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.extra_rolls
def test_two_strikes_in_extra_rolls():
    # two strikes in extra rolls
    pins = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.extra_rolls
def test_one_strike_in_extra_roll():
    # one strike in extra roll
    pins = "8/549-XX5/53639/9/X"
    total = 149
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.extra_rolls
def test_spare_in_extra_roll():
    # spare in extra roll
    pins = "X5/X5/XX5/--5/X5/"
    total = 175
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.extra_rolls
def test_triple_strike_before_extra_rolls():
    # 12 strikes is a “Thanksgiving Turkey”
    # 2 strikes in extra rolls
    pins = "XXXXXXXXXXXX"
    total = 300
    score_card = Score_card(pins)
    assert score_card == total

@pytest.mark.extra_rolls
def test_split_frames_extra_roll():
    pins = "1212121212121212129/1"
    score_card = Score_card(pins)
    frames = score_card.split_frames()
    assert frames == [
        ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'],
        ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'],
        ['9', '/', '1']
    ]

@pytest.mark.state_n
def test_split_frames_rolls():
    pins = "1212121212121212129-"
    score_card = Score_card(pins)
    frames = score_card.split_frames()
    assert frames == [
        ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'],
        ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'],
        ['9', '-']
    ]