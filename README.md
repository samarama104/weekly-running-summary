# Weekly Running Summary

A Python command-line tool that summarizes a list of running
distances in miles.

## Features

- Counts logged sessions, including zero-mile sessions.
- Calculates total mileage, longest run, and average distance.
- Displays distances to two decimal places.
- Handles an empty list without crashing.

## Requirements

Python 3. No additional packages required.

## How to run

1. Open running_summary.py and edit the distances list:

```python
distances = [3.0, 4.5, 0.0, 6.0]
```

2. Save the file.
3. Open a terminal in the project folder and run:

```bash
python3 running_summary.py
```

## Example output

```text
Logged sessions: 4
Total mileage: 13.50 miles
Longest run: 6.00 miles
Average distance: 3.38 miles
```

The average includes every logged session, including zero-mile entries.

## Example checks

| Distances | Expected result |
|---|---|
| [3.0, 4.5, 0.0, 6.0] | 4 sessions; 13.50 total; 6.00 longest; 3.38 average |
| [5.0] | 1 session; total, longest, and average all 5.00 |
| [] | No sessions logged. |

## What I practiced

- Storing numbers in a list.
- Using len(), sum(), and max().
- Calculating an average.
- Formatting numbers with f-strings.
- Using conditionals to handle an empty list.

## Limitations

- Distances must be edited directly in the code.
- Assumes all entries are nonnegative numbers.
- Uses miles only.
- Does not store dates or group sessions by calendar week.