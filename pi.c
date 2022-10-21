        main(int a,char*b[]) {int i,x,k=0,s=
      sizeof(int), n=atoi(b[1])+2, m=10*n/3,
    *A=calloc(m,s), *P=calloc(n,s),*Q=calloc
  (n,s);     for(i=        0;i<m;
 i++         )A[i]=        2;for
 (;          x<n;x         ++) {
            for(i=         0;i<m
            ;i++){         A[i]*=
            10;}i          --;for
           (;i>0;         i--) { 
           int q=         A[i]/(
           2*i +1         );A[i]
          %=2*i+         1;A[i-1]
         +=q*i;}         Q[k++]=i
        =A[0]/10         ;for(int          v
        =0;v<k&&         i<9; v++)      P[x-
        k+v]=Q[v          ];P[x-k-1    ]+=i
        ==10 ;if          (k*=(i==9)){Q=          /*      PI GENERATOR       */
        realloc            (Q,n*s);}A[0          /* Made By Steve28, 2022!! */
         ]%=10;              }for(i=0;           i<n-2;i++)putchar(48+P[i]);}
