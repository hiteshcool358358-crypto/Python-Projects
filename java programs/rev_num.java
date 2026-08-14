import java.util.*;
public class rev_num {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, rev = 0;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        while (n > 0) {
            rev = (rev*10) + (n%10);
            n /= 10;
        }
        System.out.println("Reversed: " + rev);
        sc.close();
    }
}
