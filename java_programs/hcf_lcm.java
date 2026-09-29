import java.util.*;
public class hcf_lcm {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the first no..: ");
        int n1 = sc.nextInt();
        System.out.print("Enter the second no.: ");
        int n2 = sc.nextInt(), hcf_no = 1; boolean hcf = false;
        for (int i = 2; i <= Math.min(n1, n2); i++) {
            if (n1%i == 0 && n2%i == 0) {
                hcf = true;
                hcf_no = i;
            }
        }
        if(hcf)
            System.out.println("The HCF of " + n1 + " and " + n2 + "is: " + hcf_no);
        else if (!hcf)
            System.out.println("The HCF of " + n1 + " and " + n2 + "is: 1");
        System.out.println("The LCM of " + n1 + " and " + n2 + "is: " + ((n1*n2)/hcf_no));
        sc.close();
    }
}