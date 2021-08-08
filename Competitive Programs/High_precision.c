#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#define MAXDIGITS 100
#define PLUS 1
#define MINUS -1

typedef struct{
	char digits[MAXDIGITS];
	int signbit;
	int lastdigit;
} bignum;

void print_bignum(bignum *n);
void int_to_bignum(int s, bignum *n);
void initialize_bignum(bignum *n);
int max(int a, int b);
void add_bignum(bignum *a, bignum *b, bignum *c);
void subtract_bignum(bignum *a, bignum *b, bignum *c);
int compare_bignum(bignum *a, bignum *b);
void zero_justify(bignum *n);

void print_bignum(bignum *n)
{
	int i;
	if (n->signbit == MINUS) printf("- ");
	for (i=n->lastdigit; i>=0; i--)
	printf("%c",'0'+n->digits[i]);
	printf("\n");
}

int max(int a, int b)
{
	if (a > b)
	return(a);
	else
	return(b);
}

void int_to_bignum(int s, bignum *n)
{
	int i;
	int t;
	if (s >= 0) n->signbit = PLUS;
	else n->signbit = MINUS;
	for (i=0; i<MAXDIGITS; i++) n->digits[i] = (char) 0;
	n->lastdigit = -1;
	t = abs(s);
	while (t > 0) {
		n->lastdigit ++;
		n->digits[ n->lastdigit ] = (t % 10);
		t = t / 10;
	}
	if (s == 0) n->lastdigit = 0;
}

void initialize_bignum(bignum *n)
{
	int_to_bignum(0,n);
}

void add_bignum(bignum *a, bignum *b, bignum *c)
{
	int carry;
	int i;
	initialize_bignum(c);
	if (a->signbit == b->signbit) c->signbit = a->signbit;
	else {
		if (a->signbit == MINUS) {
			a->signbit = PLUS;
			subtract_bignum(b,a,c);
			a->signbit = MINUS;
		} else {
			b->signbit = PLUS;
			subtract_bignum(a,b,c);
			b->signbit = MINUS;
		}
		return;
	}
	c->lastdigit = max(a->lastdigit,b->lastdigit)+1;
	carry = 0;
	for (i=0; i<=(c->lastdigit); i++) {
		c->digits[i] = (char) (carry+a->digits[i]+b->digits[i]) % 10;
		carry = (carry + a->digits[i] + b->digits[i]) / 10;
	}
	zero_justify(c);
}

void subtract_bignum(bignum *a, bignum *b, bignum *c){
	int borrow;
	int v;
	int i;
	if ((a->signbit == MINUS) || (b->signbit == MINUS)) {
		b->signbit = -1 * b->signbit;
		add_bignum(a,b,c);
		b->signbit = -1 * b->signbit;
		return;
	}
	if (compare_bignum(a,b) == PLUS) {
		subtract_bignum(b,a,c);
		c->signbit = MINUS;
		return;
	}
	c->lastdigit = max(a->lastdigit,b->lastdigit);
	borrow = 0;
	for (i=0; i<=(c->lastdigit); i++) {
		v = (a->digits - borrow - b->digits);
		if (a->digits > 0)
		borrow = 0;
		if (v < 0) {
			v = v + 10;
			borrow = 1;
		}
		c->digits[i] = (char) v % 10;
	}
	zero_justify(c);
}

int compare_bignum(bignum *a, bignum *b){
	int i;
	if ((a->signbit == MINUS) && (b->signbit == PLUS)) return(PLUS);
	if ((a->signbit == PLUS) && (b->signbit == MINUS)) return(MINUS);
	if (b->lastdigit > a->lastdigit) return (PLUS * a->signbit);
	if (a->lastdigit > b->lastdigit) return (MINUS * a->signbit);
	for (i = a->lastdigit; i>=0; i--) {
		if (a->digits[i] > b->digits[i]) return(MINUS * a->signbit);
		if (b->digits[i] > a->digits[i]) return(PLUS * a->signbit);
	}
	return(0);
}

void zero_justify(bignum *n){
	while ((n->lastdigit > 0) && (n->digits[ n->lastdigit ] == 0))
	n->lastdigit --;
	if ((n->lastdigit == 0) && (n->digits[0] == 0))
	n->signbit = PLUS;
}

int main(){
	int  a,b;
	bignum n1,n2,n3;

	while (scanf("%d %d\n",&a,&b) != EOF) {
		printf("a = %d    b = %d\n",a,b);
		int_to_bignum(a,&n1);
		int_to_bignum(b,&n2);

		add_bignum(&n1,&n2,&n3);
		printf("addition : ");
		print_bignum(&n3);
}
}
