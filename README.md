# Game of Life Simulation

This project implements a **Game of Life** simulation using **Streamlit** for real-time visualization and user interaction.

## Overview

The **Game of Life** is a cellular automaton devised by John Conway in 1970. Cells in a grid evolve over time according to the following rules:
- Any live cell with fewer than two live neighbors dies (underpopulation).
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies (overpopulation).
- Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Features

- **Grid Size Selection**: The user can choose the size of the grid (10x10 to 100x100).
- **Simulation Speed Control**: Adjust the frames per second (FPS) to control the speed of the simulation.
- **Start/Stop Functionality**: Allows the user to start or stop the simulation at any point.

## How to Run (with Docker)

### 1. Clone the Repository

First, clone the repository that contains the `Dockerfile` and application code:

```bash
git clone https://github.com/gggg444/game_of_life.git
```

### 2. Build the Docker Image

Navigate to the `app` directory and build the Docker image from the `Dockerfile`:

```bash
docker build -t game_of_life_app .
```

This will create a Docker image named `game_of_life_app`.

### 3. Run the Docker Container

Once the image is built, you can run the application using:

```bash
docker run -p 8501:8501 game_of_life_app
```

This command starts a container and maps port `8501` of the container to port `8501` on your local machine, allowing you to access the app in your browser at `http://localhost:8501`.

### 4. Health Check

The application includes a health check, accessible at:

```bash
http://localhost:8501/_stcore/health
```

## How to Run (without Docker)

You can also run the application without Docker by installing the necessary dependencies manually.

### 1. Install Dependencies

Make sure you have Python 3 installed, then install the required libraries:

```bash
pip install -r app/requirements.txt
```

### 2. Run the Application

Navigate to the `app` directory and run the Streamlit app:

```bash
streamlit run app/game_of_life.py
```

## License

This project is licensed under the MIT License.

## Acknowledgments

- **John Conway**: The inventor of the **Game of Life**, a famous cellular automaton.
- **Streamlit**: The framework used for the web interface.
- **Matplotlib**: The library used to render the grid visualization.



