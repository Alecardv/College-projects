import java.util.Objects;

public class Token {

    private String type;
    private String name;
    private double value;

    public Token() {
        this("");
    }

    public Token(String type) {
        this(type, 0);
    }

    public Token(String type, double value) {
        this(type, type, value);
    }

    public Token(String type, String name, double value) {
        this.type = type;
        this.name = name;
        this.value = value;
    }

    public String getType() {
        return type;
    }

    public String getName() {
        return name;
    }

    public double getValue() {
        return value;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Token other = (Token) obj;
        if (!Objects.equals(this.type, other.type)) {
            return false;
        }
        if (!Objects.equals(this.name, other.name)) {
            return false;
        }
        if (Double.doubleToLongBits(this.value) != Double.doubleToLongBits(other.value)) {
            return false;
        }
        return true;
    }


    @Override
    public String toString() {
        return " type=" + type + " name=" + name + " value=" + value;
    }
}
