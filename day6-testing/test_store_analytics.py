"""
test_store_analytics.py

Starter file for the "write your own tests" exercise.

pytest and the module under test are already imported below, and there's
one fully-worked example test to show you the pattern. Everything after
that is up to you: add your own test functions (name them test_something)
that check store_analytics.py against its docstrings.

Run your tests from this folder with:
    pytest -v
"""

import pytest

from store_analytics import (
    parse_order_row,
    compute_line_total,
    summarize_by_product,
    top_n_products,
    apply_bulk_discount,
    loyalty_tier,
    load_orders_from_csv,
    write_top_products_report,
)


# --- Example test (already written for you) -------------------------------

def test_parse_order_row_valid_row():
    row = ["1001", "Widget", "4", "9.99", "alice@example.com"]
    order = parse_order_row(row)
    assert order == {
        "order_id": "1001",
        "product": "widget",
        "quantity": 4,
        "unit_price": 9.99,
        "customer_email": "alice@example.com",
    }


# --- Your tests go below here ----------------------------------------------

############################################################
# 
# Load up the CSV data one time for entire test session
# 
############################################################

@pytest.fixture(scope="module")

def orders_and_errors():
    filepath = "sample_orders.csv"
    orders, errors = load_orders_from_csv(filepath)
    return orders, errors


############################################################
#
# Code in function checks quantity * unit_price
# return round(order["quantity"] * order["unit_price"], 2)
#
############################################################

def test_compute_line_total():
    order = {
        "order_id": "1001",
        "product": "widget",
        "quantity": 4,
        "unit_price": 9.99,
        "customer_email": "alice@example.com",
    }

    total = compute_line_total(order)
    assert total == 39.96


############################################################
# 
# test_load_orders_from_csv()
#
# Verify the file loads
# 
############################################################
    
def test_load_orders_from_csv():
    filepath = "sample_orders.csv"
    orders, errors = load_orders_from_csv(filepath)
    assert isinstance(orders, list)


############################################################
#
# test_load_orders_errors_from_csv()
#
# Verify the file loads and checks for errors
#
############################################################

def test_load_orders_errors_from_csv():
    filepath = "sample_orders.csv"
    orders, errors = load_orders_from_csv(filepath)
    assert errors

    
############################################################
#
# test_compute_line_total_integrated()
#
# Reads the CSV and runs a test using data from it
#
#############################################################

def test_compute_line_total_with_file_load(orders_and_errors):
    orders, errors = orders_and_errors
    order = orders[0]
    assert int(order['quantity']) * float(order['unit_price']) == 39.96


############################################################
# 
# test_summarize_by_product()
#
# Check summary
#
# Actual data:
# {
#  'widget': {'total_quantity': 4, 'total_revenue': 39.96, 'order_count': 1},
#  'gadget': {'total_quantity': 3, 'total_revenue': 59.97, 'order_count': 2}
# }
# 
############################################################

@pytest.mark.parametrize("product, expected_quantity, expected_revenue, expected_count", [
    ("widget", 4, 39.96, 1),
    ("gadget", 3, 59.97, 2),
])

def test_summarize_by_product(orders_and_errors, product, expected_quantity, expected_revenue, expected_count):
    orders, errors = orders_and_errors
    summary = summarize_by_product(orders)

    assert product in summary
    assert summary[product]['total_quantity'] == expected_quantity
    assert summary[product]['total_revenue'] == expected_revenue
    assert summary[product]['order_count'] == expected_count
    

############################################################
#
# Now again but with assert messages
#
############################################################

@pytest.mark.parametrize("product, expected_quantity, expected_revenue, expected_count", [
    ("widget", 4, 39.96, 1),
    ("gadget", 3, 59.97, 2),
])

def test_summarize_by_product_with_messages(orders_and_errors, product, expected_quantity, expected_revenue, expected_count):
    orders, errors = orders_and_errors
    summary = summarize_by_product(orders)

    assert product in summary
    assert summary[product]['total_quantity'] == expected_quantity, f"{product}: quantity mismatch"
    assert summary[product]['total_revenue'] == expected_revenue, f"{product}: revenue mismatch"
    assert summary[product]['order_count'] == expected_count, f"{product}: count mismatch"


    
