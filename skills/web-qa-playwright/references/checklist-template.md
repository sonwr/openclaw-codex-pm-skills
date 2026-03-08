# Web QA Checklist Template (Fixed)

## Context
- Feature/PR:
- Target URL/environment:
- Build/commit:

## Functional checks (5 required)
1. [ ]
2. [ ]
3. [ ]
4. [ ]
5. [ ]

## Visual checks (3 required)
1. [ ]
2. [ ]
3. [ ]

## Off-happy-path checks (2 required)
1. [ ]
2. [ ]

## Evidence
- Screenshots:
  - [ ] `...`
  - [ ] `...`
  - [ ] `...`
- Execution log summary (checkpoint per check id: F1..F5, V1..V3, O1..O2, in this exact order):
  - F1 checkpoint:
  - F2 checkpoint:
  - F3 checkpoint:
  - F4 checkpoint:
  - F5 checkpoint:
  - V1 checkpoint:
  - V2 checkpoint:
  - V3 checkpoint:
  - O1 checkpoint:
  - O2 checkpoint:

## Failure recovery notes (only for FAIL checks)
- Check id:
  - Expected:
  - Observed:
  - First failure timestamp (UTC):
  - Retry: `PASS` / `FAIL`
  - Failure classification: `selector` / `runtime` / `product`
  - Evidence: `path/to/artifact.png`
  - Recovery plan:

## Results
- Regressions detected: `0`
- Merge recommendation: `APPROVE` / `BLOCK`
- Failure breakdown: `selector=0, runtime=0, product=0`
- Notes:
