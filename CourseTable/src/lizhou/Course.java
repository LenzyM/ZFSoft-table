package lizhou;
import java.util.*;
import java.io.*;
public class Course {
	public static void main(String[] args) throws FileNotFoundException {
		String nameStr[]={"","����","�ո߷�","��ǰ��","������","������","����˶","ԬӢ��","����","���","����"};
		String alltable[][]=new String[8][6];
		for(int i=1;i<nameStr.length;i++)
		{
			func(nameStr[i],alltable);
		}
		System.out.println("    ,һ,��,��,��,��,��,��");
		for(int j=1;j<6;j++)
		{
			System.out.printf("%d%d��,",j*2-1,j*2);
			for(int i=1;i<8;i++)
			{
				if(alltable[i][j]!=null){
				System.out.print(alltable[i][j]);
				System.out.print("/����");
				}
				System.out.print(",");
			}
			System.out.println();
		}
	}
public static void func(String name,String alltable[][]) throws FileNotFoundException {
	 int table[][]=new int[8][6];
	 File file=new File("C:\\Users\\Administrator\\Desktop\\�α�ͳ��EXCEL\\"+name+".txt");
	Scanner sc=new Scanner(file);
	String str[]=new String[100];
	int ct=1;
	while(sc.hasNext())
	{
		str[ct]=sc.nextLine();
		ct++;
	}
	for(int i=1;i<ct;i++)
	{
		proc(str[i],table);
	}
	prt(name,alltable,table);
}
public static void proc(String str ,int [][]table)
{
	char zhouStr=str.charAt(1);
	int zhou=999;
	if(zhouStr=='һ')
		zhou=1;
	if(zhouStr=='��')
		zhou=2;
	if(zhouStr=='��')
		zhou=3;
	if(zhouStr=='��')
		zhou=4;
	if(zhouStr=='��')
		zhou=5;
	if(zhouStr=='��')
		zhou=6;
	if(zhouStr=='��')
		zhou=7;
	String courseStr=str.substring(3, 4);
	int course=Integer.parseInt(courseStr);
	course=(course+1)/2;
	table[zhou][course]=1;
}

public static void prt(String name,String alltable[][],int[][] table)
{
	//System.out.println("    ,һ,��,��,��,��,��,��");
	for(int j=1;j<6;j++)
	{
		//System.out.printf("%d%d��,",j*2-1,j*2);
		for(int i=1;i<8;i++)
		{
			if(table[i][j]==1){
			//System.out.printf("��,");
			}
			else
			{
			//System.out.print("��,");
			alltable[i][j]=alltable[i][j]+name+'/';
			}
		}
		//System.out.println();
	}
}
}