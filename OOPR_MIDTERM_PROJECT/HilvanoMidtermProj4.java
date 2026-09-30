import java.util.Scanner;

public class HilvanoMidtermProj4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. Enter Size of Array
        System.out.print("Enter Size of Array : ");
        int size = scanner.nextInt();

        int[] array = new int[size];

        // 2. Enter array elements
        System.out.println("Enter any " + size + " elements in Array:");
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextInt();
        }

        // 3. Find and display Even Elements (Divisible by 2)
        System.out.print("Even Elements: ");
        for (int i = 0; i < size; i++) {
            if (array[i] % 2 == 0) {
                System.out.print(array[i] + " ");
            }
        }
        System.out.println();

        // 4. Find and display Odd Elements (Not divisible by 2)
        System.out.print("Odd Elements: ");
        for (int i = 0; i < size; i++) {
            if (array[i] % 2 != 0) {
                System.out.print(array[i] + " ");
            }
        }
        System.out.println();

        scanner.close();
    }
}
