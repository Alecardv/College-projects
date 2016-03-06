public class Function {

    private String name;
    private Node child;

    public Function() {
    }

    public Function(String name, Node child) {
        this.name = name;
        this.child = child;
    }

    public double calc() {
        switch (name) {
            case "cos":
                return Math.cos(child.calc());
            case "sen":
                return Math.sin(child.calc());
            case "tan":
                return Math.tan(child.calc());
            default:
                return 0;
        }
    }
}
