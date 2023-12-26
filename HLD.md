# NewsTok - High-Level Details

## Overview

NewsTok is a Flask-based web application that offers users a TikTok-like scrolling interface for reading articles and news. The project structure is organized into two main components: **web** and **core**. The web component manages the frontend and backend, while the core component handles essential functionalities independently.

## Folder Structure

```plaintext
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
    |   |   |-- fetcher.py (File)
    |   |   |-- businessinsider.py (File)
    |   |   |-- scheduler.py (File)
    |   |   |-- searcher.py (File)
    |   |   |-- businessinsiderSearcher.py (File)
```

This structure reflects the organization of the NewsTok project, providing clarity on the location of key files and components within the codebase.

## Web Component

### `components.py`

- **Description:**
  - A file within the project, possibly handling shared components or utilities.
- **Role:**
  - Provides additional functionalities or shared utilities.

### `web/app.py`

- **Description:**
  - Main application file responsible for initializing and running the web application.
- **Role:**
  - Orchestrates the integration of frontend and backend components.

### `web/back.py`

- **Description:**
  - Backend blueprint defining core server-side functionalities.
- **Role:**
  - Manages backend operations, including article fetching and AI summarization.

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

### `core/workers/searcher.py`

- **Description:**
  - Parent class for searching any website for articles.
- **Role:**
  - Looks through a website and extracts articles using fetchers.
- **Note:**
  - Meant to be extended for specific websites.

### `core/workers/businessinsiderSearcher.py`

- **Description:**
  - Specialized searcher for [Business Insider](https://www.businessinsider.in/).
- **Role:**
  - Inherits from the `searcher.py` parent class.
  - Utilizes Business Insider-specific fetchers for article extraction.

## Miscellaneous

### `components.py`

- **Description:**
  - A file within the project, possibly handling shared components or utilities.
- **Role:**
  - Provides additional functionalities or shared utilities.

## Note

This updated overview outlines the roles and responsibilities of each component, considering the new files added to the project structure.