import java.util.*;
public class abundant {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a no.: ");
        int n = sc.nextInt(), s = 0;
        for (int i = 1; i < n; i++) {
            if (n % i == 0)
                s++;
            else
                continue;
        }
        if (s > 0) 
            System.out.println(n + " is an abundant no.");
        else
            System.out.println(n + " is not an abundant no.");
        sc.close();
    }
}