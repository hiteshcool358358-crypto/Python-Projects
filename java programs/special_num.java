import java.util.*;
public class special_num {
    public static void main() {
        Scanner sc = new Scanner(System.in);
        int n, copy, fact, special = 0;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        copy = n;
        while (copy > 0) {
            int digit = copy % 10;
            fact = 1;
            for (int i = 1; i <= digit; i++)
                fact *= i;
            special += fact;
            copy /= 10;
        }
        if (special == n)
            System.out.println(n + " is a special no.");
        else
            System.out.println(n + " is not a special no.");
        sc.close();
    }
}
