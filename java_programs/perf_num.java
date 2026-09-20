import java.util.*;
public class perf_num {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, i, s = 0;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        for (i = 1; i < n; i ++) {
            if (n % i == 0)
                s += i;
        }
        if (s == n)
            System.out.println(n + " is a perfect no.");
        else
            System.out.println(n + " is not a pefect no.");
        sc.close();
    }
}
