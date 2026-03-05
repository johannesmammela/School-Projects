import matplotlib.pyplot as plt
import numpy as np

# List to store points
points = []

def onclick(event):
    """Handle mouse clicks."""
    # Left mouse button adds a point
    if event.button == 1 and event.inaxes:
        points.append((event.xdata, event.ydata))
        plt.plot(event.xdata, event.ydata, 'bo')  # plot point in blue
        plt.draw()
    # Right mouse button stops collecting points
    elif event.button == 3:
        plt.close()

# Create plot and connect event handler
fig, ax = plt.subplots()
ax.set_title('Left click to add points, right click to finish')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

# Convert points to NumPy arrays
points = np.array(points)
if len(points) < 2:
    print("Not enough points to fit a line.")
else:
    x = points[:, 0]
    y = points[:, 1]

    # Fit linear model
    coeffs = np.polyfit(x, y, 1)
    slope, intercept = coeffs
    print(f"Fitted line: y = {slope:.2f}x + {intercept:.2f}")

    # Plot points and fitted line
    plt.scatter(x, y, color='blue', label='Points')
    x_line = np.linspace(min(x), max(x), 100)
    y_line = slope * x_line + intercept
    plt.plot(x_line, y_line, color='red', label='Fitted line')
    plt.title('Points and Linear Fit')
    plt.legend()
    plt.show()