package poo;

public class Main {

	public static void main(String[] args) {
		Funcion fx = new Log( new Suma(
				new Mult(new Var(), new Var()),
				new Mult(new Numero(3), new Var())
				));
		System.out.println(fx.eval(4));
		Funcion gx = fx.derivar().derivar();
		//System.out.println(gx);
		System.out.println(gx.eval(3));
	}

}
