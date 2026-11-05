import pytest
from customs_duty import duty_rate, total_duty, clearance_channel


# duty_rate() tests

def test_prohibited_weapons():
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("weapons", "FTA")


def test_prohibited_narcotics():
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("narcotics", "US")


def test_electronics_fta():
    assert duty_rate("electronics", "FTA") == 0.10


def test_electronics_non_fta():
    assert duty_rate("electronics", "US") == 0.20


def test_clothing_fta():
    assert duty_rate("clothing", "FTA") == 0.05


def test_clothing_non_fta():
    assert duty_rate("clothing", "US") == 0.12


def test_books():
    assert duty_rate("books", "US") == 0


def test_unknown_category():
    assert duty_rate("furniture", "US") == 0.15


# total_duty() tests

def test_negative_value():
    with pytest.raises(ValueError, match="negative value"):
        total_duty("electronics", -100, "US", False)


def test_gift_within_exemption():
    assert total_duty("electronics", 5000, "US", True) == 0


def test_gift_exceeding_exemption():
    assert total_duty("electronics", 6000, "FTA", True) == 100


def test_non_gift_within_exemption():
    assert total_duty("electronics", 1000, "US", False) == 0


def test_non_gift_exceeding_exemption():
    assert total_duty("electronics", 2000, "FTA", False) == 200


def test_minimum_duty_applied():
    assert total_duty("clothing", 5500, "FTA", True) == 50


def test_minimum_duty_not_applied():
    assert total_duty("electronics", 2000, "FTA", False) == 200


def test_zero_duty():
    assert total_duty("books", 2000, "US", False) == 0


def test_prohibited_item_in_total_duty():
    with pytest.raises(ValueError, match="prohibited item"):
        total_duty("weapons", 2000, "US", False)


# clearance_channel() tests

def test_prohibited_clearance():
    assert clearance_channel(100, "weapons", True) == "refuse"


def test_value_above_100000():
    assert clearance_channel(100001, "electronics", True) == "inspect"


def test_value_at_100000():
    assert clearance_channel(100000, "electronics", True) == "green"


def test_value_above_20000_without_documents():
    assert clearance_channel(20001, "electronics", False) == "inspect"


def test_value_above_20000_with_documents():
    assert clearance_channel(20001, "electronics", True) == "green"


def test_value_at_20000_without_documents():
    assert clearance_channel(20000, "electronics", False) == "green"


def test_low_value_clearance():
    assert clearance_channel(10000, "electronics", True) == "green"
