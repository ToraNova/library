// Code adapted from http://www.c.learncodethehardway.org/book/ex20.html
// Original Author: Zed Shaw

// edited by : ToraNova

#ifndef __dbg_h__
#define __dbg_h__

//#define EDEBUG  //comment to disable debugging prints
#define AUTONL //auto newline for debugging prints

#include <stdio.h>
#include <errno.h>
#include <string.h>

#ifdef EDEBUG //main block---------------------
#define clean_errno() (errno == 0 ? "None" : strerror(errno))
#ifdef AUTONL
#define debug(M, ...) fprintf(stderr, "DEBUG %s:%s:L%d: " M "\n", __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
#define log_err(M, ...) fprintf(stderr, "[ERROR] (%s:%s:L%d: errno: %s) " M "\n", __FILE__, __FUNCTION__, __LINE__, clean_errno(), ##__VA_ARGS__)
#define log_info(M, ...) fprintf(stderr, "[INFO] (%s:%s:L%d) " M "\n", __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
#else
#define debug(M, ...) fprintf(stderr, "DEBUG %s:%s:L%d: " M, __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
#define log_err(M, ...) fprintf(stderr, "[ERROR] (%s:%s:L%d: errno: %s) " M, __FILE__, __FUNCTION__, __LINE__, clean_errno(), ##__VA_ARGS__)
#define log_info(M, ...) fprintf(stderr, "[INFO] (%s:%s:L%d) " M, __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
#endif

#else
//dummy defines
#define debug(M, ...)
#define log_err(M, ...)
#define log_info(M, ...)
#define clean_errno()

#endif //end main block

#endif

