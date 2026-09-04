import java.util.*;
public class vol_case {
    public static void main() {
        Scanner sc=new Scanner(System.in);
        String c;
        System.out.println("1. Volume of a cube");
        System.out.println("2. Volume of a cuboid");
        System.out.println("3. Volume of a sphere");
        System.out.print("Enter yout choice: ");
        c = sc.nextLine();
        switch (c) {
            case "a": System.out.print("Enter side of the cube: ");
            double a = sc.nextDouble();
            System.out.println("Volume of cube: " + (Math.pow(a, 3)));
            break;
            case "b": System.out.print("Enter length: ");
            double l = sc.nextDouble();
            System.out.print("Enter breadth: ");
            double b = sc.nextDouble();
            System.out.print("Enter height: ");
            double h = sc.nextDouble();
            System.out.println("Volume of cuboid: " + (l*b*h));
            break;
            case "c": System.out.print("Enter radius: ");
            double r = sc.nextDouble();
            System.out.println("Volume of sphere: " + ((4/3)*Math.PI*Math.pow(r, 3)));
            break;
            default: System.out.println("Invalid choice");
            break;
        }
        sc.close();
    }
}