import java.util.*;
public class PalinCheck {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, rev = 0, copy;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        copy = n;
        while (copy > 0) {
            rev = (rev*10) + (copy%10);
            copy /= 10;
        }
        if (rev == n) 
            System.out.println(n + " is a palindrome no.");
        else
            System.out.println(n + " is not a palindrome no.");
        sc.close();
    }
}
