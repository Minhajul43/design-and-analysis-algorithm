#include<stdio.h>
int main()
{
    int n,i;
    printf("Enter no of sequence:");
    scanf("%d",&n);
    int f[n];
    f[0]=0,f[1]=1;
    printf("%d %d",f[0],f[1]);
    for(i=2;i<n;i++)
    {
        f[i]=f[i-1]+f[i-2];
        printf(" %d",f[i]);
    }
    return 0;
}

#include<stdio.h>
int main()
{
    int n,i;
    printf("Enter no of sequence:");
    scanf("%d",&n);
    int f[n];
    f[0]=0,f[1]=1;
    //printf("%d %d",f[0],f[1]);
    for(i=2;i<n;i++)
    {
        f[i]=f[i-1]+f[i-2];
    }
    printf("The %dth fibonacci number is: %d",n,f[n-1]);
    return 0;
}
