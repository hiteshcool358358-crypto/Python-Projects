import java.util.*;
public class automorphic2 {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, copy, d = 0;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        copy = n;
        while (copy > 0) {
            d++;
            copy/=10;
        }
        if (((int) Math.pow(n, 2))%((int) Math.pow(10, d)) == n)
            System.out.println(n + " is an automorphic no.");
        else
            System.out.println(n + " is not an automorphic no.");
        sc.close();
    }
}