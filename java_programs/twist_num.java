import java.util.*;
public class twist_num {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, rev = 0, c1 = 0, c2 = 0, copy;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        copy = n;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0)
                c1++;
        }
        if (c1 == 2) {
            while (n > 0) {
                rev = rev*10 + n%10;
                n /= 10;
            }
            for (int j = 1; j <= rev; j++) {
                if (rev % j == 0) 
                    c2++;
            }
            if (c2 == 2)
                System.out.println(copy + " is a twisted prime no.");
            else
                System.out.println(copy + " is not a twisted prime no.");
        }
        else
            System.out.println("Please enter a prime no.");
        sc.close();
    }
}