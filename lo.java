public class lo {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
# Execute build and run commands as specified:
javac lo.java
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
java lo
# Expected output: Hello, World!