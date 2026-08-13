import java.util.*;
class spy_number {
    public static void main() {
        Scanner in=new Scanner(System.in);
        int n, copy1, copy2, s = 0, p = 1;
        System.out.print("Enter a no.: ");
        n = in.nextInt();
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
        if (s == p)
            System.out.println(n + " is a spy number.");
        else
            System.out.println(n + " is not a spy number.");
    }
}