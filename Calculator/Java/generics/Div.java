package poo;

public class Div implements Funcion {
	Funcion num, den;
	
	public Div(Funcion num, Funcion den) {
		this.num = num;
		this.den = den;
	}
dict a;
dict b;
a + b;

@Override
public int Add 

	@Override
	public double eval(double x) {
		return num.eval(x) / den.eval(x);
	}
	
	@Override
	public Funcion derivar() {
		return new Div(
				new Resta(new Mult(num.derivar(),den), new Mult(num, den.derivar())),
				new Mult(den, den)
				);
	}
	
	@Override
	public String toString() {
		return "(" + num.toString() + ")/(" + den.toString() + ")";
	}
}
