import numpy as np
from odespy import Vode

# Define the ODE function
def ode_function(t, y):
    y1, y2, y3, y4 = y  # Unpack the dependent variables
    return [y4, y3, y2, -y1 - 2*y2 - 3*y3 - y4]

# Create a Vode solver
solver = Vode(ode_function)

# Set the initial conditions and time interval
solver.set_initial_condition([0, 0, 0, 1])
t_points = np.linspace(0, 2, 11)

# Solve the ODE
u, t = solver.solve(t_points)

# Print the solution
print(u[:, 3])
