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
/* File Name : program1.c 											     */
/* Purpose   : this C-file tests the functions of the "my_string" library*/
/*                                                                       */
/*                                                                       */
/* Author(s) : tjf & you 											     */
/*************************************************************************/

#include <stdio.h>
#include <string.h>
#include "../src/my_string.h"

int main() {

	// a string we will test with
	char my_string [100] = "Tom" ;

	// test of strlen() functions 
	printf ("Sample string: \"%s\" \n", my_string) ;
	printf (" string's length: strlen()     = %lu \n",   strlen  (my_string)) ;
	printf (" string's length: my_strlen()  = %lu \n", my_strlen (my_string)) ;
	printf (" string's length: my_strlen2() = %lu \n", my_strlen2(my_string)) ;

    /* CIT 593 students: TODO: add code to test your my_string.h functions */

	return (0) ;

}
