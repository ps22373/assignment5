# Module 5: Advanced Object-Oriented Programming (OOP), Design Patterns, and Data Management in Python

## Module Overview
Welcome to **Module 5**, where you will elevate your Python programming skills by delving deeper into **Object-Oriented Programming (OOP)**, exploring **design patterns**, and mastering **data management techniques** using libraries like `pandas` and handling `CSV` files. Building upon your foundational knowledge from previous modules, this module introduces more sophisticated OOP concepts, design patterns for scalable and maintainable code, and effective data handling strategies to manage and persist application state.

Your primary textbook for this module is the provided codebase, organized with the following folder structure:

```
app/
├── calculator.py
├── calculation.py
├── calculator_config.py
├── calculator_memento.py
├── exceptions.py
├── history.py
├── input_validators.py
├── operations.py
tests/
├── test_calculations.py
├── test_calculator.py
├── test_operations.py
└── test_history.py
```

Each `.py` file within the `app/` directory contains the relevant code for that module. The `tests/` directory includes unit and parameterized tests to verify the functionality of your application.

By studying and interacting with this code, you'll gain hands-on experience in implementing advanced OOP principles, applying design patterns such as Factory and Observer, managing application configuration, handling persistent data with `pandas` and `CSV` files, and ensuring code reliability through thorough testing.

## Why Advanced OOP, Design Patterns, and Data Management?
**Object-Oriented Programming (OOP)** is a cornerstone of modern software development, enabling developers to create modular, reusable, and scalable code. By leveraging advanced OOP concepts such as inheritance, encapsulation, and polymorphism, you can design more sophisticated applications that are easier to maintain and extend.

**Design Patterns** provide proven solutions to common software design problems, promoting best practices and enhancing code flexibility. Patterns like Factory, Observer, and Strategy facilitate the creation of scalable and maintainable systems.

**Data Management** is crucial for applications that require persistence, configuration management, and efficient data handling. Utilizing libraries like `pandas` for data manipulation and `CSV` files for storage ensures that your applications can manage and persist data effectively.

## Learning Outcomes
By the end of this module, you will be able to:

- **Apply Advanced OOP Principles:** Utilize inheritance, encapsulation, and polymorphism to create well-structured Python programs.
- **Implement Design Patterns:** Apply Factory, Observer, and Strategy design patterns to enhance code scalability and maintainability.
- **Manage Application Configuration:** Use environment variables and configuration classes to manage application settings effectively.
- **Handle Persistent Data:** Utilize `pandas` for data manipulation and manage data persistence using `CSV` files.
- **Develop Robust Command-Line Applications:** Enhance your REPL-based applications with maintainable and scalable code structures.
- **Conduct Thorough Testing:** Write extensive unit and parameterized tests using `pytest` to ensure all code paths are tested.
- **Achieve 100% Test Coverage:** Utilize coverage tools to measure and ensure complete test coverage of your application.
- **Optimize Test Coverage:** Learn how to handle specific lines of code that may require coverage exceptions (e.g., lines with `pass` or `continue`).

## Module 5 Learning Pathway

### Recall

**Title:** Reflecting on Your OOP, Design Patterns, and Data Management Experiences  
**Grading Type:** Points  
**Instructions:** 
- **Discussion Forum:** Share your experiences with Object-Oriented Programming, design patterns, and data management in Python.
  - Discuss any projects where you applied OOP principles and design patterns.
  - Reflect on the challenges you faced while handling data persistence and achieving test coverage.
- **Quiz:** Complete a short quiz to assess your current understanding of advanced OOP concepts, design patterns, and data management techniques.
- **Purpose:** This activity will help you recall and articulate your prior experiences, setting the stage for deeper learning in this module.

### Read

Your **primary textbook** for this module is the provided codebase. Each `.py` file within the `app/` directory is thoroughly commented to explain advanced OOP concepts, design patterns, error handling strategies, and data management techniques. Here’s an overview of the key components:

1. **`app/calculation.py`**
   - **Purpose:** Implements the `Calculation` class, a value object representing a single mathematical calculation.
   - **Key Concepts:**
     - **Data Classes:** Utilize Python's `@dataclass` for boilerplate-free class definitions. [Python Documentation on Data Classes](https://docs.python.org/3/library/dataclasses.html)
     - **Post-Initialization Processing:** Automatically compute results after object creation.
     - **Serialization and Deserialization:** Convert objects to and from dictionaries for storage.
     - **Exception Handling:** Raise custom exceptions for invalid operations.
     - **Design Patterns:** Implements aspects of the **Memento** pattern for state management.

