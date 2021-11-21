#include <stdio.h>
#include <stdlib.h>

struct book{
    char *bookname;
    int price;
    char *author;
    int publishyear;
};

struct ebook{
    char *bookname;
    char *author;
    int price;
    int publishyear;
};
void printbookdetails(struct book Book)
{
printf("\n| Book Name is: %s",Book.bookname);
printf("\n| Book Price is: %d",Book.price);
printf("\n| Book Publish is: %d",Book.publishyear);
}

void printbookdetailsusingptr(struct book *bookpointer)
{
printf("\n+ Printing using Book Pointer");
printf("\n| Book Name is: %s",bookpointer->bookname);
printf("\n| Book Price is: %d",bookpointer->price);
printf("\n| Book Publish is: %d",bookpointer->publishyear);
}

int main()
{
struct book Book1,*bookpointer;
struct ebook eBook1;
// bookpointer=&Book1;
Book1.bookname="Shawshawnk Redemption";
Book1.price=500;
Book1.publishyear=1998;

printbookdetails(Book1);
printbookdetailsusingptr(&Book1);

printf("| Size of Book Structure : %d",sizeof(Book1));
printf("| Size of eBook Structure : %d",sizeof(eBook1));
printf("| Book and eBook are same structure just elements are re-arranged!");
printf("\n >---end---< \n");
return 0;    
}