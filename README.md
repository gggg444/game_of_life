# Game of Life Simulation

This project implements a **Game of Life** simulation using **Streamlit** for real-time visualization and user interaction.

## Overview

The **Game of Life** is a cellular automaton devised by the mathematician John Conway in 1970. It simulates a zero-player game where cells in a grid evolve over time based on a set of simple rules:
- A live cell with fewer than two live neighbors dies (underpopulation).
- A live cell with two or three live neighbors survives.
- A live cell with more than three live neighbors dies (overpopulation).
- A dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Features

- **Grid Size Selection**: The user can choose the size of the grid (10x10 to 100x100).
- **Simulation Speed Control**: Adjust the frames per second (FPS) to control the speed of the simulation.
- **Start/Stop Functionality**: Allows the user to start or stop the simulation at any point.

## Installation

To run the application, you'll need Python 3 and the following libraries:

- `streamlit`
- `numpy`
- `matplotlib`

You can install the required dependencies by running:

```bash
pip install streamlit numpy matplotlib
```
## How to Run

1. Clone the repository or download the project files.
2. Open a terminal in the project directory.
3. Run the Streamlit app with the following command:

    ```bash
    streamlit run app.py
    ```

    This will start the application in your web browser.

## Usage

- **Grid Size**: Use the slider to adjust the grid size from 10x10 to 100x100.
- **Simulation Speed**: Control the simulation speed (frames per second) using the corresponding slider.
- **Start/Stop Simulation**: Use the `Start/Stop Simulation` button to toggle the simulation on and off.

### Example Output

The simulation will display a grid of black and white cells:
- **Black cells** are "alive"
- **White cells** are "dead"

The grid evolves over time according to the rules of the **Game of Life**.

## Code Explanation

- **`create_grid(size)`**: Initializes a grid of given size with random live (`1`) and dead (`0`) cells, using a probability distribution (85% dead, 15% alive).
- **`update(frame)`**: Applies the rules of the Game of Life to compute the next generation of the grid.
- **`main()`**: The Streamlit application logic, which includes user interaction via sliders for grid size and simulation speed, and renders the evolving grid in real time.

## License

This project is licensed under the MIT License.

## Acknowledgments

- **John Conway**: The inventor of the **Game of Life**, a famous cellular automaton.
- **Streamlit**: The framework used for the web interface.
- **Matplotlib**: The library used to render the grid visualization.