2. **`app/calculator_config.py`**
   - **Purpose:** Defines the `CalculatorConfig` class for managing configuration settings.
   - **Key Concepts:**
     - **Configuration Management:** Load and validate configuration from environment variables and defaults.
     - **Properties:** Use `@property` decorators to define dynamic attributes. [Python Documentation on Properties](https://docs.python.org/3/library/functions.html#property)
     - **Error Handling:** Raise custom exceptions for invalid configurations.
     - **Design Patterns:** Implements aspects of the **Singleton** pattern by ensuring a single configuration instance.

3. **`app/calculator_memento.py`**
   - **Purpose:** Implements the `CalculatorMemento` class to store calculator state for undo/redo functionality.
   - **Key Concepts:**
     - **Memento Design Pattern:** Capture and restore the state of an object without exposing its internal structure. [Memento Pattern Explanation](https://refactoring.guru/design-patterns/memento)
     - **Serialization and Deserialization:** Convert mementos to and from dictionaries for persistence.

4. **`app/exceptions.py`**
   - **Purpose:** Defines a hierarchy of custom exception classes for the calculator application.
   - **Key Concepts:**
     - **Custom Exceptions:** Create specific exception types for different error scenarios.
     - **Inheritance:** Utilize inheritance to create a base exception class for the application.

5. **`app/history.py`**
   - **Purpose:** Implements the Observer pattern to manage history observers.
   - **Key Concepts:**
     - **Observer Design Pattern:** Allow objects to subscribe and receive updates about state changes. [Observer Pattern in Python](https://refactoring.guru/design-patterns/observer/python/example)
     - **Abstract Base Classes:** Define interfaces for observers.
     - **Concrete Observers:** Implement observers that perform actions like logging and auto-saving.

6. **`app/input_validators.py`**
   - **Purpose:** Provides input validation mechanisms for the calculator.
   - **Key Concepts:**
     - **Input Validation:** Ensure user inputs meet required formats and constraints.
     - **Exception Handling:** Raise custom validation errors for invalid inputs.

7. **`app/operations.py`**
   - **Purpose:** Contains abstract and concrete classes for arithmetic operations, implementing the Strategy and Factory patterns.
   - **Key Concepts:**
     - **Strategy Design Pattern:** Define a family of algorithms, encapsulate each one, and make them interchangeable. [Strategy Pattern in Python](https://realpython.com/strategy-pattern-python/)
     - **Factory Design Pattern:** Create objects without specifying the exact class of the object to be created. [Factory Method Pattern in Python](https://realpython.com/factory-method-python/)
     - **Inheritance and Polymorphism:** Use abstract base classes and method overriding to implement different operations.
     - **Operation Registration:** Allow dynamic addition of new operations via the Factory.

8. **`app/calculator.py`**
   - **Purpose:** Implements the main `Calculator` class that integrates all components, manages operations, history, observers, and configuration.
   - **Key Concepts:**
     - **Integration of Design Patterns:** Combines Strategy, Observer, and Memento patterns.
     - **Data Persistence with pandas and CSV:** Use `pandas` to manage calculation history and persist it to `CSV` files. [pandas Documentation](https://pandas.pydata.org/docs/)
     - **Logging:** Implement logging for application events and errors. [Python Logging Documentation](https://docs.python.org/3/library/logging.html)

9. **`tests/test_calculations.py`**
   - **Purpose:** Provides unit tests for the `Calculation` class and related functionalities.
   - **Key Concepts:**
     - **Parameterized Testing:** Use `pytest` to run tests with multiple input scenarios.
     - **Exception Testing:** Ensure that invalid operations raise appropriate exceptions.

10. **`tests/test_calculator.py`**
    - **Purpose:** Contains unit tests for the `Calculator` class, including REPL interactions.
    - **Key Concepts:**
      - **Simulating User Input:** Use `monkeypatch` to simulate user interactions within the REPL.
      - **Capturing Output:** Verify that the correct outputs are displayed based on user inputs.
      - **Negative Testing:** Ensure that the application gracefully handles invalid inputs and unexpected errors.

11. **`tests/test_operations.py`**
    - **Purpose:** Includes unit and negative tests for the `Operation` classes.
    - **Key Concepts:**
      - **Edge Case Testing:** Test arithmetic methods with various input scenarios, including zero and negative numbers.
      - **Type Validation:** Ensure that methods handle invalid input types appropriately by raising exceptions.

12. **`tests/test_history.py`**
    - **Purpose:** Provides tests for the history management and observer functionalities.
    - **Key Concepts:**
      - **Observer Pattern Testing:** Ensure that observers are correctly notified and respond to new calculations.
      - **Memento Pattern Testing:** Verify that undo and redo operations correctly restore previous states.

**Supplementary Articles:**
To enhance your understanding of the codebase, please refer to the following Python documentation and resources:

1. **[Python Data Classes](https://docs.python.org/3/library/dataclasses.html)**
   - **Purpose:** Understand how to use data classes to simplify class definitions and manage data attributes efficiently.

2. **[Python Properties](https://docs.python.org/3/library/functions.html#property)**
   - **Purpose:** Learn how to use `@property` decorators to create managed attributes in your classes.

3. **[Python Abstract Base Classes (ABC)](https://docs.python.org/3/library/abc.html)**
   - **Purpose:** Explore how to define abstract base classes to create interfaces for your classes.

4. **[Python Logging Module](https://docs.python.org/3/library/logging.html)**
   - **Purpose:** Implement logging in your applications to track events, errors, and debug information.

5. **[pandas Documentation](https://pandas.pydata.org/docs/)**
   - **Purpose:** Master data manipulation and analysis using the pandas library.

6. **[Handling CSV Files in Python](https://docs.python.org/3/library/csv.html)**
   - **Purpose:** Learn how to read from and write to CSV files using Python's built-in `csv` module.

7. **[Strategy Design Pattern in Python](https://realpython.com/strategy-pattern-python/)**
   - **Purpose:** Understand and implement the Strategy design pattern to define a family of algorithms.

8. **[Factory Design Pattern in Python](https://realpython.com/factory-method-python/)**
   - **Purpose:** Learn how to implement the Factory design pattern to manage object creation.

9. **[Observer Design Pattern in Python](https://realpython.com/observer-pattern-python/)**
   - **Purpose:** Implement the Observer design pattern to allow objects to subscribe and react to events.

10. **[Singleton Design Pattern in Python](https://realpython.com/python-singleton/)**
    - **Purpose:** Learn how to implement the Singleton pattern to ensure a class has only one instance.

11. **[Achieving 100% Test Coverage in Python](https://docs.pytest.org/en/7.2.x/coverage.html)**
    - **Purpose:** Use coverage tools with pytest to measure and achieve full test coverage.

12. **[Understanding the Memento Design Pattern](https://refactoring.guru/design-patterns/memento)**
    - **Purpose:** Gain a deeper understanding of how the Memento pattern can be used to capture and restore an object's state.

### Watch

See Canvas Uploaded videos.

### Review

Utilize the following cheat sheets as quick references to aid your study and project development:

1. **[Advanced OOP Cheat Sheet](https://realpython.com/python-cheat-sheet/)**
   - **Purpose:** Offers a quick reference for advanced OOP concepts and syntax in Python.

2. **[Design Patterns Cheat Sheet](https://refactoring.guru/design-patterns)**
   - **Purpose:** Provides essential information on various design patterns, including Factory and Observer.

3. **[pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)**
   - **Purpose:** Quick reference for using `pandas` for data manipulation and analysis.

4. **[CSV Handling Cheat Sheet](https://realpython.com/python-csv/)**
   - **Purpose:** Comprehensive guide to reading from and writing to `CSV` files in Python.

5. **[Test Coverage Cheat Sheet](https://pytest-cov.readthedocs.io/en/latest/)**
   - **Purpose:** Quick reference for measuring and managing test coverage in Python projects.

6. **[Python Logging Cheat Sheet](https://realpython.com/python-logging/)**
   - **Purpose:** Quick reference for implementing and configuring logging in Python applications.

7. **[Strategy Design Pattern Cheat Sheet](https://refactoring.guru/design-patterns/strategy)**
   - **Purpose:** Provides a summary and examples of the Strategy design pattern.

8. **[Factory Design Pattern Cheat Sheet](https://refactoring.guru/design-patterns/factory-method)**
   - **Purpose:** Offers an overview and implementation details of the Factory design pattern.

9. **[Observer Design Pattern Cheat Sheet](https://refactoring.guru/design-patterns/observer)**
   - **Purpose:** Summarizes the Observer design pattern with examples and use cases.

### Submit

**Activity Type:** Advanced Hands-on Assignment  

**Activity Title:** Professional Calculator Command-Line Application with Design Patterns and Data Management  

**Grading Type:** Points  

**Submission Instructions:** Submit a link to your GitHub repository containing the project.

**Instructions:** 
- **Repository Setup:**
  - Initialize a new Git repository locally and create a corresponding repository on GitHub.
  - Set up a Python project in your preferred IDE with a well-structured directory layout, following the provided folder structure (`app/calculator.py`, `app/calculation.py`, `app/calculator_config.py`, `app/calculator_memento.py`, `app/exceptions.py`, `app/history.py`, `app/input_validators.py`, `app/operations.py`, and `tests/` directory).
  - Create and activate a virtual environment for your project.
  
- **Application Development:**
  - Develop a professional-grade calculator command-line application with the following features:
    - **REPL Interface:** Implement a Read-Eval-Print Loop for continuous user interaction.
    - **Arithmetic Operations:** Allow users to perform addition, subtraction, multiplication, division, power, and root operations.
    - **Design Patterns:**
      - **Factory Pattern:** Use the `OperationFactory` to create operation instances based on user input.
      - **Observer Pattern:** Implement observers like `LoggingObserver` and `AutoSaveObserver` to monitor and react to new calculations.
      - **Memento Pattern:** Enable undo and redo functionality by storing and restoring calculator state using `CalculatorMemento`.
    - **Configuration Management:** Utilize the `CalculatorConfig` class to manage application settings, loading from environment variables and providing defaults.
    - **Data Persistence:**
      - **History Management:** Use `pandas` to manage calculation history and persist it to `CSV` files.
      - **Serialization:** Implement serialization and deserialization methods for `Calculation` and `CalculatorMemento` classes.
    - **User Prompts:**
      - Prompt for the desired operation and the numbers to operate on.
      - Provide clear instructions and feedback to the user.
      - Implement special commands (`help`, `history`, `clear`, `undo`, `redo`, `save`, `load`, `exit`) to enhance user experience.
    - **Input Validation:** Validate user inputs to ensure they follow the expected format and handle invalid inputs gracefully using the `InputValidator` class.
    - **Error Handling:** 
      - Implement comprehensive error handling to manage invalid inputs and exceptional scenarios (e.g., division by zero).
      - Demonstrate both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission) paradigms within your error handling strategies.
    - **Calculation Management:** 
      - Create and manage `Calculation` instances for each operation.
      - Maintain a history of calculations performed during the session.
      - Ensure the history does not exceed the maximum size defined in the configuration.
  
- **Best Practices:**
  - **DRY Principle:** Apply the DRY (Don't Repeat Yourself) principle and other best practices to ensure your code is maintainable and efficient.
  - **Modular Design:** Organize your code into modules and classes to enhance readability and reusability.
  - **Logging:** Implement logging to track application events and errors using the `LoggingObserver`.
  
- **Testing:**
  - **Unit Tests:** 
    - Write comprehensive unit tests using `pytest` to verify the functionality of individual components (e.g., arithmetic operations, calculation classes, configuration management).
    - Ensure that each method and function behaves as expected under various scenarios.
  - **Parameterized Tests:** 
    - Implement parameterized tests in `tests/test_calculations.py`, `tests/test_operations.py`, and `tests/test_history.py` to cover multiple input scenarios efficiently.
    - Achieve extensive test coverage by testing both positive and negative cases.
  - **Test Coverage:** 
    - Use coverage tools (e.g., `pytest-cov`) to measure your test coverage.
    - **Achieve 100% test coverage**, ensuring that all lines of code, branches, and edge cases are tested.
    - **Handling Coverage Exceptions:** 
      - Some lines of code, such as those containing `pass` or `continue`, may not be covered by tests. Research how to use coverage comments (e.g., `# pragma: no cover`) to intentionally ignore these lines without affecting overall coverage metrics.
  
- **Documentation:**
  - Create detailed documentation, including a `README.md` file with setup and usage instructions.
  - Document your code with meaningful comments and docstrings to enhance readability and maintainability.
  
- **Version Control & CI:**
  - **Push Code to GitHub:**
    - Ensure your code follows best practices for code organization and documentation.
    - Commit changes with clear and descriptive messages.
  - **Configure GitHub Actions:**
    - Set up GitHub Actions to automatically run your tests and measure test coverage on each push to the repository.
    - **Enforce 100% Test Coverage:** 
      - Configure your CI pipeline to check for 100% test coverage. If the coverage is below 100%, the build should fail, prompting you to add the necessary tests.
      - Example GitHub Actions workflow file (`.github/workflows/python-app.yml`):
        ```yaml
        name: Python application

        on:
          push:
            branches: [ main ]
          pull_request:
            branches: [ main ]

        jobs:
          build:

            runs-on: ubuntu-latest

            steps:
            - uses: actions/checkout@v2
            - name: Set up Python 3.x
              uses: actions/setup-python@v2
              with:
                python-version: '3.x'
            - name: Install dependencies
              run: |
                python -m pip install --upgrade pip
                pip install pytest pytest-cov pandas python-dotenv
            - name: Run tests with coverage
              run: |
                pytest --cov=app tests/
            - name: Check coverage
              run: |
                coverage report --fail-under=100
        ```
      - **Handling Coverage Exceptions:** 
        - In your code, add comments like `# pragma: no cover` to lines that are intentionally excluded from coverage metrics (e.g., lines with `pass` or `continue`). This ensures that your coverage report accurately reflects the test coverage without being penalized for these lines.
        - Example:
          ```python
          if some_condition:
              pass  # pragma: no cover
          ```

**Grading Expectations:** 
- **Functionality:** Completeness and accuracy of the calculator command-line application, including all specified features and design patterns.
- **Design Patterns Implementation:** Correct application of Factory, Observer, and Memento design patterns.
- **Data Management:** Effective use of `pandas` for data manipulation and `CSV` files for data persistence.
- **User Interface:** Proper implementation of the REPL pattern and a user-friendly interface that handles user inputs gracefully.
- **Code Quality:** Efficient use of Python control structures, adherence to the DRY principle, and professional coding practices.
- **Error Handling:** Comprehensive error handling mechanisms that manage invalid inputs and exceptional scenarios effectively.
- **Testing:** 
  - Thorough unit and parameterized testing using `pytest`.
  - Achieving **100% test coverage**, ensuring all code paths are tested.
- **Documentation:** Well-structured code with comprehensive documentation, including a clear and informative `README.md`.
- **Automation:** Successful setup of GitHub Actions to automatically run your tests and enforce 100% test coverage, ensuring code quality on every commit.

**Alignment:** 
- Implement advanced Python control structures and OOP principles effectively in a command-line application.
- Apply design patterns such as Factory, Observer, and Memento to enhance code scalability and maintainability.
- Manage application configuration and data persistence using `pandas` and `CSV` files.
- Apply the DRY principle and other best practices for writing maintainable and efficient Python code.
- Develop a command-line application using the REPL pattern with robust error handling.
- Implement comprehensive unit and parameterized tests for Python applications using `pytest`.
- Achieve and enforce **100% test coverage** through Continuous Integration with GitHub Actions, including handling coverage exceptions where necessary.

### Reflect

**Title:** Module 5 In-Depth Reflection  
**Grading Type:** Points  
**Instructions:**
- **Reflection Essay:** Compose a comprehensive reflection (300-400 words) on your experience developing the professional calculator command-line application.
  - **Application of Concepts:** Analyze how the advanced OOP principles, design patterns, and data management techniques learned in this module can be applied to real-world programming scenarios.
  - **Challenges and Solutions:** Discuss any challenges you encountered during the project, particularly in implementing design patterns, managing data persistence, or achieving full test coverage, and the strategies you used to overcome them.
  - **Self-Evaluation:** Evaluate your current level of confidence in using advanced OOP, design patterns, and data management tools. Identify areas where you feel proficient and areas where you need further practice or support.
- **Purpose:** This activity aims to encourage deep metacognition and help you connect new knowledge with prior experiences and future applications.

### Quiz

**Title:** Advanced Python Programming, Design Patterns, and Data Management Quiz  
**Grading Type:** Points  
**Instructions:**
- **Comprehensive Assessment:** Complete a comprehensive quiz covering the advanced OOP concepts, design patterns, data management techniques, and testing methodologies introduced in this module.
  - **Question Types:** The quiz will include multiple-choice, short answer, and code analysis questions to thoroughly evaluate your comprehension and application of the module's content.
- **Preparation:** 
  - Review all provided materials, including the codebase, supplementary articles, instructional videos, and cheat sheets.
  - Ensure you understand how to implement and test advanced OOP concepts and design patterns.
  - Familiarize yourself with using `pandas` for data management and handling coverage exceptions in `pytest`.