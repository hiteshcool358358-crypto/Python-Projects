import java.util.*;
public class area_case {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.println("a) Area of square");
        System.out.println("a) Area of rectangle");
        System.out.println("a) Area of right angled triangle");
        System.out.println("Enter your choice: ");
        String c = sc.nextLine();
        switch(c) {
            case "a": System.out.print("Enter side of the square: ");
            double s = sc.nextDouble();
            System.out.println("Area: " + Math.pow(s, 2));
            break;
            case "b": System.out.print("Enter length: ");
            double l = sc.nextDouble();
            System.out.print("Enter breadth: ");
            double b = sc.nextDouble();
            System.out.println("Area: " + (l*b));
            break;
            case "c": System.out.print("Enter base: ");
            double base = sc.nextDouble();
            System.out.print("Enter height: ");
            double height = sc.nextDouble();
            System.out.println("Area: " + (0.5*base*height));
            break;
            default: System.out.println("Invalid choice");
            break;
        }
        sc.close();
    }
}
