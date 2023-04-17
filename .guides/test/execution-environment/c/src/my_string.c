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
#include <stdio.h>

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

	const char* s ;
	for (s = str; *s; ++s) ;
	return (s - str) ;

}



/* CIT 593 students: TODO: implement the remaining string functions
   that were declared in my_string.h */



/* ========== functions to copy a string ========== */

/**
 * This function will take in two strings: a source and destination.
 * It will copy the source to the location of the destination
 * */
char* my_strcpy  (char *dest, const char *src) {
    int i, length = my_strlen2 (src) ;
    for (i = 0; i < length; i++) {
        dest[i] = src[i] ;
    }
    // Null terminate
    dest [length] = '\0' ;
    return (dest) ;
}

/**
 * This function will take in two strings: a source and destination.
 * It will copy the source to the location of the destination
 * */
char* my_strcpy2 (char *dest, const char *src) {
    const char* s ;
    for (s = src; *s; s++) {
        dest[s - src] = *s ;
    }
    // Null terminate
    dest [s - src] = '\0' ;

    return (dest) ;
}



/* ========== functions to search a string ========== */

/**
 * This function will take in a string and a character. If
 * the character is present in the string, it will return the location
 * at which it appears first. If it isn't present, it will return NULL 
 * */
char* my_strchr  (const char *str, int c) {
    int i, length = my_strlen2 (str) ;
    for (i = 0; i < length; i++) {
        if (str[i] == c) {
            return ((char*) str + i) ;
        }
    }
    return (NULL) ;
}

/**
 * This function will take in a string and a character. If
 * the character is present in the string, it will return the location
 * at which it appears first. If it isn't present, it will return NULL 
 * */

char* my_strchr2 (const char *str, int c) {
    const char* s ;
    for (s = str; *s; s++) {
        if (*s == c) {
            return ((char*) s) ;
        }
    }
    return (NULL) ;
}



/* ========== functions to concatenate string ========== */

/**
 * This function will take in two strings, a source and destination.
 * It will append the source to the end of the destination string.
 * */
char* my_strcat  (char *dest, const char *src) {
    int i, src_length = my_strlen2 (src), dest_length = my_strlen2 (dest) ;
    for (i = 0; i < src_length; i++) {
        dest[dest_length + i] = src[i] ;
    }
    // Make sure that new string NULL terminates
    dest [dest_length + src_length + 1] = '\0'; 
    return (dest) ;
}

/**
 * This function will take in two strings, a source and destination.
 * It will append the source to the end of the destination string.
 * */
char* my_strcat2 (char *dest, const char *src) {
    const char* s = src;
    char* temp = dest;        // Temporary return value
    
    int i = 0;
    while (*s) {
        dest++;             
        if (*dest) {          // If d isn't null, continue until it is
            continue;
        } else if (*s) {      // else, append s
            *dest = *s ;      // deref d (should be null now), add s
        } 
        s++ ;                 
    }
    // Make sure the new string NULL terminates
    temp [dest - temp + 2] = '\0' ;
    
    return (temp) ;
}



/* ========== functions to compare two strings ========== */

/**
 * Given two strings, this will return which comes first in the 
 * ASCII table. A negative result indicates that str1 is alphabetically
 * earlier than str2. A positive result indicates the opposite, and a 
 * zero indicates that they are equal.
 * */
int my_strcmp  (const char *str1, const char *str2) {
    int min, str1_len, str2_len, i ;
    str1_len = my_strlen2 (str1) ;
    str2_len = my_strlen2 (str2) ;
    // Find the minimum for iteration
    if (str1_len < str2_len) {
        min = str1_len ;
    } else {
        min = str2_len ;
    }
    
    // Check each character. If it's different, return the difference
    for (i = 0; i < min; i++) {
        if (str1[i] == str2[i]) {
            continue ;
        } else {
            return (str1[i] - str2[i]) ;
        }
    }
    
    // If all characters are the same, return the shorter one
    return (str1_len - str2_len) ;
}

