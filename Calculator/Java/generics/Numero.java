package poo;

public class Numero implements Funcion {
	double val;
	
	public Numero(double x) {
		val = x;
	}

	@Override
	public double eval(double x) {
		return val;
	}

	@Override
	public Funcion derivar() {
		return new Numero(0.0);
	}
	
	@Override
	public String toString() {
		return val+"";
	}

}
