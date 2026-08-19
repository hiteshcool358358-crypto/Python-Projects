import java.util.*;
public class niven_num {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, s = 0, copy;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        copy = n;
        while (copy > 0) {
            s += copy%10;
            copy/=10;
        }
        if (n%s==0)
            System.out.println(n + " is a niven no.");
        else
            System.out.println(n + " is not a niven no.");
        sc.close();
    }
}