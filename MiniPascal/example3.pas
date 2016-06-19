fun hanoi(n:int, scr:int, dest:int, spare:int)
begin
	if n == 1 then begin
		print("mueva ");
		write(scr);
		print(" a ");
		write(dest);
		print("\n")
	end
	else begin
		hanoi(n-1, scr, spare, dest);
		hanoi(1, scr, dest, spare);
		hanoi(n-1, spare, dest, scr)
	end
end
fun main()
n:int;
begin
	print("Las torres de hanoi\n");
	print("Entre el numero de discos: ");
	read(n);
	hanoi(n, 1, 3, 2)
end