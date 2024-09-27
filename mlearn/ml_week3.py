### START CODE HERE ###
#if (isinstance(z, (int, float))):
#    g = 1 / (1 + np.exp(-z))
#elif (isinstance(z, np.ndarray)):
#    g = []
#    for i in z:
#        g.append(1 / (1 + np.exp(-i)))
### END SOLUTION ###]

#Exercise 2
### START CODE HERE ###
#m, n = X.shape
#total_cost = 0
#z = 0
#loss_f = 0
#for i in range(m):
#    z = 0
#    for j in range(n):
#        z += w[j] * X[i][j]
#    z += b
#    g = 1 / (1 + np.exp(-z))
#    loss_f += (-y[i] * np.log(g)) - ((1 - y[i]) * np.log(1 - g))
#total_cost = loss_f / m
#print(total_cost)
### END CODE HERE ###

#Exercise 3
### START CODE HERE ###
#for i in range(m):
#    z_wb = 0
#    for j in range(n):
#        z_wb += w[j] * X[i][j]
#    z_wb += b
#    f_wb = 1 / (1 + np.exp(-z_wb))

#    dj_db_i = f_wb - y[i]
#    dj_db += dj_db_i

#    for j in range(n):
#        dj_dw_ij = (f_wb - y[i]) * X[i][j]
#        dj_dw[j] += dj_dw_ij

#dj_dw = dj_dw / m
#dj_db = dj_db / m
### END CODE HERE ###

#Exercise 3
### START CODE HERE ###
# Loop over each example
#for i in range(m):
#    z_wb = None
    # Loop over each feature
#    for j in range(n):
        # Add the corresponding term to z_wb
#        z_wb += None

    # Add bias term
#    z_wb += None

    # Calculate the prediction for this example
#    f_wb = None

    # Apply the threshold
#    p[i] = None
### END CODE HERE ###

#Exercise 4
### START CODE HERE ###
# Loop over each example
#for i in range(m):
#    z_wb = 0
    # Loop over each feature
#    for j in range(n):
        # Add the corresponding term to z_wb
#        z_wb += X[i, j] * w[j]

    # Add bias term
#    z_wb += b

    # Calculate the prediction for this example
#    f_wb = sigmoid(z_wb)

    # Apply the threshold
#    p[i] = f_wb >= 0.5

#Exercise 5
### START CODE HERE ###
#for j in range(n):
#    reg_cost_j = w[j] ** 2
#    reg_cost = reg_cost + reg_cost_j
#reg_cost = (lambda_ / (2 * m)) * reg_cost
### END CODE HERE ###

#Exercise 6