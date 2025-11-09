def approximate_pi(n_terms):

    pi_approx = 0
    for n in range(n_terms):
        term = (-1) ** n / (2 * n + 1)
        pi_approx += term
        current_pi = 4 * pi_approx
        print("Term", n+1, "Approximation:", current_pi)

    return 4 * pi_approx
