import pytest
from app.exceptions import CalculatorError, ValidationError, OperationError, ConfigurationError

# Test cases for CalculatorError hierarchy

def test_calculator_error_is_base_exception():
    with pytest.raises(CalculatorError) as exc_info:
        raise CalculatorError("Base calculator error occurred")
    assert str(exc_info.value) == "Base calculator error occurred"

def test_validation_error_is_calculator_error():
    with pytest.raises(CalculatorError) as exc_info:
        raise ValidationError("Validation failed")
    assert isinstance(exc_info.value, CalculatorError)
    assert str(exc_info.value) == "Validation failed"

def test_validation_error_specific_exception():
    with pytest.raises(ValidationError) as exc_info:
        raise ValidationError("Validation error")
    assert str(exc_info.value) == "Validation error"

def test_operation_error_is_calculator_error():
    with pytest.raises(CalculatorError) as exc_info:
        raise OperationError("Operation failed")
    assert isinstance(exc_info.value, CalculatorError)
    assert str(exc_info.value) == "Operation failed"

def test_operation_error_specific_exception():
    with pytest.raises(OperationError) as exc_info:
        raise OperationError("Specific operation error")
    assert str(exc_info.value) == "Specific operation error"

def test_configuration_error_is_calculator_error():
    with pytest.raises(CalculatorError) as exc_info:
        raise ConfigurationError("Configuration invalid")
    assert isinstance(exc_info.value, CalculatorError)
    assert str(exc_info.value) == "Configuration invalid"

def test_configuration_error_specific_exception():
    with pytest.raises(ConfigurationError) as exc_info:
        raise ConfigurationError("Specific configuration error")
    assert str(exc_info.value) == "Specific configuration error"
