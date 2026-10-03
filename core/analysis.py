def validate_holdings(holdings):
    if not isinstance(holdings, list) or not holdings:
        raise ValueError("holdings must be a non-empty list")
    for h in holdings:
        if not isinstance(h, dict):
            raise ValueError("each holding must be an object")
        for key in ("symbol", "quantity", "price"):
            if key not in h:
                raise ValueError(f"missing required field: {key}")
        if not isinstance(h["symbol"], str) or not h["symbol"].strip():
            raise ValueError("symbol must be a non-empty string")
        if not isinstance(h["quantity"], (int, float)) or h["quantity"] < 0:
            raise ValueError("quantity must be non-negative")
        if not isinstance(h["price"], (int, float)) or h["price"] < 0:
            raise ValueError("price must be non-negative")

def analyze_portfolio(holdings):
    validate_holdings(holdings)
    values = []
    for h in holdings:
        values.append((h["symbol"], h["quantity"] * h["price"]))
    total = sum(v for _, v in values)
    allocations = {s: (v / total * 100 if total else 0.0) for s, v in values}
    return {"total_value": total, "holding_values": dict(values), "allocations_percent": allocations}

def analyze_risk(holdings):
    result = analyze_portfolio(holdings)
    allocations = result["allocations_percent"]
    max_symbol = max(allocations, key=allocations.get)
    max_weight = allocations[max_symbol]
    return {
        "largest_holding": max_symbol,
        "largest_allocation_percent": max_weight,
        "concentration_flag": max_weight > 25.0,
    }

def analyze_allocation(holdings, target_allocations):
    if not isinstance(target_allocations, dict):
        raise ValueError("target_allocations must be an object")
    actual = analyze_portfolio(holdings)["allocations_percent"]
    deviations = {s: actual.get(s, 0.0) - float(target_allocations.get(s, 0.0))
                  for s in set(actual) | set(target_allocations)}
    return {"actual_allocations_percent": actual, "deviation_percent": deviations}
