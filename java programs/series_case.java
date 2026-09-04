import java.util.*;
public class series_case {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int c;
        System.out.println("1. 77, 74, 71,...6 terms");
        System.out.println("2. 0, 1, 1, 2, 3, 5,...10 terms");
        System.out.println("3. 2, -4, 6, -8,...10 terms");
        System.out.print("Enter choice: ");
        c = sc.nextInt();
        switch (c) {
            case 1: int value = 77;
            for (int i = 1; i <= 6; i++) {
                System.out.println(value);
                value-=3;
            }
            break;
            case 2: int a = 0, b = 1, n;
            System.out.println(a);
            System.out.println(b);
            for (int i = 1; i <= 10; i++) {
                n = a + b;
                System.out.println(n);
                a = b;
                b = n;
            }
            break;
            case 3: int term = 2;
            for (int i = 1; i <= 10; i++) {
                term = 2 * i;
                if (i % 2 == 0){
                    term = -(term);
                }
                else {
                    continue;
                }
                System.out.println(term);
            }
            break;
            default: System.out.println("Invalid choice");
        }
        sc.close();
    }
}