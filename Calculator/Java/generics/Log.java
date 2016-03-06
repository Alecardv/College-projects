package poo;

public class Log implements Funcion {
	Funcion arg;

	public Log(Funcion arg) {
		this.arg = arg;
	}
	
	@Override
	public double eval(double x) {
		return Math.log(arg.eval(x));
	}

	@Override
	public Funcion derivar() {
		return new Div(arg.derivar(), arg);
	}

}
