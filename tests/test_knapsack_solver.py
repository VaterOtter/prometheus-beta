import pytest
from src.knapsack_solver import solve_knapsack, Item

def test_basic_knapsack():
    """Test a basic knapsack scenario."""
    items = [
        Item(weight=10, value=60),
        Item(weight=20, value=100),
        Item(weight=30, value=120)
    ]
    max_weight = 50
    
    total_value, selected_items = solve_knapsack(items, max_weight)
    
    assert total_value == 220
    assert len(selected_items) == 2
    assert {(item.weight, item.value) for item in selected_items} == {(10, 60), (20, 100)}

def test_empty_items_list():
    """Test knapsack with empty items list."""
    items = []
    max_weight = 50
    
    total_value, selected_items = solve_knapsack(items, max_weight)
    
    assert total_value == 0
    assert selected_items == []

def test_zero_max_weight():
    """Test knapsack with zero max weight."""
    items = [
        Item(weight=10, value=60),
        Item(weight=20, value=100)
    ]
    max_weight = 0
    
    total_value, selected_items = solve_knapsack(items, max_weight)
    
    assert total_value == 0
    assert selected_items == []

def test_negative_max_weight():
    """Test knapsack with negative max weight."""
    items = [
        Item(weight=10, value=60),
        Item(weight=20, value=100)
    ]
    max_weight = -10
    
    with pytest.raises(ValueError, match="Maximum weight must be non-negative"):
        solve_knapsack(items, max_weight)

def test_single_item_fits():
    """Test knapsack with a single item that fits."""
    items = [Item(weight=10, value=100)]
    max_weight = 20
    
    total_value, selected_items = solve_knapsack(items, max_weight)
    
    assert total_value == 100
    assert len(selected_items) == 1
    assert selected_items[0].weight == 10
    assert selected_items[0].value == 100

def test_single_item_does_not_fit():
    """Test knapsack with a single item that does not fit."""
    items = [Item(weight=30, value=100)]
    max_weight = 20
    
    total_value, selected_items = solve_knapsack(items, max_weight)
    
    assert total_value == 0
    assert selected_items == []

def test_fractional_weights():
    """Test knapsack with fractional weights."""
    items = [
        Item(weight=10.5, value=60),
        Item(weight=20.2, value=100),
        Item(weight=30.7, value=120)
    ]
    max_weight = 50.5
    
    total_value, selected_items = solve_knapsack(items, max_weight)
    
    assert total_value == 160
    assert len(selected_items) == 2
    assert {(item.weight, item.value) for item in selected_items} == {(10.5, 60), (20.2, 100)}

def test_complex_knapsack_scenario():
    """Test a more complex knapsack scenario with multiple possible combinations."""
    items = [
        Item(weight=2, value=3),
        Item(weight=3, value=4),
        Item(weight=4, value=5),
        Item(weight=5, value=6)
    ]
    max_weight = 10
    
    total_value, selected_items = solve_knapsack(items, max_weight)
    
    assert total_value == 13
    assert len(selected_items) == 3
    assert {(item.weight, item.value) for item in selected_items} == {(2, 3), (3, 4), (5, 6)}