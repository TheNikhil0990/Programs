#include<stdio.h>
    int main()
    {
    int num1,num2,carry,count,bit1,bit2;
    scanf("%d%d",&num1,&num2);
    while(num1 || num2)
    {
    count=0;
    carry=0;
    while(num1||num2)
    {
    bit1=num1%10;
    bit2=num2%10;
    if((bit1+bit2+carry)>9)count++;
    carry=(bit1+bit2+carry)/10;
    num1=num1/10;
    num2=num2/10;
    }
    if(count==0)printf("\nOUTPUT:No carry operation.\n");
    else if(count==1)printf("\nOUTPUT:1 carry operation.\n");
    else printf("\n%d OUTPUT:carry operations.\n",count);
    scanf("%d%d",&num1,&num2);
    }
    return 0;
    }

