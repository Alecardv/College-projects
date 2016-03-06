package poo;

public class Suma implements Funcion {
	Funcion left, right;
	
	public Suma(Funcion left, Funcion right) {
		this.left = left;
		this.right = right;
	}
	
	@Override
	public double eval(double x) {
		return left.eval(x) + right.eval(x);
	}

	@Override
	public Funcion derivar() {
		return new Suma(left.derivar(), right.derivar());
	}
	
	@Override
	public String toString() {
		return left.toString() + " + " + right.toString();
	}

}