/**
 * Given two strings, this will return which comes first in the 
 * ASCII table. A negative result indicates that str1 is alphabetically
 * earlier than str2. A positive result indicates the opposite, and a 
 * zero indicates that they are equal.
 * */
int my_strcmp2 (const char *str1, const char *str2) {
    // for loop to compare characters, no need to initialize anything
    for ( ; *str1 && *str2; str1++, str2++) {
        if (*str1 == *str2) {
            continue ;
        }
        return (*str1 - *str2) ;
    }
    if (*str1) {
        return (1) ;
    } else if (*str2) {
        return (-1) ;
    } else {
        return (0) ;
    }
}


/**
 * This will reverse the array that is passed in
 * */
char* my_strrev (char *str) {
    int i ;
    int length = my_strlen2 (str) ;
    char copy [length + 1] ; // Setup copy destination for temporary use
    my_strcpy2 (copy, str) ; // Copy into that location
    for (i = 0; i < length; i++) {
        str[i] = copy [length - 1 - i] ;
    }
    return (str) ;
}

/**
 * Upper: [65 - 90], Lower: [97 - 122]
 * This function will reverse the case on letters
 * */
char* my_strccase (char *str) {
    char* ptr ;
    for (ptr = str; *ptr; ptr++) {
        if (*ptr >= 65 && *ptr <= 90) {
            *ptr += 32 ;
        } else if (*ptr >= 97 && *ptr <= 122) {
            *ptr -= 32 ;
        }
    }
    return (str) ;
}



/** ======================================================================
 * This will split a string based on a delimiter (can be multi-char). It took
 * an extremely long time to write/test.
 * ======================================================================
 * */
char* my_strtok(char *str, const char *delim) {
    static char* buffer [50][50] ; // Array of pointers to the tokens
    static int tok_num = 0 ;       // Which token are we on
    static int size = 0 ;          // Number of stored tokens
    char temp [50] ;               // Actual tokens (temporarily)
    
    // if NULL passed in, skip any calcs and return next token
    // or NULL if out of tokens
    if (str == NULL) {
        if (tok_num >= size) {
            return (NULL) ;
        }
        tok_num++ ;
        return ((char*) buffer [tok_num - 1]) ;
    } else {
    
        // Break a given string into multiple strings based on the delimiter 
        int i, j ;
        int debug_ctr = 0 ;
        int counter = 0 ;
        int match = 0 ; // 'boolean' to represent whether we're currently matching
        int delim_length = my_strlen2 (delim) ;
        int length = my_strlen2 (str) ;
        for (i = 0; i < length; i++) {

            if (debug_ctr > 20) {
                return NULL ;
            }
            debug_ctr++;

            // If the char is beginning of the delimiter, check to see if it's the whole thing
            if (str[i] == delim[0]) {
                match = 1 ;

                // Compare each char... 
                for (j = 1; j < delim_length; j++) {
                    if (str[i + j] != delim[j]) {
                        match = 0 ;
                        break ;
                    }
                }

                // If it's still a match, then we don't add the delimiter to the array, 
                // but store our temp array
                if (match == 1) {
                    i += delim_length - 1 ; // Increment by the delimiter length to skip it (-1 for loop)
                    temp[counter] = '\0' ; // NULL terminate
                    my_strcpy2 ((char*) buffer[size], temp) ;
                    for (j = 0; j < counter; j++) {
                    }
                    
                    size++ ;
                    counter = 0 ;
                }
            } else {
                temp[counter] = str[i] ;
                counter++ ;
            } 
        }
        
        // If the loop ended but there's some str left, add that at the end
        if (counter > 0) {
            temp[counter] = '\0' ; // Confirm NULL termination
            static char temp_copy [50] ;
            my_strcpy2 ((char*) buffer[size], temp) ;
            size++ ;
        }
        
        tok_num++ ;
        return ((char*) buffer[tok_num - 1]) ;
    }
}