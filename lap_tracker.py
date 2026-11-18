
# DSCM4L1 After Class Project: My Running Lap Tracker
#
# Run: python3 lap_tracker.py
# Or paste into one Google Colab cell and press Run.
#
# Complete TODO 1, TODO 2, and TODO 3 in order.
# Run the program after each TODO and check your results.
#
# Scoring:
# Lap 1 = 1 point, Lap 2 = 3 points, Lap 3 = 5 points...
# Each lap earns 2 more points than the previous lap.
#
# Find the total points after n laps in three different ways.


def total_formula(n):
    """Calculate the total using a mathematical formula."""
    # TODO 1: Use the formula n * n to calculate the total.
    # Return the total and 1 step.
    # Check: 5 laps = 25 points.
    return 0, 1


def total_loop(n):
    """Calculate the total using a single loop."""
    total, steps = 0, 0

    # TODO 2: Loop through each lap from 1 to n.
    # Add the lap's points (2 * lap - 1) to total.
    # Increase steps by 1 each time.
    # Check: 5 laps = 25 points, 5 steps.

    return total, steps


def total_point_by_point(n):
    """Calculate the total by counting every individual point."""
    total, steps = 0, 0

    # TODO 3: Use a nested loop.
    # Outer loop: visit each lap from 1 to n.
    # Inner loop: count each point earned on that lap.
    # Add 1 to total and steps for every point counted.
    # Check: 5 laps = 25 points, 25 steps.

    return total, steps


# Test all three methods for 5 and 50 laps.

for n in [5, 50]:
    print("Laps:", n)
    print("  Formula        total =", total_formula(n)[0],
          " steps =", total_formula(n)[1])
    print("  Loop           total =", total_loop(n)[0],
          " steps =", total_loop(n)[1])
    print("  Point by point total =", total_point_by_point(n)[0],
          " steps =", total_point_by_point(n)[1])
    print()

print("Formula: O(1) time")
print("Loop: O(n) time")
print("Point by point: O(n^2) time")
print("All three: O(1) extra space")
