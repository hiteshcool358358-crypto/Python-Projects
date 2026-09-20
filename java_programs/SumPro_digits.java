import java.util.*;
class SumPro_digits {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, copy1, copy2, s = 0, p = 1;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        copy1 = n;
        copy2 = n;
        while (copy1 > 0) {
            s = s + copy1%10;
            copy1 /= 10;
        }
        while (copy2 > 0) {
            p = p * copy2%10;
            copy2 /= 10;
        }
        System.out.println("Sum of the digits of " + n + ": " + s);
        System.out.println("Product of the digits of " + n + ": " + p);
        sc.close();
    }
}