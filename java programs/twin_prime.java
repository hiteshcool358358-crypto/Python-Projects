import java.util.*;
public class twin_prime {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the first prime no.: ");
        int n1 = sc.nextInt(), c1 = 0; boolean prime1 = false;
        System.out.print("Enter the second prime no.: ");
        int n2 = sc.nextInt(), c2 = 0; boolean prime2 = false, cont;
        for (int i = 1; i <= n1; i++) {
            if (n1 % i == 0)
            c1++;
            else
            continue;
        }
        if (c1 == 2)
        prime1 = true;
        else {
            System.out.println(n1 + " is not a prime no.");
            cont = false;
        }
        for (int i = 1; i <= n2; i++) {
            if (n2 % i == 0)
            c2++;
            else
            continue;
        }
        if (c2 == 2)
        prime2 = true;
        else {
            System.out.println(n2 + " is not a prime no.");
            cont = false;
        }
        if (prime1 == true && prime2 == true)
            cont = true;
        else
            cont = false;
        if (cont != false) {
            if (n1 - n2 == 2 || n2 - n1 == 2)
            System.out.println(n1 + " and " + n2 + " are twin prime nos.");
            else
            System.out.println(n1 + " and " + n2 + " are not twin prime nos.");
        }
        else if (cont == false)
            System.out.println("Further exexution of the program was terminated!");
        sc.close();
    }
}