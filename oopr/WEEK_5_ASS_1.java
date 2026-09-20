import java.io.BufferedReader;
import java.io.InputStreamReader;

public class WEEK_5_ASS_1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter first word: ");
        String word1 = br.readLine();

        System.out.print("Enter second word: ");
        String word2 = br.readLine();

        System.out.print("Enter third word: ");
        String word3 = br.readLine();

        System.out.println(word1 + " " + word2 + " " + word3);
    }
}
