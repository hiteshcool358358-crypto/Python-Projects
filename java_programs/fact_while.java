import java.util.*;
public class fact_while {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, i = 1, fact = 1;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        while (i <= n) {
            fact *= i;
            i++;
        }
        System.out.println("Factorial: " + fact);
        sc.close();
    }
}