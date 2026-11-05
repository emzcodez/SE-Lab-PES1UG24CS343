import pytest
from customs_duty import duty_rate, total_duty, clearance_channel


def test_books_are_duty_free():
    assert duty_rate("books", "FTA") == 0


def test_electronics_fta():
    assert duty_rate("electronics", "FTA") == 0.10


def test_electronics_non_fta():
    assert duty_rate("electronics", "US") == 0.20


def test_clothing_fta():
    assert duty_rate("clothing", "FTA") == 0.05


def test_clothing_non_fta():
    assert duty_rate("clothing", "US") == 0.12


def test_unknown_category():
    assert duty_rate("furniture", "US") == 0.15


def test_prohibited_category():
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("weapons", "US")


def test_low_value_personal_import():
    assert total_duty("books", 500, "US", False) == 0


def test_negative_value():
    with pytest.raises(ValueError, match="negative value"):
        total_duty("books", -100, "US", False)


def test_gift_below_limit():
    assert total_duty("electronics", 4000, "US", True) == 0


def test_gift_above_limit():
    assert total_duty("electronics", 6000, "FTA", True) == 100


def test_non_gift_above_limit():
    assert total_duty("electronics", 2000, "FTA", False) == 200


def test_minimum_duty_applied():
    assert total_duty("clothing", 5500, "FTA", True) == 50


def test_clearance_prohibited():
    assert clearance_channel(500, "narcotics", True) == "refuse"


def test_clearance_high_value():
    assert clearance_channel(150000, "electronics", True) == "inspect"


def test_clearance_missing_documents():
    assert clearance_channel(25000, "electronics", False) == "inspect"


def test_clearance_green():
    assert clearance_channel(10000, "electronics", True) == "green"
