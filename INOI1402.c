#include <stdio.h>

#include<stdio.h>

int main()
{
       int i,j,k,v,e,x,y,l;
       scanf("%d%d",&v,&e);
       int a[v][v];
       for(i=0;i<v;i++)
       {
              for(j=0;j<v;j++)
              {
                     if(i==j)
                     a[i][j]= 0;
                     else
                     a[i][j] = -1;
              }
       }
       for(i=0;i<e;i++)
       {
              scanf("%d%d%d",&x,&y,&l);
              a[x-1][y-1] = l;
              a[y-1][x-1] = l;
       }
      
       for(k=0;k<v;k++)
       {
              for(i=0;i<v;i++)
              {
                     for(j=0;j<v;j++)
                     {
                           if(i!=j && (a[i][j]>a[i][k] + a[k][j] || a[i][j]==-1) && a[i][k]>-1 && a[k][j]>-1)
                           {
                                  a[i][j] = a[i][k] + a[k][j];
                           }
                     }
              }
       }
       long long int max = 0;
       for(i=0;i<v;i++)
       {
              for(j=i+1;j<v;j++)
              {
                     if(a[i][j] > max)
                     {
                           max = a[i][j];
                     }
              }
       }
       printf("%lld\n",max);
       return 0;
}
