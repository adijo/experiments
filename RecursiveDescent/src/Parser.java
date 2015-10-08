
public class Parser 
{
	// Parser is written for the production
	// E -> T | T + E
	// T -> int | int * T | ( E )
	private int next = 0;
	private String[] tokens;
	
	public boolean parse(String[] tokens)
	{
		this.tokens = tokens;
		boolean res =  E();
		return (res && next == tokens.length); 
	}
	
	public boolean check(Token tok)
	{
		if(next >= tokens.length) return false;
		String curr = tokens[next++];
		if(tok.equals(Token.PLUS))
		{
			return curr.equals("+");
		}
		
		else if(tok.equals(Token.OPEN))
		{
			return curr.equals("(");
		}
		
		else if(tok.equals(Token.CLOSE))
		{
			return curr.equals(")");
		}
		else if(tok.equals(Token.INT))
		{
		
			return curr.equals("int");
		}
		
		else if(tok.equals(Token.TIMES))
		{
			return curr.equals("*");
		}
		
		else return false;
	}
	
	public boolean E()
	{
		if(next >= tokens.length) return true;
		int save = next;
		boolean res = false;
		
		res = E1();
		if(res) return true;
		else next = save;
		
		if(next >= tokens.length) return false;
		res = E2();
		if(res) return true;
		else return false;
		
	}
	
	
	
	public boolean E1()
	{
		if(next >= tokens.length) return true;
		return T();
	}
	
	public boolean E2()
	{
		return T() && check(Token.PLUS) && E(); 
	}
	
	public boolean T()
	{
		
		int save = next;
		boolean res = T2();
		if(res) return true;
		else next = save;
		if(next >= tokens.length) return false;
		res = T1();
		if(res) return true;
		else next = save;
		if(next >= tokens.length) return false;
		res = T3();
		if(res) return true;
		else return false;
		
	} 
	
	public boolean T1()
	{
		return check(Token.INT);
	}
	
	public boolean T2()
	{
		return check(Token.INT) && check(Token.TIMES) && T();
	}
	
	public boolean T3()
	{
		return check(Token.OPEN) && E() && check(Token.CLOSE);
	}
	
	

}
