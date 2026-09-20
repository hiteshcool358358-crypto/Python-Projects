public class fibonacci_series {
    public static void main() {
        int a = 0, b = 1, value, i;
        System.out.print(a + "\n" + b + "\n");
        for (i = 1; i <= 8; i++) {
            value = b + a;
            System.out.println(value);
            a = b;
            b = value;
        }
    }
}
