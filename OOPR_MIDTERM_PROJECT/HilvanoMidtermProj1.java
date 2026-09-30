import java.util.Scanner;

public class HilvanoMidtermProj1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numbers = new double[10];

        // 1. Loop to read 10 real numbers from the user
        System.out.println("Please enter 10 real numbers (positive or negative):");
        for (int i = 0; i < 10; i++) {
            System.out.print("Enter number " + (i + 1) + ": ");
            numbers[i] = scanner.nextDouble();
        }

        // 2. Loop to find the sum and average of positive numbers (> 0)
        double positiveSum = 0;
        int positiveCount = 0;
        for (int i = 0; i < 10; i++) {
            if (numbers[i] > 0) {
                positiveSum += numbers[i];
                positiveCount++;
            }
        }

        // 3. Loop to count negative numbers (< 0)
        int negativeCount = 0;
        for (int i = 0; i < 10; i++) {
            if (numbers[i] < 0) {
                negativeCount++;
            }
        }

        // 4. Loop to find the minimum value in the array
        double minValue = numbers[0];
        for (int i = 1; i < 10; i++) {
            if (numbers[i] < minValue) {
                minValue = numbers[i];
            }
        }

        // Displaying results
        System.out.println("\n--- Results ---");
        if (positiveCount > 0) {
            double positiveAverage = positiveSum / positiveCount;
            System.out.println("Sum of positive numbers: " + positiveSum);
            System.out.println("Average of positive numbers: " + positiveAverage);
        } else {
            System.out.println("No positive numbers were entered.");
        }

        System.out.println("Count of negative numbers: " + negativeCount);
        System.out.println("Minimum value in the array: " + minValue);

        scanner.close();
    }
}
