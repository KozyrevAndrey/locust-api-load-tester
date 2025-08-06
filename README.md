# 🚀 Locust API Load Testing Framework

A comprehensive and flexible foundation for creating API load tests using Locust. This repository provides a well-structured template for performance testing REST APIs with realistic user scenarios and comprehensive monitoring.

## 🎯 Features

- **Multi-endpoint Testing**: Support for GET, POST, PUT, DELETE operations
- **Flexible Configuration**: Environment-based configuration management
- **Real-time Monitoring**: Built-in event logging and request tracking
- **Scalable Architecture**: Easy to extend with new test scenarios

## 📁 Project Structure

```
├── app/
│   ├── __init__.py
│   ├── config.py          # Configuration settings
│   └── locustfile.py      # Main test scenarios
├── tests/
│   └── __init__.py
├── pyproject.toml         # Poetry dependencies
├── poetry.lock
└── README.md
```

## 🛠️ Installation

### Requirements

- Python 3.12
- Poetry (recommended) or pip

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd locust-api-load-tester

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

## 🚀 Usage

```bash
poetry run locust -f app/locustfile.py
```

You can access the web interface at `http://0.0.0.0:8089`

## 🙏 Acknowledgments

[Locust](https://github.com/locustio/locust) - Modern load testing framework

[Poetry](https://python-poetry.org/) - Dependency management
