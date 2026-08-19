import java.util.*;
public class duck {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, c = 0, copy;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        copy = n;
        while (copy > 0) {
            if (copy % 10 == 0)
                c++;
            copy /= 10;
        }
        if (c > 0)
            System.out.println(n + " is a duck no.");
        else
            System.out.println(n + " is not a duck no.");
        sc.close();
    }
}