import java.util.Scanner;

public class HilvanoMidtermProj2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] originalArray = new int[8];

        // 1. Read 8 integer numbers from the user
        System.out.println("Please enter 8 integer numbers:");
        for (int i = 0; i < 8; i++) {
            System.out.print("Enter number " + (i + 1) + ": ");
            originalArray[i] = scanner.nextInt();
        }

        // 2. Remove duplicate elements from the array
        // Count how many unique numbers exist
        int uniqueCount = 0;
        for (int i = 0; i < 8; i++) {
            boolean isDuplicate = false;
            for (int j = 0; j < i; j++) {
                if (originalArray[i] == originalArray[j]) {
                    isDuplicate = true;
                    break;
                }
            }
            if (!isDuplicate) {
                uniqueCount++;
            }
        }

        // Create a new array with only unique elements
        int[] uniqueArray = new int[uniqueCount];
        int index = 0;
        for (int i = 0; i < 8; i++) {
            boolean isDuplicate = false;
            for (int j = 0; j < i; j++) {
                if (originalArray[i] == originalArray[j]) {
                    isDuplicate = true;
                    break;
                }
            }
            if (!isDuplicate) {
                uniqueArray[index++] = originalArray[i];
            }
        }

        // Display the array after removing duplicates
        System.out.print("\nArray after removing duplicates: ");
        for (int i = 0; i < uniqueArray.length; i++) {
            System.out.print(uniqueArray[i] + " ");
        }
        System.out.println();

        // Check if we have enough unique elements to find second largest/smallest
        if (uniqueArray.length < 2) {
            System.out.println("Error: Not enough unique elements to determine second largest or second smallest values.");
            scanner.close();
            return;
        }

        // 3. Find the second largest element
        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;

        for (int i = 0; i < uniqueArray.length; i++) {
            if (uniqueArray[i] > largest) {
                secondLargest = largest;
                largest = uniqueArray[i];
            } else if (uniqueArray[i] > secondLargest) {
                secondLargest = uniqueArray[i];
            }
        }

        // 4. Find the second smallest element
        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for (int i = 0; i < uniqueArray.length; i++) {
            if (uniqueArray[i] < smallest) {
                secondSmallest = smallest;
                smallest = uniqueArray[i];
            } else if (uniqueArray[i] < secondSmallest) {
                secondSmallest = uniqueArray[i];
            }
        }

        // Displaying results
        System.out.println("Second largest element: " + secondLargest);
        System.out.println("Second smallest element: " + secondSmallest);

        scanner.close();
    }
}
