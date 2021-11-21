#include <stdio.h>
#include <stdlib.h>

int main()
{
int *ptr=NULL;
int *ptr2=NULL;
ptr=(int*)malloc(sizeof(int)*4);
if (ptr == NULL) 
{
    printf("Memory not allocated.\n");
    exit(0);
}
printf("\n| Malloc Allocated Memory Address: %p ",ptr);
printf("\n| Value at first location of Malloc Address %p is %d ",ptr,*ptr);


ptr2=(int*)calloc(4,sizeof(int));
if (ptr2 == NULL) 
{
    printf("Memory not allocated.\n");
    exit(0);
}
printf("\n| Calloc Allocated Memory Address: %p ",ptr2);
printf("\n| Writing values to Address %p to %p",ptr2,ptr2+4);
*(ptr2)=5;
*(ptr2+1)=9;
*(ptr2+2)=7;
*(ptr2+3)=55;
printf("\n| Value at location of Address %p is %d ",ptr2,*(ptr2));
printf("\n| Value at location of Address %p is %d ",ptr2+1,*(ptr2+1));
printf("\n| Value at location of Address %p is %d ",ptr2+2,*(ptr2+2));
printf("\n| Value at location of Address %p is %d ",ptr2+3,*(ptr2+3));

ptr2 = (int*)realloc(ptr2,2*sizeof(int));
printf("\n| Value at location of Address %p is %d ",ptr2,*(ptr2));
printf("\n| Value at location of Address %p is %d ",ptr2+1,*(ptr2+1));
printf("\n| Value at location of Address %p is %d ",ptr2+2,*(ptr2+2));
printf("\n| Value at location of Address %p is %d ",ptr2+3,*(ptr2+3));

free(ptr2);
printf("\n| Value at location of Address %p is %d ",ptr2,*(ptr2));
printf("\n| Value at location of Address %p is %d ",ptr2+1,*(ptr2+1));
printf("\n| Value at location of Address %p is %d ",ptr2+2,*(ptr2+2));
printf("\n| Value at location of Address %p is %d ",ptr2+3,*(ptr2+3));
printf("\n >---end---< \n");

return 0;
}
