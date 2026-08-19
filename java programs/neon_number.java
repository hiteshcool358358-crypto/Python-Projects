import java.util.*;
public class neon_number {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, s = 0; double sqr;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        sqr = Math.pow(n, 2);
        while (sqr > 0) {
            s += sqr%10;
            sqr/=10;
        }
        if (s == n) 
            System.out.println(n + " is a neon number: ");
        else
            System.out.println(n + " is not a neon number: ");
        sc.close();
    }
}
