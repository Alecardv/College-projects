fun foo()
	x : int;
	y : float;
	a : int;
	b : int[20];
	begin
		read(x);
		read(y)
	end


/* Calcula GCD */
fun main()
	x: int;
	y: int;
	g: int;
	begin
		x := 1+(2+(3+(4+(5+(6+(7+(8+(9+10))))))));
		read(x);
		read(y);
		g := y;
		while x > 0 do
			begin
				g := x;
				x := y - (y/x)*x;
				y := g
			end;
		write(g)
	end