#include<stdio.h>
#include<string.h>
int main()
{
    char name[100];
    double salary,sold,ta,TOTAL;
    scanf("%s%.2lf",name,&salary,&sold);
    ta = salary+(sold*(15/100));
    printf("TOTAL = %.2lf",ta);
    return 0;
}
