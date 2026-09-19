import java.util.*;
public class armstrong {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a no.: ");
        int n = sc.nextInt(), copy1 = n, c = 0, copy2 = n, arms = 0;
        while (copy1 > 0) {
            c++;
            copy1/=10;
        }
        if (c == 3) {
            while (copy2 > 0) {
                arms += (int) Math.pow((copy2%10), 3);
                copy2/=10;
            }
            if (arms == n)
                System.out.println(n + " is an armstrong no.");
            else
                System.out.println(n + " is not a armstrong no.");
        }
        else
            System.out.println(n + " is not a three digit no. Please enter a three digit no.");
        sc.close();
    }
}