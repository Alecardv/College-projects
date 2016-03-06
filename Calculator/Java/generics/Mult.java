package poo;

public class Mult implements Funcion {
	Funcion left, right;
	
	public Mult(Funcion left, Funcion right) {
		this.left = left;
		this.right = right;
	}

	@Override
	public double eval(double x) {
		return left.eval(x) * right.eval(x);
	}
	
	@Override
	public Funcion derivar() {
		return new Suma(
				new Mult(left.derivar(),right),
				new Mult(left, right.derivar())
				);
	}
	
	@Override
	public String toString() {
		return "(" + left.toString() + ")*(" + right.toString() + ")";
	}
}
