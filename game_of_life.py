import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

def create_grid(size):
    return np.random.choice([0, 1], size * size, p=[0.85, 0.15]).reshape(size, size)

def update(frame):
    size = frame.shape[0]
    new_frame = frame.copy()
    for i in range(size):
        for j in range(size):
            total = int((frame[i, (j-1)%size] + frame[i, (j+1)%size] + 
                         frame[(i-1)%size, j] + frame[(i+1)%size, j] + 
                         frame[(i-1)%size, (j-1)%size] + frame[(i-1)%size, (j+1)%size] + 
                         frame[(i+1)%size, (j-1)%size] + frame[(i+1)%size, (j+1)%size]))
            if frame[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_frame[i, j] = 0
            else:
                if total == 3:
                    new_frame[i, j] = 1
    return new_frame

# Streamlit app
def main():
    st.title("Game of Life Simulation")

    # Add a slider for grid size
    size = st.slider("Grid Size", min_value=10, max_value=100, value=50, step=10)

    # Add a slider for simulation speed
    speed = st.slider("Simulation Speed (fps)", min_value=1, max_value=60, value=10)

    # Add a button to start/stop the simulation
    if 'running' not in st.session_state:
        st.session_state.running = False

    start_stop = st.button('Start/Stop Simulation')

    # Create initial grid
    if 'grid' not in st.session_state or st.session_state.grid.shape[0] != size:
        st.session_state.grid = create_grid(size)

    # Create a placeholder for the plot
    plot_placeholder = st.empty()

    # Toggle running state when button is pressed
    if start_stop:
        st.session_state.running = not st.session_state.running

    # Main simulation loop
    while st.session_state.running:
        # Update and display the grid
        st.session_state.grid = update(st.session_state.grid)
        
        fig, ax = plt.subplots()
        ax.imshow(st.session_state.grid, cmap='binary')
        ax.axis('off')
        plot_placeholder.pyplot(fig)
        plt.close(fig)

        # Add a delay to control the simulation speed
        time.sleep(1/speed)

        # Rerun the app to update the display
        st.experimental_rerun()

    # Display the grid when not running
    fig, ax = plt.subplots()
    ax.imshow(st.session_state.grid, cmap='binary')
    ax.axis('off')
    plot_placeholder.pyplot(fig)
    plt.close(fig)

if __name__ == "__main__":
    main()