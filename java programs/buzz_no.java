import java.util.*;
public class buzz_no {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a no.: ");
        int n = sc.nextInt();
        if ((n%10 == 7) || (n%7 == 00)) 
            System.out.println(n + " is a buzz no.");
        else
            System.out.println(n + " is anot a buzz no.");
        sc.close();
    }
}