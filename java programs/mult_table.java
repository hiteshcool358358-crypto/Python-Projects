import java.util.*;
public class mult_table {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int n, i;
        System.out.print("Enter a no.: ");
        n = sc.nextInt();
        for (i = 1; i <= 10; i++) {
            System.out.println(n + " * " + i + " = " + (n*i));
        }
        sc.close();
    }
}