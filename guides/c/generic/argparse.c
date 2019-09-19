/*
 * Perform argument parsing using argp from the GNU C library
 * example obtained from
 * https://stackoverflow.com/questions/9642732/parsing-command-line-arguments-in-c
 * RESERVED KEYWORDS (-h --help) (-? --usage) (-v --version) try not to use these
 */
#include <stdlib.h>
#include <stdio.h>
#include <argp.h>
#include <stdbool.h>
#include <errno.h>

const char *argp_program_version = "argparse version 1.0";
const char *argp_program_bug_address = "toranova@examplemail.com";
static char doc[] = "Simple Argument Parsing Example Program";
static char args_doc[] = "[STRING]"; //[STRING]... for multiple args
static struct argp_option options[] = {
	{ "count", 'c', "COUNT", 0, "Number of lines -- COUNT to print"},
	{ "newline", 'n', 0, 0, "Newline after each print"},
	{ "space", 's', 0, 0, "Space after each print"},
	{ 0 }
};

//editable
struct arguments {
	enum { JOINED_MODE, NEWLINE_MODE, SPACE_MODE } mode; //for multi type classes
	int numlines;
	char *pstring;
};

static error_t parse_opt(int key, char *arg, struct argp_state *state) {
	struct arguments *arguments = state->input;
	char *end;
	switch (key) {
		case 'n':
			arguments->mode = NEWLINE_MODE; break;

		case 's':
			arguments->mode = SPACE_MODE; break;

		case 'c':
			arguments->numlines = strtol( arg, &end, 10); //parse to base10
			if( errno == ERANGE ){
				//error handling
				printf("Range_Error on numlines\n");
				errno = 0;
				arguments->numlines = 1; //fallback value
			} break;

		case ARGP_KEY_ARG:
			arguments->pstring = arg; break;

		case ARGP_KEY_END:
			if( state->arg_num < 1 ){
				/* not enough arguments */
				argp_usage( state ); break;
			}
			break;

		default: return ARGP_ERR_UNKNOWN;
	}
	return 0;
}

static struct argp argp = { options, parse_opt, args_doc, doc, 0, 0, 0 };

int main(int argc, char *argv[]){

	struct arguments arguments;

	// default argument values
	arguments.mode = JOINED_MODE;
	arguments.numlines = 1;

	// perform parsing, result in var 'arguments'
	argp_parse(&argp, argc, argv, 0, 0, &arguments);

	/* following logic is pretty damn inefficient but screw it this is
	 * just a fricking argparse example not an efficient example
	 * switch should be outside and possibly string is pre-formatted for
	 * increased speed
	 */
	int i;
	for(i=0;i<arguments.numlines;i++){
		switch( arguments.mode ){
			case NEWLINE_MODE:
				printf("%s\n",arguments.pstring); break;
			case SPACE_MODE:
				printf("%s ",arguments.pstring); break;
			default:
				//JOINED_MODE
				printf("%s",arguments.pstring); break;
		}
	}
	return 0;
}
