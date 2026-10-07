########################
# Exception Hierarchy  #
########################

class CalculatorError(Exception):
    """
    Base exception class for calculator-specific errors.

    All custom exceptions for the calculator application inherit from this class,
    allowing for unified error handling.
    """
    pass


class ValidationError(CalculatorError):
    """
    Raised when input validation fails.

    This exception is triggered when user inputs do not meet the required criteria,
    such as entering non-numeric values or exceeding maximum allowed values.
    """
    pass


class OperationError(CalculatorError):
    """
    Raised when a calculation operation fails.

    This exception is used to indicate failures during the execution of arithmetic
    operations, such as division by zero or invalid operations.
    """
    pass


class ConfigurationError(CalculatorError):
    """
    Raised when calculator configuration is invalid.

    Triggered when there are issues with the calculator's configuration settings,
    such as invalid directory paths or improper configuration values.
    """
    pass
