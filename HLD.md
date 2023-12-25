# NewsTok - High-Level Details

## Overview

NewsTok is a Flask-based web application that provides users with an interactive and engaging news-reading experience. The project architecture is divided into two main components: **web** and **core**. The web component manages the frontend and backend of the application, while the core component handles essential functionalities independently.

## Structure

    |-- components.py (File)

    |-- web
    |   |-- app.py (File)
    |   |-- back.py (File)
    |   |-- front.py (File)
    |   |-- __init__.py (File)
    |-- core
    |   |-- __init__.py (File)
    |   |-- models
    |   |   |-- article.py (File)
    |   |-- workers
    |   |   |-- businessinsider.py (File)
    |   |   |-- fetcher.py (File)
    |   |   |-- scheduler.py (File)

## Web Component

### `web/app.py`

- **Description:**
  - Main application file responsible for initializing and running the web application.
- **Role:**
  - Orchestrates the integration of frontend and backend components.

### `web/back.py`

- **Description:**
  - Backend blueprint defining core server-side functionalities.
- **Role:**
  - Manages backend operations.

### `web/front.py`

- **Description:**
  - Frontend blueprint managing the user interface and interactions.
- **Role:**
  - Handles user interactions and ensures a seamless scrolling experience.

### `web/__init__.py`

- **Description:**
  - Initialization file for the web component.
- **Role:**
  - Initializes and configures the web component.

## Core Component

### `core/__init__.py`

- **Description:**
  - Initialization file for the core component.
- **Role:**
  - Initializes and configures the core functionalities.

### `core/models/article.py`

- **Description:**
  - Logical model for an article, containing data and methods related to articles.
- **Role:**
  - Defines the structure and behavior of articles within the application.

### `core/workers/fetcher.py`

- **Description:**
  - Parent class for all fetchers.
- **Role:**
  - Provides a template for sending requests to a given URL and parsing the result.
- **Note:**
  - Does not implement a fetch method; meant to be extended by child classes.

### `core/workers/businessinsider.py`

- **Description:**
  - Specialized fetcher designed for [Business Insider](https://www.businessinsider.in/).
- **Role:**
  - Implements the fetch method for Business Insider articles.
- **Inheritance:**
  - Inherits from the `fetcher.py` parent class.

### `core/workers/scheduler.py`

- **Description:**
  - Used to schedule multiple fetchers for sending requests asynchronously.
- **Role:**
  - Enhances efficiency by managing the timing of article fetches.

## Miscellaneous

### `components.py`

- **Description:**
  - A file within the project, possibly handling shared components or utilities.
- **Role:**
  - Provides additional functionalities or shared utilities.

## Note

This detailed overview outlines the roles and responsibilities of each component, ensuring a clear understanding of the project's structure and functionality.