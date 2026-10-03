from core.analysis import analyze_allocation
def run(input_data):
    return analyze_allocation(input_data["holdings"], input_data["target_allocations"])
