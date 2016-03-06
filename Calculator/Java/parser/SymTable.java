import java.util.HashMap;
import java.util.Map;

public class SymTable {

    private Map<String, Double> st = new HashMap<String, Double>();

    public void put(String name, double value) {
        st.put(name, value);
    }

    public double get(String name) {
        Double x = st.get(name);
        return (x != null)? x.doubleValue() : 0;
    }
}
