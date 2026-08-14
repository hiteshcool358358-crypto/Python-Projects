import java.util.*;
public class series_case {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        int ch;
        System.out.print("1. 77, 74, 71,...6 terms\n2. 0, 1, 1, 2, 3, 5,...10 terms\n3. 2, 4, 8,...10 terms\n"); 
        System.out.print("Enter your choice: ");
        ch = sc.nextInt();
        switch (ch) {
            case 1: int a = 77;
            for (int i = 1; i <= 6; i++) {
                System.out.println(a);
                a -= 3;
            }
            break;
            case 2: int x = 0;
            int y = 1;
            System.out.println(x);
            System.out.println(y);
            for (int i = 1; i <= 8; i++) {
                int value = x + y;
                System.out.println(value);
                x = y;
                y = value;
            }
            break;
            case 3: int m = 2;
            for (int i = 1; i <= 10; i++) {
                System.out.println(m);
                m += 2;
            }
            break;
        }
        sc.close();
    }
}