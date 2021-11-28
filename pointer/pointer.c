#include <stdio.h>
#include <stdlib.h>


// * Find max and min element from array using pointers
// * Find mid element of array using pointer
// * Sum of array using pointer
// * Reverse array using pointer

int maxminelement(int *b,int num,int op)
{
    int min, max;
    min=max=*b;
    for(int i=0; i<num;i++)
    {
        if(*(b+i)>max)
        {
            max=*(b+i);
        }
        if(*(b+i)<min)
        {
            min=*(b+i);
        }
    }
    if(op==1)
    {
        return max;
    }
    else
    {
        return min;
    }
}

int midelement(int *b,int num)
{
    return *(b+num/2);
}

int sumofarray(int *b,int num)
{
    int sum=0;
    for(int i=0;i<num;i++)
    {
        sum=sum+*(b+i);
    }
    return sum;
}

void printarray(int *b, int n)
{
    printf(" \n | Printing Array: ");
    for(int i=0;i<n;i++)
    {
        printf(" %d ",*(b+i));
    }
}


void reversearray(int *be,int num)
{
    int lastelement=num-1;
    int a;
    int b;
    for(int i=0;i<lastelement;i++)
    {

        a=*(be+i);
        b=*(be+(lastelement-i));
        a=a^b;
        b=a^b;
        a=a^b;
        *(be+i)=a;
        *(be+(lastelement-i))=b;
    }
}

int main()
{
printf("| C Pointers |");
char str[]="Hello World";
int  a[]={1,5,8,9,6,3,4,-11,25,68};
int  c[]={1,1,2};
int n;
int maxelement,minelement,mid,sum;
n = sizeof(a)/sizeof(a[0]);
maxelement = maxminelement(a,n,1);
minelement = maxminelement(a,n,0);
mid        = midelement(a,n);
sum        = sumofarray(a,n);
printf("\n Max Element in  Array is: %d",maxelement);
printf("\n Min Element in  Array is: %d",minelement);
printf("\n Mid Element in  Array is: %d",mid);
printf("\n Sum Elements in Array is: %d",sum);
reversearray(a,n);
printarray(a,n);
printf("\n >---end---< \n");

return 0;    
}