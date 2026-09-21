import java.util.*;
public class kaprekar {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a no.: ");
        int n = sc.nextInt(), sqr = (int) Math.pow(n, 2), temp = sqr, c = 0, rd;
        while (temp > 0) {
            c++;
            temp/=10;
        }
        if (c%2 == 0){
            rd = c/2;
        }
        else {
            rd = (c/2) + 1;
        }
        int RightDigits = sqr%((int) Math.pow(10, rd));
        int LeftDigits = sqr/((int) Math.pow(10, rd));
        if (RightDigits+LeftDigits == n)
            System.out.println(n + " is a kaprekar no.");
        else
            System.out.println(n + " is not a kaprekar no.");
        sc.close();
    }
}