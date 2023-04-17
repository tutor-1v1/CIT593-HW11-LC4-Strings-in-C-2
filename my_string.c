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
https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
/*************************************************************************/
/* File Name : my_string.c 											     */
/* Purpose   : this C-file defines the functions previously declared	 */
/*             in the my_string.h header file 						     */
/*																		 */
/* Author(s) : tjf & you 											     */
/*************************************************************************/

#include "my_string.h"

// strlen functions takes in a pointer to a string and return its length
//
size_t2 my_strlen  (const char *str) {

	size_t2 len = 0 ;
	while (str[len] != '\0') {  // count up to the first NULL
		len++ ; 
	}
	return (len) ;

}

size_t2 my_strlen2 (const char *str) {

	const char* s;
	for (s = str; *s; ++s) ;
	return (s - str);

}


/* CIT 593 students: TODO: implement the remaining string functions
   that were declared in my_string.h */