import java.util.*;
class Complix{
	int x;
	int y;
	public Complix(int x,int y){
		this.x=x;
		this.y=y;
	}
	public int getX(){
		return x;
	}
	public int getY(){
		return y;
	}                               
	public void setXY(int x,int y){
		this.x=x;
		this.y=y;
	}
	public String toString(Complix t){
		String s;
		s=""+x;
		if(y>0)
			s=s+"+"+y+"i"+"加"+t.x;
		else 
			s=s+y+"i"+"加"+t.x;
		if(t.y>0)
			s=s+"+"+t.y+"i"+"为"+additionX(t);
		else 
			s=s+t.y+"i"+"为"+additionX(t);
		if(additionY(t)>0)
			s=s+"+"+additionY(t)+"i";
		else 
			s=s+additionY(t)+"i";
		return s;
		//return x+"+"+y+"i"+"加"+t.x+"+"+t.y+"i"+"为"+additionX(t)+"+"+additionY(t)+"i";
		
	}
	public int additionX(Complix t){
		return x+t.x;
	} 
	public int additionY(Complix t){
		return y+t.y;
	} 
}
public class Complix_18{
	public static void main(String args[]){
		Scanner reader=new Scanner(System.in);
		int a=reader.nextInt();
		int b=reader.nextInt();
		int c=reader.nextInt();
		int d=reader.nextInt();
		Complix t1=new Complix(a,b);
		Complix t2=new Complix(c,d);
		System.out.println(t1.toString(t2));
	}
}