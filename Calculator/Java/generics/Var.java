package poo;

public class Var implements Funcion {
	
	public Var() {		
	}

	@Override
	public double eval(double x) {
		return x;
	}

	@Override
	public Funcion derivar() {
		return new Numero(1.0);
	}
	
	@Override
	public String toString() {
		return "x";
	}
}
