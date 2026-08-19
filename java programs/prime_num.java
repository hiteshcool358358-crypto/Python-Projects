import java.util.*;
public class prime_num {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, c = 0, i;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        for (i = 1; i <= n; i++) {
            if (n % i == 0)
                c++;
        }
        if (c == 2)
            System.out.println(n + " is a prime no.");
        else
            System.out.println(n + " is not a prime no.");
        sc.close();
    }
}
