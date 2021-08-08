#include <stdio.h>
#include <string.h>
#define NAMELENGTH 30 /* maximum length of name */
#define NSUITORS 100 /* maximum number of suitors */
#define BESTHEIGHT 180 /* best height in centimeters */
#define BESTWEIGHT 75 /* best weight in kilograms */
typedef struct {
char first[NAMELENGTH]; /* suitor’s first name */
char last[NAMELENGTH]; /* suitor’s last name */
int height; /* suitor’s height */
int weight; /* suitor’s weight */
} suitor;
suitor suitors[NSUITORS]; /* database of suitors */
int nsuitors; /* number of suitors */

read_suitors()
{

int count;
printf("Enter count of names: ");
scanf("%d",&count);
char first[NAMELENGTH], last[NAMELENGTH];
int height, weight;
nsuitors = 0;
while(nsuitors != count-1){
	/*
while (scanf("%s %s %d %d\n",suitors[nsuitors].first,
suitors[nsuitors].last, &height, &weight) !=EOF) { */
scanf("%s %s %d %d\n",suitors[nsuitors].first,suitors[nsuitors].last, &height, &weight);
suitors[nsuitors].height = abs(height - BESTHEIGHT);
if (weight > BESTWEIGHT)
suitors[nsuitors].weight = weight - BESTWEIGHT;
else
suitors[nsuitors].weight = - weight;
++ nsuitors ;
}
}
int suitor_compare(suitor *a, suitor *b)
{
int result; /* result of comparison */
if (a->height < b->height) return(-1);
if (a->height > b->height) return(1);
if (a->weight < b->weight) return(-1);
if (a->weight > b->weight) return(1);
if ((result=strcmp(a->last,b->last)) != 0) return result;
return(strcmp(a->first,b->first));
}
int main()
{
int i; /* counter */
int suitor_compare();
read_suitors();
qsort(suitors, nsuitors, sizeof(suitor), suitor_compare);
printf("\n");
printf("Result in sorted order:\n ");

for (i=0; i<nsuitors; i++)
printf("%s, %s\n",suitors[i].last, suitors[i].first);
}
