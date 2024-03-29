# BattlemapSearcher-Django

## Overview

BattlemapSearcher-Django is a single page application developed to facilitate the search for battlemaps seamlessly.

![BattlemapsSearcher](https://raw.githubusercontent.com/miki4920/BattlemapSearcher-Flask/main/BattlemapsSearcher.gif)

## Setup

### Prerequisites

- Python 3.10 or later
- Pipenv

### Environment Variables

The project requires the setting of the following environment variables for smooth operation:

- `IP`: Database IP (defaults to MySQL, although alterations can be made in the config)
- `USERNAME`: Database account username
- `PASSWORD`: Database account password
- `SCHEMA_NAME`: Name of the database schema

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/miki4920/BattlemapSearcher-Django.git
    ```

2. Transition into the project directory:
    ```bash
    cd BattlemapSearcher-Django
    ```

3. Install the necessary project dependencies utilizing pipenv:
    ```bash
    pipenv install
    ```

4. Establish the required environment variables.

## Usage

Post setup, the website is at your disposal to search for battlemaps. The web scraper will periodically scour Reddit for new maps in accordance with the specified subreddits. A heads-up, the API employed is pushshift.io, known for its occasional non-functionality.

## Contributing

Your contributions are heartily welcomed! Feel free to forward a pull request.

## License

This project is under the aegis of the MIT license terms.
