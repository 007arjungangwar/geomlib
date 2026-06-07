"""Shared numeric constants and validation helpers."""

EPSILON = 1e-9


def is_close(a, b, *, rel_tol=EPSILON, abs_tol=EPSILON):
    """Return True when two floats are approximately equal."""
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def require_positive(value, name):
    """Validate that a numeric value is positive and return it as float."""
    value = float(value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def require_non_zero(value, name):
    """Validate that a numeric value is non-zero and return it as float."""
    value = float(value)
    if is_close(value, 0.0):
        raise ValueError(f"{name} must be non-zero")
    return value
