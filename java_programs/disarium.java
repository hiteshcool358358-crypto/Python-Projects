import java.util.*;
public class disarium {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a no.: ");
        int n = sc.nextInt(), temp1 = n, temp2 = n, c = 0, sum = 0;
        while (temp1 > 0) {
            c++;
            temp1/=10;
        }
        for (int i = c; i >= 1; i--) {
            sum += ((int) Math.pow(temp2%10, i));
            temp2/=10;
        }
        if (sum == n)
            System.out.println(n + " is a disarium no.");
        else
            System.out.println(n + " is not a disarium no.");
        sc.close();
    }
}