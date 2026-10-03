from core.analysis import analyze_portfolio, analyze_risk, analyze_allocation
import pytest

H = [
    {"symbol": "AAA", "quantity": 10, "price": 100},
    {"symbol": "BBB", "quantity": 5, "price": 100},
]

def test_portfolio_value():
    r = analyze_portfolio(H)
    assert r["total_value"] == 1500
    assert r["allocations_percent"]["AAA"] == pytest.approx(66.6666667)

def test_risk_concentration():
    r = analyze_risk(H)
    assert r["largest_holding"] == "AAA"
    assert r["concentration_flag"] is True

def test_allocation():
    r = analyze_allocation(H, {"AAA": 50, "BBB": 50})
    assert r["deviation_percent"]["AAA"] == pytest.approx(16.6666667)

def test_invalid_holdings():
    with pytest.raises(ValueError):
        analyze_portfolio([])

def test_missing_field():
    with pytest.raises(ValueError):
        analyze_portfolio([{"symbol": "AAA", "quantity": 1}])
