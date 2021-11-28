#include <stdio.h>
#include <stdlib.h>

struct node{
    unsigned int data;
    struct node *link;
};

void addNodeatEnd(struct node *headptr,int number)
{
    struct node *traverse, *prev, *current;
    traverse = headptr;
    while(traverse->link!=NULL)
    {
        traverse = traverse->link;
    }
    prev = traverse;
    current = (struct node*)malloc(sizeof(struct node));
    current->data = number;
    current->link = NULL;
    prev->link=current;
}

void deleteNodeAtEnd(struct node *headptr)
{
    struct node *traverse,*prev,*current;
    traverse=headptr;
    // This Link List has only one node - and boom link list is deleted now
    if(traverse->link==NULL)
    {
        free(traverse);
    }
    else
    {
        while(traverse->link->link!=NULL)
        {
            traverse=traverse->link;
        }
        free(traverse->link);
        traverse->link=NULL;
}

    // struct node *traverse, *prev, *current;
    // traverse = headptr;
    // while(traverse->link!=NULL)
    // {
    //     traverse = traverse->link;
    // }
    // prev = traverse;
    // current = (struct node*)malloc(sizeof(struct node));
    // current->data = number;
    // current->link = NULL;
    // prev->link=current;
}

void printlinklistNCountNodes(struct node *headptr, int flag)
{
    struct node *traverse;
    traverse=headptr;
    int countnodes=0;
    printf("\n");
    while(traverse->link!=NULL)
    {
        printf(" | %d | -> ",traverse->data);
        traverse=traverse->link;
        countnodes++;
    }
    printf(" |  %d  | -> | NULL | ",traverse->data);
    countnodes++;
    if(flag==1)
    {
        printf("\n | No of Nodes in List: %d ",countnodes);
    }
}


int main()
{
    struct node *headptr=(struct node*)malloc(sizeof(struct node));
    headptr->data=5;
    headptr->link=NULL;
    addNodeatEnd(headptr,25);
    printlinklistNCountNodes(headptr,1);
    addNodeatEnd(headptr,99);
    printlinklistNCountNodes(headptr,1);
    deleteNodeAtEnd(headptr);
    printlinklistNCountNodes(headptr,1);

    printf("\n---end---\n");
    return 0;
}