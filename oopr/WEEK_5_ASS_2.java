import java.util.Scanner;

public class WEEK_5_ASS_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int a = input.nextInt();

        System.out.print("Enter second number: ");
        int b = input.nextInt();

        System.out.print("Enter third number: ");
        int c = input.nextInt();

        int highest = a;

        if (b > highest)
            highest = b;

        if (c > highest)
            highest = c;

        System.out.println("The highest number is " + highest);

        input.close();
    }
}