---
sessionId: session-260925-210809-8253
---

# Requirements

### Overview & Goals
The goal is to sort a list of activity dictionaries loaded from `activities.csv` by either date or duration (`estimated_minutes`) while maintaining each activity dictionary's integrity (keeping all fields together).

### Scope
- **In Scope:**
  - Sorting the list of dictionaries directly using a custom sorting key.
  - Converting numeric string fields to integers and date string fields to datetime objects for accurate comparison.
  - Allowing flexible sorting by either date or duration.
- **Out of Scope:**
  - Modifying the CSV schema or altering the underlying CSV file structure.
  - Modifying other unrelated helper functions in `oppgave_5_helpers.py`.

### Functional Requirements
- Retain all dictionary attributes (`title`, `category`, `date`, `estimated_minutes`, `status`) in each record after sorting.
- Sort durations numerically (e.g. 30 < 90 < 120).
- Sort dates chronologically based on parsed date values.

# Technical Design

### Current Implementation
In `oppgave_5_helpers.py`, `read_file` reads rows as a list of dictionaries with string values via `csv.DictReader`. Currently, `filter_date_or_duration` creates two separate lists with list comprehensions (`dates` and `durations`), sorting them independently and losing the association with other activity fields.

### Key Decisions
- **In-place vs New List:** Use `sorted()` with a `key` parameter to return a new sorted list of dictionaries without mutating the original list.
- **Key Extraction & Type Casting:**
  - For duration: cast `int(row["estimated_minutes"])` inside the key function.
  - For date: parse the date string using `datetime.strptime` to guarantee accurate chronological comparison regardless of date separator formats.

### Proposed Changes
- Update `filter_date_or_duration(activity_list, sort_by)` to sort full dictionaries based on the chosen attribute (`"date"` or `"estimated_minutes"`).
- Pass appropriate key transformations to Python's `sorted()` function.

### File Structure
- `oppgave_5_helpers.py`: Update `filter_date_or_duration` implementation.
- `oppgave_5_program.py`: Call and display sorted activity lists.

# Testing

### Validation Approach
Verify sorting functionality with representative dataset records containing multi-digit numbers and various dates.

### Key Scenarios
- **Numeric Duration Sorting:** Verify that activities with durations like 30, 90, and 120 minutes sort in numeric order (30, 90, 120) instead of alphabetical order (120, 30, 90).
- **Date Sorting:** Verify that activities with dates across different months and years sort in chronological sequence.
- **Dictionary Integrity:** Verify that each element in the resulting list retains all original keys and values.

# Delivery Steps

###   Step 1: Implement value transformation logic for sorting keys
Implement helper logic or key functions to extract and convert dictionary values for proper numeric and chronological sorting.

- Define integer conversion logic for `estimated_minutes` to ensure numeric comparison rather than lexicographical string comparison.
- Define datetime parsing logic using `datetime.strptime` to ensure accurate chronological date sorting.
- Handle potential malformed entries or formatting inconsistencies gracefully.

###   Step 2: Refactor filter_date_or_duration to sort dictionary list
Update the sorting function in `oppgave_5_helpers.py` so that full activity dictionaries are sorted and returned.

- Refactor `filter_date_or_duration` to accept criteria (such as sorting by date or duration, and optional sort order).
- Use `sorted()` with the appropriate `key` parameter to sort the list of dictionaries without breaking apart the dictionary records.
- Verify that calling `filter_date_or_duration` in `oppgave_5_program.py` prints the activities in the expected sorted order.