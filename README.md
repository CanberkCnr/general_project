## API Usage
**PORT** `1995`

### Endpoint
**POST** `/weather`

### Docker RUN
- docker build --tag general-project .
- docker run --detach general-project
----

### Swagger Docs
http://127.0.0.1:1995/docs


## Code Style and Linting

This project uses `flake8` for linting to enforce coding standards and ensure code quality. 

### `flake8` Configuration

`flake8` is configured to check for common Python style violations, such as:
- PEP 8 compliance (e.g., indentation, spacing, etc.)
- Naming conventions for variables and functions
- Import order

However, **E501 (line length)** is deliberately ignored to accommodate lines that exceed the typical 79-character limit defined by PEP 8. This exception is made to ensure the readability of longer lines, such as long import statements or complex function definitions, without unnecessary line breaks.
