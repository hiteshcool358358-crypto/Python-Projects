import java.util.*;
public class automorphic {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, copy1, c = 0, LastDigits = 0, rev = 0; double sqr;
        // instead of double sqr, int sqr can also be taken and instead of using Math.pow(), simply n*n can be used
        // declarations will be: int n, copy1, c = 0, LastDigits = 0, rev = 0, sqr;
        // and calculation of square of n will be: sqr = n*n; instead of sqr = Math.pow(n, 2);
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        sqr = Math.pow(n, 2);
        int sqr_int = (int) sqr; // not required read above
        copy1 = n;
        while (copy1 > 0) {
            c++;
            copy1/=10;
        }
        for (int i = 1; i <= c; i++) {
            LastDigits = LastDigits*10 + sqr_int%10;
            sqr_int/=10;
        }
        while (LastDigits > 0) {
            rev = rev*10 + LastDigits%10;
            LastDigits/=10;
        }
        if (rev == n)
            System.out.println(n + " is an automorphic no.");
        else
            System.out.println(n + " is not an automorphic no.");
        sc.close();
    }
}