from lab02 import seconds_to_hms, admission_price, sum_multiples, total_of_positives

def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    hours: int
    minutes: int
    seconds: int
    hours = total_seconds//3600
    minutes = total_seconds%3600//60
    seconds = total_seconds%60
    return f"{hours}:{minutes:02d}:{seconds:02d}"


def test_seconds_to_hms():
    assert seconds_to_hms(3661) == "1:01:01"
    assert seconds_to_hms(59) == "0:00:59"
    assert seconds_to_hms(3600) == "1:00:00"
    assert seconds_to_hms(7325) == "2:02:05"
    assert seconds_to_hms(0) == "0:00:00"


def test_admission_price():
    assert admission_price(3) == 0
    assert admission_price(5) == 8
    assert admission_price(12) == 8
    assert admission_price(13) == 15
    assert admission_price(64) == 15
    assert admission_price(65) == 10
    assert admission_price(30) == 15
    assert admission_price(70) == 10


def test_sum_multiples():
    assert sum_multiples(10) == 23
    assert sum_multiples(1) == 0
    assert sum_multiples(0) == 0
    assert sum_multiples(16) == 60
    assert sum_multiples(20) == 78


# STRETCH (optional) - skipping this one still passes the three above.
def test_total_of_positives():
    assert total_of_positives([1, -2, 3, -4, 5]) == 9
    assert total_of_positives([-1, -2]) == 0
    assert total_of_positives([]) == 0
    assert total_of_positives([10, 20]) == 30
