# NewsTok

## Overview

NewsTok is a web-based application developed using Flask, offering users a TikTok-like scrolling interface for discovering and reading articles and news. The application employs web scraping to gather articles from the internet, storing them in a database. As users scroll through the app, they are presented with article titles and AI-generated shortened content. Clicking on an article reveals its full content.

<div style="display:flex;justify-content:space-between;"><img src="gallery/preview1.png">
<img src="gallery/preview2.png"></div>

## Features

- **TikTok-like Interface:** Engage with news and articles in a visually dynamic and user-friendly manner.
- **Web Scraping:** Automatically fetch articles from the internet to keep content fresh.
- **AI Summarization:** Utilize artificial intelligence to provide concise summaries of article content.
- **Database Storage:** Efficiently store and manage a collection of articles for seamless retrieval.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ivanrj7j/NewsTok.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Access NewsTok in your web browser at [http://localhost:5000](http://localhost:5000).

## Usage

1. Scroll through the app to discover articles.
2. Click on an article to view its full content.
3. Stay informed with a unique and engaging news-reading experience.

## Source Code Structure


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


The source code is organized into two main parts:

- **web:** Contains the web application code.
  - `app.py`: Main application file.
  - `back.py`: Backend blueprint.
  - `front.py`: Frontend blueprint.
  - `__init__.py`: Initialization file.

- **core:** Manages core functionalities, independent of the web application.
  - `__init__.py`: Initialization file.
  - **models:**
    - `article.py`: A model for an article, contains essential details and methods related to an article
  - **workers:**
    - `businessinsider.py`: Worker for fetching articles from Business Insider.
    - `fetcher.py`: Generic article fetching functionality. Used as a parent class for other targetted fetchers
    - `scheduler.py`: Schedules tasks for fetching articles.
    - `searcher.py`: Parent class for searching any website for articles.
    - `businessinsiderSearcher.py`: Specialized searcher for [Business Insider](https://www.businessinsider.in/).

## [High Level Details](HLD.md)

[Click here to see HLD](HLD.md)

## License

NewsTok is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for more details.

## Contributions

Contributions are welcome! Please follow our [Contribution Guidelines](CONTRIBUTING.md) when submitting pull requests.

## Contact

For issues or suggestions, feel free to [open an issue](https://github.com/ivanrj7j/NewsTok/issues).

---
