
// #include <stdio.h>
// void main() {
//   int k=5;
//   int *p=&k;
//   int **m=&p;
//   **m=6;
//     printf("%d",k);

// }

// #include <stdio.h>
// void main() {
//   int k=5;
//   int *p=&k;
//   int **m=&p;
   
//     printf("%d%d%d",**m,k,*p);

// }


// #include <stdio.h>
// void main() {
//   int x=20,*y,*z;
//   y=&x;
//   z=y;
//   *y++;
//   *z++;
//   x++;
//   printf("%d %d %d\n",x,y,z);

// }

// #include <stdio.h>

// void test(int *p, int *q) {
//     *p = *p * *q;
//     *q = *p + *q;
//     *p = *p - *q;
// }

// void main() {
//     int a = 5, b = 6;

//     test(&a, &b);

//     printf("%d %d", a, b);
// }


// #include <stdio.h>

// int main() {
//     int a = 3, *b = &a;

//     printf("%d", a * b);

//     return 0;
// }


// #include <stdio.h>

// int main() {
//     int arr[2] = {4, 5,6,7,8}; // Declare and initialize an integer array with 2 elements

//     printf("%d", arr[3]); // Attempt to print the fourth element (index 3)

//     return 0;
// }


// #include <stdio.h>

// int main() {
//     char chr[] = "ABES Engineering College";
//     char *ptr = chr;

//     printf("%s", ptr + ptr[5] + ptr[12] - ptr[1] - ptr[14]);

//     return 0;
// }

// #include <stdio.h>
// #include <string.h>

// void printlength(char *s, char *t) {
//     int len = (strlen(s) > strlen(t)) ? strlen(s) : strlen(t);
//     printf("%d\n", len);
// }

// int main() {
//     char *x = "abc";
//     char *y = "defgh";
//     printlength(x, y);
//     return 0;
// }


// #include <stdio.h>

// void foo(int **p) {
//     int j = 11;
//     *p = &j; // Modifies the value of p to point to j
//     printf("%d\n", **p); // Prints the value of j, which is 11
// }

// int main() {
//     int i = 10;
//     int *const p = &i; // p is a constant pointer to i

//  foo(&p); // This line would cause a compilation error because p is const

//     printf("%d\n", *p); // Prints the value of i, which is 10

// }



// #include <stdio.h>

// void rer(int **ptr2, int **ptr1) {
//     int i;
//     i = **ptr2;
//     **ptr2 = **ptr1;
//     **ptr1 = i;
//     **ptr1 *= **ptr2;
//     **ptr2 += **ptr1;
// }

// void main() {
//     int var1 = 5, var2 = 10;
//     int *ptr1 = &var1, *ptr2 = &var2;
//     rer(&ptr1, &ptr2);
//     printf("%d %d ", var2, var1);
// }

#include <stdio.h>

int main() {
    static int a[] = {10, 20, 30, 40, 50};
    static int *p[] = {a, a+3, a+4, a+1, a+2};
    int **ptr = p;
    ptr++;

    printf("%d %d", ptr-p, **ptr);
    return 0;
}

