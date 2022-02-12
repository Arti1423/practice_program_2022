/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
struct node 
 {
     int data;
      struct node *next;
 };
 
 void printElement(struct node *head) {
     
    // if(head == NULL) {
    //     printf("linked list is empty");
    //     return 0;
    // }
    
    // if(head->next == NULL) {
    //      printf("this is last node");
    //           return 0;
    // }
    
    while( head != NULL) {
        printf("data = %d\n", head->data);
        head = head->next;
    }
}
     
 int main () {
 
    struct node a = {10 , NULL};
    struct node b = {20 , NULL};
    struct node c = {30 , NULL};
    struct node d = {40 , NULL};
    
    struct node *aa = &a;
     
     a.next = &b;
     b.next = &c;
     c.next = &d;
     
     struct node *head = &a;
     
     //printf("%d\n", a.data);
     //printf("%d", aa->data);
     
    printElement(head);
    return 0;
}
    

     
     
 

 
 
     
 

