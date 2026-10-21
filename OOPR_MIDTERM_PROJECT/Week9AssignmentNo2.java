import java.util.Scanner;

public class Week9AssignmentNo2 {
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        char continueChoice;
        do {
            
            int number = 0;
            System.out.print("Enter a number from 1-10: ");
            number = scanner.nextInt();
            if (number == 1) {
                System.out.println("One");
            } else if (number == 2) {
                System.out.println("Two");
            } else if (number == 3) {
                System.out.println("Three");
            } else if (number == 4) {
                System.out.println("Four");
            } else if (number == 5) {
                System.out.println("Five");
            } else if (number == 6) {
                System.out.println("Six");
            } else if (number == 7) {
                System.out.println("Seven");
            } else if (number == 8) {
                System.out.println("Eight");
            } else if (number == 9) {
                System.out.println("Nine");
            } else if (number == 10) {
                System.out.println("Ten");
            } else {
                System.out.println("Invalid Number");
            }

            System.out.print("Again? y/n: ");
            continueChoice = scanner.next().toLowerCase().charAt(0);
 
        } while (continueChoice == 'y');
        
        System.out.println("Exiting.....");

        scanner.close();
    }
}
