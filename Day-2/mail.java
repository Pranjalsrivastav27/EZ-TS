import java.util.Scanner;
public class Bank1 {
static int fact1(int e)
{
if(e==1)
{
return 1;
}
else
{
return e*fact1(e-1);
}
}
public static void main(String[] args)
{
Scanner sc=new Scanner(System.in);
System.out.println("enter number");
int n=sc.nextInt();
int a=fact1(n);
System.out.println(a);
}

}


       