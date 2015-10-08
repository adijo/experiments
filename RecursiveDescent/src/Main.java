
public class Main 
{

		
	public static void main(String[] args)
	{
		Parser p = new Parser();
		String[] tokens = {"(", "(", "int", "*", "int", ")", ")"};
		
		System.out.println(p.parse(tokens));
		
		
	}
}
