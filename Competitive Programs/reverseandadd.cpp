#include <stdio.h>

/* only works for unsigned longs */
unsigned long reverse(unsigned long original)
{
  unsigned long number = original;
  unsigned long reversed = 0;
  unsigned long place = 1;
  unsigned long i, q;

  for(i = 1000000000; i > 0; i = i / 10) {

    q = number / i;

    if ((q > 0) || (reversed > 0)) {
      reversed = reversed + (q * place);
      number = number - (q * i);
      place = place * 10;
    }
  }

  return(reversed);
}

int is_palindrome(unsigned long original)
{
  unsigned long reversed;
  reversed = reverse(original);
  return(reversed == original);
}

unsigned long reverse_add(unsigned long original, int *iterations)
{
  if (is_palindrome(original)) {
    return(original);
  }

  if (*iterations >= 1000) {
    return(0);
  }

  *iterations = *iterations + 1;
  reverse_add(original + reverse(original), iterations);
}

int main()
{
  int n = 0;
  unsigned long start;
  unsigned long end;
  int iterations = 0;

  while (scanf("%ld\n", &start) == 1) {
    if (n == 0) {
      n = start;
    }
    else {
      iterations = 0;
      end = reverse_add(start, &iterations);
      printf("OUTPUT:%d %ld\n", iterations, end);
    }
  }

  return(0);
}
