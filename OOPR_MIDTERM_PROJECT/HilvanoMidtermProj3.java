import java.util.Scanner;

public class HilvanoMidtermProj3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] data = new int[5];

  
        System.out.print("Enter Data in Array: ");
        for (int i = 0; i < 5; i++) {
            data[i] = scanner.nextInt();
        }

        
        System.out.print("Stored Data in Array: ");
        for (int i = 0; i < 5; i++) {
            System.out.print(data[i] + " ");
        }
        System.out.println();

       
        System.out.print("Enter poss. of Element to Delete: ");
        int position = scanner.nextInt();

       
        for (int i = position; i < 4; i++) {
            data[i] = data[i + 1];
        }

       
        System.out.print("New data in Array: ");
        for (int i = 0; i < 4; i++) {
            System.out.print(data[i] + " ");
        }
        System.out.println();

        scanner.close();
    }
}

