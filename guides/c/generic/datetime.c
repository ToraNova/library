/*
 * Sample DateTime usage
 * ToraNova Aug 14 2019
 * compile with:
 * gcc datetime.c -o datetime
 */

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <time.h>

int main(int argc, char *argv[]){

	//EXAMPLE 1
	time_t timer;
	struct tm y2k = {0};
	double seconds;

	y2k.tm_hour = 0;   y2k.tm_min = 0; y2k.tm_sec = 0;
	y2k.tm_year = 100; y2k.tm_mon = 0; y2k.tm_mday = 1;

	time(&timer);  // get current time; same as: timer = time(NULL)

	seconds = difftime(timer,mktime(&y2k));
	printf("%.f seconds since January 1, 2000 in the current timezone\n", seconds);

	//EXAMPLE 2
	//for string to struct tm conversion use
	int yy, month, dd, hh, mm, ss, numargs;


	//time(0) or time(NULL) both works
	time_t c = time(0); //obtain current time
	time_t c2;
	char buff[64]; //buffer to hold the string representation
	char specified[64] = "2019/10/02 12:34:56";

	struct tm *tp, *tp2;
	//assign current time to pointer s
	//essentially converts time_t to struct tm
	tp = localtime(&c);

	//print unix timestamp using unsigned long format specifier
	printf("Current Timestamp: %lu\n", c);

	//convert tp to string
	strftime(buff, 64, "%a %Y-%m-%d %H:%M:%S", tp);

	//print out the string representation
	printf("Current Time is: %s\n", buff);

	//parse string and obtain tp2
	//strptime(buff, "%Y/%m/%d %H:%M:%S", tp2); //deprecate as not possible on windows
        numargs = sscanf( specified, "%d/%d/%d %d:%d:%S", &yy, &month, &dd, &hh, &mm, &ss);
	if(numargs < 6){ printf("datetime string error!\n"); return 1;}//should have 6 args
	//must allocate memory for struct tp2 first (UNLESS IT IS DECLARED AS A VARIABLE)
	tp2 = (struct tm *)malloc( sizeof(struct tm) );
        tp2->tm_isdst = -1; //disable DST
        tp2->tm_year = yy - 1900;
        tp2->tm_mon = month - 1;
        tp2->tm_mday = dd;
        tp2->tm_hour = hh;
        tp2->tm_min = mm;
        tp2->tm_sec = ss;
	//tp2->tm_wday = 0;
	//tp2->tm_yday = 0;

	c2 = mktime(tp2); //convert back to time_t

	//print buf2 for validation
	//reset specified for printing
	memset(specified,0,64);
	strftime(specified, 64, "%B %d %Y %H.%M.%S %A", tp2);
	printf("Specified Time is : %s\n", specified);
	printf("Specified timestamp : %lu\n" ,c2);

	return 0;
}
