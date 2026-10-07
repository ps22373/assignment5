# Module 5: Advanced Design Patterns and Data Management with pandas in Python

## Module Overview
Welcome to **Module 5**, where you will elevate your Python programming expertise by exploring **Advanced Design Patterns** and mastering **Data Management** using the `pandas` library. Building upon the foundational Object-Oriented Programming (OOP) and testing techniques from previous modules, this module introduces sophisticated design patterns and emphasizes efficient data handling to create scalable and maintainable applications.

Your primary textbook for this module is the provided codebase, organized with the following flat folder structure:

```
app/
├── calculator_repl.py
├── calculation.py
├── calculator_config.py
├── calculator_memento.py
├── exceptions.py
├── history.py
├── input_validators.py
├── operations.py
tests/
├── test_calculations.py
├── test_calculator_repl.py
├── test_calculator_config.py
├── test_calculator_memento.py
├── test_exceptions.py
├── test_history.py
├── test_input_validators.py
├── test_operations.py
```

All Python modules are placed directly within the `app/` directory, promoting a flat and straightforward project structure. The `tests/` directory contains comprehensive unit and parameterized tests to verify the functionality and reliability of your application, ensuring robust and dependable performance.

By studying and interacting with this code, you'll gain hands-on experience in implementing advanced design patterns, integrating the `pandas` library for data management, applying the DRY (Don't Repeat Yourself) principle, handling errors gracefully, and ensuring code reliability through thorough testing.

## Why Advanced Design Patterns and pandas?
**Advanced Design Patterns** are proven solutions to common software design problems, enabling developers to create more flexible, scalable, and maintainable codebases. By leveraging patterns such as **Factory**, **Observer**, **Memento**, **Strategy**, and **Facade**, you can design applications that are easier to extend and modify over time.

**pandas** is a powerful data manipulation and analysis library in Python, widely used for handling structured data. Integrating `pandas` into your applications allows for efficient data processing, storage, and retrieval, enhancing the functionality and performance of your software solutions.

Combining advanced design patterns with `pandas` empowers you to build sophisticated applications that are not only well-architected but also capable of handling complex data operations seamlessly.

## Learning Outcomes
By the end of this module, you will be able to:
- CLO 6: Implement object-oriented programming principles in Python.
- CLO 7: Apply professional terminology and concepts related to web systems development.
- CLO 8: Create and manipulate CSV files using Python.

## Module 5 Learning Pathway

### Recall

**Title:** Reflecting on Your Design Patterns and Data Management Experiences  
**Grading Type:** Points  
**Instructions:** 
- **Discussion Forum:** Share your experiences with implementing design patterns and managing data in Python.
  - Discuss any projects where you applied design patterns.
  - Reflect on the challenges you faced while integrating `pandas` and how you overcame them.
- **Quiz:** Complete a short quiz to assess your current understanding of advanced design patterns and data management with `pandas`.
- **Purpose:** This activity will help you recall and articulate your prior experiences, setting the stage for deeper learning in this module.

### Read

Your **primary textbook** for this module is the provided codebase. Each Python file within the `app/` directory is thoroughly commented to explain advanced design patterns, data management strategies using `pandas`, and testing best practices. Here’s an overview of the key components:

1. **`app/calculator_repl.py`**
   - **Purpose:** Implements the command-line interface (REPL) for the calculator application.
   - **Key Concepts:** 
     - Advanced control structures (`try-except` blocks, loops)
     - User input handling and command parsing
     - Integration with design patterns (Observer, Memento, Strategy, Facade)
     - Interaction with `pandas` for data management

2. **`app/calculation.py`**
   - **Purpose:** Defines the `Calculation` class, representing individual calculations.
   - **Key Concepts:**
     - Data modeling with `dataclasses`
     - Exception handling and error reporting
     - Serialization and deserialization of calculation data
     - Usage of `pandas` for data storage and manipulation

3. **`app/calculator_config.py`**
   - **Purpose:** Manages configuration settings for the calculator application.
   - **Key Concepts:**
     - Environment variable management with `dotenv`
     - Configuration validation and error handling
     - Dynamic directory and file path management

4. **`app/calculator_memento.py`**
   - **Purpose:** Implements the Memento design pattern to support undo/redo functionality.
   - **Key Concepts:**
     - Memento pattern implementation
     - State preservation and restoration
     - Integration with `pandas` for historical data management

5. **`app/exceptions.py`**
   - **Purpose:** Defines a hierarchy of custom exception classes for the calculator application.
   - **Key Concepts:**
     - Custom exception creation
     - Hierarchical exception handling
     - Enhanced error reporting

6. **`app/history.py`**
   - **Purpose:** Implements the Observer design pattern to monitor and manage calculation history.
   - **Key Concepts:**
     - Observer pattern implementation
     - Logging and automatic saving of history
     - Integration with `pandas` for data persistence

