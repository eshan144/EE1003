#include <stdio.h>

// Function to compute PMF
double pmf(int n) {
    if (n == 1) return 2.0 / 6.0;
    else if (n == 2) return 3.0 / 6.0;
    else if (n == 3) return 1.0 / 6.0;
    else return 0.0;
}

// Function to compute CDF
double cdf(int n) {
    double sum = 0.0;
    for (int i = 1; i <= n; i++) {
        sum += pmf(i);
    }
    return sum;
}

int main() {
    // Open a file to write PMF and CDF values
    FILE *file = fopen("data.txt", "w");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    // Write PMF values to the file
    fprintf(file, "PMF:\n");
    for (int i = 1; i <= 3; i++) {
        fprintf(file, "P(X = %d) = %.4f\n", i, pmf(i));
    }

    // Write CDF values to the file
    fprintf(file, "\nCDF:\n");
    for (int i = 0; i <= 3; i++) {
        fprintf(file, "P(X <= %d) = %.4f\n", i, cdf(i));
    }

    // Close the file
    fclose(file);

    printf("Data written to data.txt successfully.\n");
    return 0;
}

