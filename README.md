# Work Time Calculator

A simple Python script that calculates how much time you still need to work after lunch based on your daily workload.

## Features

* Define your daily workload (supports decimal values like `7.5` hours).
* Enter your:

  * Clock-in time
  * Lunch start time
  * Lunch end time
* Calculates:

  * Time worked before lunch
  * Remaining work time
  * Expected clock-out time

## Requirements

* Python 3.8 or newer

## Usage

Run the script:

```bash
python main.py
```

Example:

```text
Daily workload (hours): 8
Clock in (HH:MM): 08:00
Lunch start (HH:MM): 12:00
Lunch end (HH:MM): 13:00
```

Output:

```text
========== Work Summary ==========
Daily workload : 8.00 hours
Worked morning : 4:00:00
Worked total   : 4:00:00
Remaining work : 4:00:00
Clock out at   : 17:00
==================================
```

## Time Format

All time inputs must follow the 24-hour format:

```text
HH:MM
```

Examples:

* `08:00`
* `12:30`
* `17:45`

## Notes

* The script assumes a single lunch break.
* The workload can be an integer or a decimal (e.g., `6`, `7.5`, `8`).
* The expected clock-out time is calculated based on the remaining required work hours after lunch.

## License

NO LICENSE.