7. **`app/input_validators.py`**
   - **Purpose:** Validates and sanitizes user inputs.
   - **Key Concepts:**
     - Input validation techniques
     - Error handling for invalid inputs
     - Integration with configuration settings

8. **`app/operations.py`**
   - **Purpose:** Defines operation classes and the Factory design pattern for creating operations.
   - **Key Concepts:**
     - Abstract Base Classes (ABCs) for operations
     - Factory pattern implementation for operation instantiation
     - Strategy pattern for interchangeable operation execution
     - Extension of operations with new functionality


### Watch

Engage with the following instructional videos to reinforce the concepts covered in the codebase and readings:

ADD VIDEO

### Review

Utilize the following cheat sheets as quick references to aid your study and project development:
To enhance your understanding of the codebase, please read the following articles:
1. **[Design Patterns in Python](https://refactoring.guru/design-patterns/python)**
2. **[Observer Pattern Explained](https://realpython.com/python-observer-pattern/)**
3. **[Memento Design Pattern in Python](https://refactoring.guru/design-patterns/memento/python/example)**
4. **[Strategy Pattern in Python](https://refactoring.guru/design-patterns/strategy/python/example)**
5. **[Facade Design Pattern in Python](https://refactoring.guru/design-patterns/facade/python/example)**
6. **[Mastering pandas for Data Analysis](https://realpython.com/pandas-python-explore-dataset/)**
7. **[Factory Design Pattern in Python](https://refactoring.guru/design-patterns/factory-method/python/example)**

8. **[Environment Variables and Configuration Management](https://realpython.com/python-dotenv/)**

### Submit

**Activity Type:** Advanced Hands-on Assignment  

**Activity Title:** Enhanced Calculator Application with Advanced Design Patterns and pandas  

**Grading Type:** Points  

**Submission Instructions:** Submit a link to your GitHub repository containing the project.

**Instructions:** 
- **Repository Setup:**
  - Initialize a new Git repository locally and create a corresponding repository on GitHub.
  - Set up a Python project in your preferred IDE with a well-structured directory layout, following the provided flat folder structure (`app/calculator_repl.py`, `app/calculation.py`, `app/calculator_config.py`, `app/calculator_memento.py`, `app/exceptions.py`, `app/history.py`, `app/input_validators.py`, `app/operations.py`, and `tests/` directory).
  - Create and activate a virtual environment for your project.
  
- **Application Development:**
  - Develop an enhanced calculator command-line application with the following features:
    - **REPL Interface:** Implement a Read-Eval-Print Loop for continuous user interaction.
    - **Advanced Arithmetic Operations:** Allow users to perform addition, subtraction, multiplication, division, power, and root operations.
    - **Design Patterns Integration:**
      - **Observer Pattern:** Implement observers to monitor and react to calculation events (e.g., logging, auto-saving history).
      - **Memento Pattern:** Enable undo and redo functionality by preserving and restoring the application's state.
      - **Strategy Pattern:** Implement interchangeable operation execution strategies using the Strategy pattern.
      - **Factory Pattern:** Use a factory to instantiate operation classes based on user input.
      - **Facade Pattern:** Provide a simplified interface to complex subsystems within the `Calculator` class.
    - **Data Management with pandas:**
      - **History Management:** Utilize `pandas` DataFrames to store, manipulate, and persist calculation history.
      - **Auto-Saving and Loading:** Automatically save calculation history to CSV files and load existing history upon application start.
    - **Configuration Management:** 
      - Implement a configuration system using environment variables and the `dotenv` library to manage application settings.
      - Validate configuration settings and handle configuration errors gracefully.
    - **User Commands:**
      - Implement commands such as `help`, `history`, `exit`, `clear`, `undo`, `redo`, `save`, and `load` to enhance user experience.
    - **Error Handling:** 
      - Implement comprehensive error handling to manage invalid inputs and exceptional scenarios (e.g., division by zero, invalid operations).
      - Demonstrate both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission) paradigms within your error handling strategies.
  
- **Best Practices:**
  - **DRY Principle:** Apply the DRY (Don't Repeat Yourself) principle and other best practices to ensure your code is maintainable and efficient.
  - **Modular Design:** Organize your code into modules and classes to enhance readability and reusability.
  - **Documentation:** 
    - Create a detailed `README.md` file with setup and usage instructions.
    - Document your code with meaningful comments and docstrings to enhance readability and maintainability.
  
- **Testing:**
  - **Unit Tests:** 
    - Write comprehensive unit tests using `pytest` to verify the functionality of individual components (e.g., arithmetic operations, calculation classes, observers).
    - Ensure that each method and function behaves as expected under various scenarios.
  - **Parameterized Tests:** 
    - Implement parameterized tests in `tests/test_calculations.py`, `tests/test_calculator_repl.py`, `tests/test_calculator_config.py`, `tests/test_calculator_memento.py`, `tests/test_exceptions.py`, `tests/test_history.py`, `tests/test_input_validators.py`, and `tests/test_operations.py` to cover multiple input scenarios efficiently.
    - Achieve extensive test coverage by testing both positive and negative cases.
  - **Test Coverage:** 
    - Use coverage tools (e.g., `pytest-cov`) to measure your test coverage.
    - **Achieve 100% test coverage**, ensuring that all lines of code, branches, and edge cases are tested.
    - **Handling Coverage Exceptions:** 
      - Some lines of code, such as those containing `pass` or `continue`, may not be covered by tests. Research how to use coverage comments (e.g., `# pragma: no cover`) to intentionally ignore these lines without affecting overall coverage metrics.
      - Example:
        ```python
        if some_condition:
            pass  # pragma: no cover
        ```
  
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
- **Functionality:** Completeness and accuracy of the enhanced calculator command-line application, including all specified features.
- **User Interface:** Proper implementation of the REPL pattern and a user-friendly interface that handles user inputs gracefully.
- **Code Quality:** Efficient use of Python control structures, adherence to the DRY principle, and professional coding practices.
- **Design Patterns Implementation:** Correct and effective use of advanced design patterns (Factory, Observer, Memento, Strategy, Facade) within the application.
- **Data Management with pandas:** Efficient integration of `pandas` for data handling, ensuring data integrity and performance.
- **Error Handling:** Comprehensive error handling mechanisms that manage invalid inputs and exceptional scenarios effectively.
- **Testing:** 
  - Thorough unit and parameterized testing using `pytest`.
  - Achieving **90+% test coverage**, ensuring all code paths are tested.
- **Documentation:** Well-structured code with comprehensive documentation, including a clear and informative `README.md`.
- **Automation:** Successful setup of GitHub Actions to automatically run your tests and enforce 100% test coverage, ensuring code quality on every commit.

**Alignment:** 
- Implement advanced design patterns and integrate `pandas` effectively in a command-line application.
- Apply the DRY principle and other best practices for writing maintainable and efficient Python code.
- Develop a command-line application using the REPL pattern with robust error handling.
- Implement comprehensive unit and parameterized tests for Python applications using `pytest`.
- Achieve and enforce **100% test coverage** through Continuous Integration with GitHub Actions, including handling coverage exceptions where necessary.

### Reflect

**Title:** Module 5 In-Depth Reflection  
**Grading Type:** Points  
**Instructions:**
- **Reflection Essay:** Compose a comprehensive reflection (300-400 words) on your experience developing the enhanced calculator command-line application.
  - **Application of Concepts:** Analyze how the advanced design patterns and data management techniques with `pandas` learned in this module can be applied to real-world programming scenarios.
  - **Challenges and Solutions:** Discuss any challenges you encountered during the project, particularly in implementing design patterns or integrating `pandas`, and the strategies you used to overcome them.
  - **Self-Evaluation:** Evaluate your current level of confidence in using advanced design patterns and `pandas`. Identify areas where you feel proficient and areas where you need further practice or support.
- **Purpose:** This activity aims to encourage deep metacognition and help you connect new knowledge with prior experiences and future applications.

### Quiz

**Title:** Advanced Design Patterns and pandas Data Management Quiz  
**Grading Type:** Points  
**Instructions:**
- **Comprehensive Assessment:** Complete a comprehensive quiz covering the advanced design patterns, data management strategies with `pandas`, and testing methodologies introduced in this module.
  - **Topics Covered:** 
    - Advanced Design Patterns (Factory, Observer, Memento, Strategy, Facade)
    - Data Management with pandas (DataFrames, CSV operations)
    - Error Handling Paradigms (LBYL vs EAFP)
    - Writing Unit and Parameterized Tests with `pytest`
    - Achieving and Enforcing Test Coverage
    - Handling Coverage Exceptions
  - **Question Types:** The quiz will include multiple-choice, short answer, and code analysis questions to thoroughly evaluate your comprehension and application of the module's content.
- **Preparation:** 
  - Review all provided materials, including the codebase, supplementary articles, instructional videos, and cheat sheets.
  - Ensure you understand how to implement and test advanced design patterns.
  - Familiarize yourself with using the `pandas` library for data management.
  - Practice writing and running tests with `pytest` to achieve high test coverage.

---

This updated module leverages the provided codebase as your primary textbook, allowing you to learn by doing. By engaging with the well-commented code, implementing advanced design patterns, integrating `pandas` for efficient data management, completing hands-on assignments with stringent testing requirements, and reflecting on your learning process, you will build a strong foundation in advanced software design and data handling in Python. Embrace the opportunity to write clean, efficient, and thoroughly tested code, ensuring high-quality applications through **100% test coverage** and optimized design and data management strategies.

If you have any further questions or need additional assistance with your module materials, feel free to ask!
