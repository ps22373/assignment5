########################
# Calculator Config    #
########################

from dataclasses import dataclass
from decimal import Decimal
from numbers import Number
from pathlib import Path
import os
from typing import Optional

from dotenv import load_dotenv

from app.exceptions import ConfigurationError

# Load environment variables from a .env file into the program's environment
load_dotenv()


def get_project_root() -> Path:
    """
    Get the project root directory.

    This function determines the root directory of the project by navigating up
    the directory hierarchy from the current file's location.

    Returns:
        Path: The root directory path of the project.
    """
    # Get the directory of the current file (app/calculator_config.py)
    current_file = Path(__file__)
    # Navigate up two levels to reach the project root (from app/calculator_config.py to project root)
    return current_file.parent.parent


@dataclass
class CalculatorConfig:
    """
    Calculator configuration settings.

    This class manages all configuration parameters required by the calculator
    application, including directory paths, history size, auto-save preferences,
    calculation precision, maximum input values, and default encoding.

    Configuration can be set via environment variables or by passing parameters
    directly to the class constructor.
    """

    def __init__(
        self,
        base_dir: Optional[Path] = None,
        max_history_size: Optional[int] = None,
        auto_save: Optional[bool] = None,
        precision: Optional[int] = None,
        max_input_value: Optional[Number] = None,
        default_encoding: Optional[str] = None
    ):
        """
        Initialize configuration with environment variables and defaults.

        Args:
            base_dir (Optional[Path], optional): Base directory for the calculator. Defaults to None.
            max_history_size (Optional[int], optional): Maximum number of history entries. Defaults to None.
            auto_save (Optional[bool], optional): Whether to auto-save history. Defaults to None.
            precision (Optional[int], optional): Number of decimal places for calculations. Defaults to None.
            max_input_value (Optional[Number], optional): Maximum allowed input value. Defaults to None.
            default_encoding (Optional[str], optional): Default encoding for file operations. Defaults to None.
        """
        # Set base directory to project root by default
        project_root = get_project_root()
        self.base_dir = base_dir or Path(
            os.getenv('CALCULATOR_BASE_DIR', str(project_root))
        ).resolve()

        # Maximum history size
        self.max_history_size = max_history_size or int(
            os.getenv('CALCULATOR_MAX_HISTORY_SIZE', '1000')
        )

        # Auto-save preference
        auto_save_env = os.getenv('CALCULATOR_AUTO_SAVE', 'true').lower()
        self.auto_save = auto_save if auto_save is not None else (
            auto_save_env == 'true' or auto_save_env == '1'
        )

        # Calculation precision
        self.precision = precision or int(
            os.getenv('CALCULATOR_PRECISION', '10')
        )

        # Maximum input value allowed
        self.max_input_value = max_input_value or Decimal(
            os.getenv('CALCULATOR_MAX_INPUT_VALUE', '1e999')
        )

        # Default encoding for file operations
        self.default_encoding = default_encoding or os.getenv(
            'CALCULATOR_DEFAULT_ENCODING', 'utf-8'
        )

    @property
    def log_dir(self) -> Path:
        """
        Get log directory path.

        Determines the directory path where log files will be stored.

        Returns:
            Path: The log directory path.
        """
        return Path(os.getenv(
            'CALCULATOR_LOG_DIR',
            str(self.base_dir / "logs")
        )).resolve()

    @property
    def history_dir(self) -> Path:
        """
        Get history directory path.

        Determines the directory path where calculation history files will be stored.

        Returns:
            Path: The history directory path.
        """
        return Path(os.getenv(
            'CALCULATOR_HISTORY_DIR',
            str(self.base_dir / "history")
        )).resolve()

    @property
    def history_file(self) -> Path:
        """
        Get history file path.

        Determines the file path for storing calculation history in CSV format.

        Returns:
            Path: The history file path.
        """
        return Path(os.getenv(
            'CALCULATOR_HISTORY_FILE',
            str(self.history_dir / "calculator_history.csv")
        )).resolve()

    @property
    def log_file(self) -> Path:
        """
        Get log file path.

        Determines the file path for storing log entries.

        Returns:
            Path: The log file path.
        """
        return Path(os.getenv(
            'CALCULATOR_LOG_FILE',
            str(self.log_dir / "calculator.log")
        )).resolve()

    def validate(self) -> None:
        """
        Validate configuration settings.

        Ensures that all configuration parameters meet the required criteria.
        Raises ConfigurationError if any validation fails.

        Raises:
            ConfigurationError: If any configuration parameter is invalid.
        """
        if self.max_history_size <= 0:
            raise ConfigurationError("max_history_size must be positive")
        if self.precision <= 0:
            raise ConfigurationError("precision must be positive")
        if self.max_input_value <= 0:
            raise ConfigurationError("max_input_value must be positive")
