import java.util.*;
public class pronic_num2 {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a no.: ");
        int n = sc.nextInt(); boolean pronic = false;
        for (int i = 1; i <= n; i++) {
            if (i * (i + 1) == n) {
                pronic = true;
                break;
            }
        }
        if (pronic)
            System.out.println(n + " is a pronic no.");
        else
            System.out.println(n + " is not a pronic no.");
        sc.close();
    }
}
