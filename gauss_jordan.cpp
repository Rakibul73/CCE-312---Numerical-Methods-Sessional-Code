#include<iostream>
#include<iomanip>
#include<math.h>
#include<stdlib.h>

#define   SIZE   10

using namespace std;

int main()
{
	 float a[SIZE][SIZE], x[SIZE], ratio;
	 int i,j,k,n;

     cout<< setprecision(3)<< fixed;


	 cout<<"Enter number of unknowns: ";
	 cin>>n;

	 cout<<"Enter Coefficients of Augmented Matrix: "<< endl;
	 for(i=1;i<=n;i++)
	 {
		  for(j=1;j<=n+1;j++)
		  {
			   cout<<"a["<< i<<"]"<< j<<"]= ";
			   cin>>a[i][j];
		  }
	 }
     for(i=1;i<=n;i++)
     {
          // if(a[i][i] == 0.0)AZaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          // {
          //      cout<<"Mathematical Error!";
          //      exit(0);
          // }
          for(j=1;j<=n;j++)
          {
               if(i!=j)
               {
                    ratio = a[j][i]/a[i][i];
                    for(k=1;k<=n+1;k++)
                    {
                        a[j][k] = a[j][k] - ratio*a[i][k];
                    }
               }
          }
     }
     
     for(i=1;i<=n;i++)
     {
        x[i] = a[i][n+1]/a[i][i];
     }

	 cout<< endl<<"Solution: "<< endl;
	 for(i=1;i<=n;i++)
	 {
	  	cout<<"x["<< i<<"] = "<< x[i]<< endl;
	 }

	 return(0);
}
