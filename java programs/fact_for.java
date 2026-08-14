import java.util.*;
public class fact_for {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, i, fact = 1;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        for (i = 1; i <= n; i++) {
            fact *= i;
        }
        System.out.println("Factorial: " + fact);
        sc.close();
    }
}
