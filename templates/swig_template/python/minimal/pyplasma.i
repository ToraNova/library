/* This is the interface file */
/* For our wrapper test*/

%module pyplasma 
%{      
        #include "include/irr.h"
%}

/* explicit list of functions to be interfaced */
/*void wrapper_test(int arg1);*/

/* or just */
%include "include/irr.h"
