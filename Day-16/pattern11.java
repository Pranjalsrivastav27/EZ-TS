import java.util.Scanner;

public class pattern11 {
public static void main(String[]args)
{
Scanner sc=new Scanner(System.in);
System.out.println("enter the number:");
int n=sc.nextInt();
int col=2*n-1;
int start=n-1;
int end=n-1;
for(int i=0;i<n;i++)
{
for(int j=0;i<col;j++)
{
if (j>=start && j<=end){
{
    if(j==start || j==end || i==n-1)
    {
    System.out.print("*");
    }
    else{
    System.out.print(" "); 
    }
}
else{
System.out.print(" "); 
}

}
System.out.println();
start--;
end++;


}
}
}
