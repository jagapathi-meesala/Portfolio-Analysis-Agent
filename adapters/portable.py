from tools.analyze_portfolio import run as analyze_portfolio
from tools.analyze_risk import run as analyze_risk
from tools.analyze_allocation import run as analyze_allocation

TOOLS = {
    "analyze-portfolio": analyze_portfolio,
    "analyze-risk": analyze_risk,
    "analyze-allocation": analyze_allocation,
}

def invoke(name, input_data):
    if name not in TOOLS:
        raise ValueError(f"unknown tool: {name}")
    return TOOLS[name](input_data)
