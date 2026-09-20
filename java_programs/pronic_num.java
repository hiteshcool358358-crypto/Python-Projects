import java.util.*;
public class pronic_num {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, i; boolean pronic = false;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        for (i = 1; i <= n; i++) {
            if ((i * (i + 1)) == n) {
                System.out.println(n + " is a pronic no.");
                pronic = true;
                break;
            }
            else
                continue;
        }
        if (pronic == false)
            System.out.println(n + " is not a pronic no.");
        sc.close();
    }
}