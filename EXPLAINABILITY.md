# Explainability

## Inputs and Data Sources

The agent accepts caller-provided portfolio holdings, quantities, prices, returns, sectors, and optional target allocations.

### Input Requirements

Each tool validates required fields, data types, numeric ranges, and unexpected fields before processing.

### Data Sources

The core implementation uses only caller-provided data. It does not retrieve live prices, financial news, brokerage records, or external market feeds.

### Failure Handling

Missing required fields, invalid types, negative quantities where unsupported, malformed holdings, and unexpected fields are rejected.

## Decision and Reasoning

All calculations are deterministic and traceable to supplied inputs.

### Rules Applied

- Portfolio value is calculated from quantity multiplied by supplied price.
- Allocation percentages are calculated from supplied holding values and total portfolio value.
- Concentration indicators use explicit threshold rules.
- Risk analysis uses supplied volatility and return fields when available.
- Allocation analysis compares actual weights with caller-provided target weights.

### Expected Outputs

Outputs contain calculated portfolio metrics, concentration observations, risk indicators, or allocation differences.

### Determinism

Identical valid inputs produce identical results.

## Limits and Constraints

The agent does not provide live market data, price forecasts, guaranteed returns, or personalized investment recommendations.

### Constraints

Results depend entirely on the supplied data and assumptions.

### Known Issues

Portfolio metrics may become stale when supplied prices or quantities are outdated.

### Unsupported Behavior

The agent does not execute trades, access brokerage accounts, fabricate missing market values, or claim external verification.

## Tool Documentation

### analyze-portfolio

#### Inputs
- holdings

#### Decision
Calculates holding values, total portfolio value, and allocation percentages from supplied quantities and prices.

#### Outputs
Returns deterministic portfolio metrics.

#### Failure Handling
Rejects malformed holdings and invalid numeric values.

#### Limits
No live prices or external market information are used.

### analyze-risk

#### Inputs
- holdings

#### Decision
Evaluates supplied risk indicators such as concentration and volatility when present.

#### Outputs
Returns deterministic risk observations.

#### Failure Handling
Rejects malformed input and unsupported values.

#### Limits
This is an analytical summary, not a prediction or guarantee.

### analyze-allocation

#### Inputs
- holdings
- target_allocations

#### Decision
Compares actual allocation with caller-provided target allocation.

#### Outputs
Returns allocation differences and deviation information.

#### Failure Handling
Rejects malformed holdings, invalid targets, and unexpected fields.

#### Limits
Targets must be supplied by the caller; the agent does not invent an appropriate portfolio allocation.

## Traceability

Every result is derived from explicit inputs and documented calculations.

## Transparency

The agent distinguishes supplied data, calculated metrics, and limitations.

## Safety and Scope

The agent provides analytical information only. Human users remain responsible for financial decisions.
