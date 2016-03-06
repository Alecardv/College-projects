import java.util.StringTokenizer;

public class Scanner {

    private StringTokenizer str;
    private Token nextToken = new Token();

    public Scanner(String line) {
        str = new StringTokenizer(line, "+*-/().<>!=%,|& ", true);
        getToken();
    }

    public Token peekToken() {
        return nextToken;
    }

    public Token getToken() {
        Token result = nextToken;
        nextToken = getNextToken();
        String t1 = result.getType();
        String t2 = nextToken.getType();

        if(t1.equals("_num") && t2.equals(".")) {
            nextToken = getNextToken();
            t2 = nextToken.getType();
            if (!t2.equals("_num")) throw new ArithmeticException("error formato numero");
            t2 = nextToken.getName();
            double x = result.getValue() + nextToken.getValue() * Math.pow(10.0, -t2.length());
            nextToken = getNextToken();
            return new Token("_num", "", x);
        }

        if (t1.equals("$")) {
            if (t2.equals("_int")) {
                double x = nextToken.getValue();
                nextToken = getNextToken();
                return new Token("_input", x);
            }
            else
                throw new ArithmeticException("error en variable de entrada");
        }

        if (t1.equals("+")) {
            if (t2.equals("+")) {
                nextToken = getNextToken();
                return new Token("+");
            }
        }

        if (t1.equals("-")) {
            if (t2.equals("-")) {
                nextToken = getNextToken();
                return new Token("--");
            }
        }

        if (t2.equals("=")) {
            if (t1.equals(">")) {
                nextToken = getNextToken();
                return new Token(">=");
            }
            if (t1.equals("<")) {
                nextToken = getNextToken();
                return new Token("<=");
            }
            if (t1.equals("=")) {
                nextToken = getNextToken();
                return new Token("<=");
            }
        }
        return result;
    }

    private Token getNextToken() {
        long theValue;
        // Retorna un token vacio por defecyto cuando no hay mas
        if (!str.hasMoreTokens()) return new Token();

        String s = str.nextToken();
        if (s.equals(" ")) return getNextToken();

        char c = s.charAt(0);
        if (c >= '0' && c <= '9') { // numeros
            try {
                theValue = Long.parseLong(s);
            }
            catch (NumberFormatException e) {
                throw new ArithmeticException("error en formato numero");
            }
            return new Token("_num", s, theValue);
        }

        if (c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z' || c == '$')
            return new Token("_id", s, 0);

        return new Token(s, s, 0);
    }
}