https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
/*************************************************************************/
/* File Name : program3.c 											     */
/* Purpose   : This will convert arguments to ints and store them in an  */
/*             array. If they are strings, it will store them in a long  */
/*             string                                                    */
/* Author(s) : Patrick McCauley 									     */
/*************************************************************************/

#include <stdio.h>
#include <string.h>
#include "my_string.h"

int main (int argc, char** argv) {
    int int_counter = 0 ; 
    int arg_ints [10] ;
    char arg_str [250] ;
    char temp_str [50] ;
    int str_counter = 0;
    int i, j ;
    
    for (i=0; i < 250; i++) {
        arg_str[i] = '\0';
    }
    for (i=0; i < 10; i++) {
        arg_ints[i] = '\0';
    }
    for (i=0; i < 50; i++) {
        temp_str[i] = '\0';
    }
        
    // Parse through each argument, saving ints and strings separately
    for (i=0; i< argc ; i++) {
        int result = 0 ;
        int temp = 0 ;
        result += sscanf (argv[i], "%d", &temp) ;
        if (result > 0) {
            arg_ints[int_counter] = temp ;
            int_counter++ ;
        } else {
            // Populate the string of str args
            if (str_counter > 0) { // Space delimited
                char space_arr [1] = " " ;
                my_strcat (arg_str, space_arr) ;
                my_strcat (arg_str, argv[i]) ;
            } else {
                // Remove the './' from the first element
                for (j = 2; j < my_strlen2(argv[i]) - 1; j++) {
                    temp_str[j - 2] = argv[i][j] ;
                }
                my_strcat (arg_str, temp_str) ;
            }            
            str_counter++ ;
        }
    }
    
    // Print out each integer element
    for (i = 0; i < int_counter; i++) {
        printf ("%d \n", arg_ints[i]) ;
    }
    printf ("%s \n", arg_str) ;
    
    return (0) ;
}
