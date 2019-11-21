// Code adapted from http://www.c.learncodethehardway.org/book/ex20.html
// Original Author: Zed Shaw
// edited by : ToraNova chia_jason96@live.com

#ifndef __dbg_h__
#define __dbg_h__

#ifdef __cplusplus
extern "C"{
#endif

#define EDEBUG //comment to disable debugging prints
#define ELOGGI //comment to disable logging prints
#define AUTONL //auto newline for debugging prints

#include <stdio.h>
#include <errno.h>
#include <string.h>

#define clean_errno() (errno == 0 ? "None" : strerror(errno))

#ifdef EDEBUG //main block---------------------
    #ifdef AUTONL
    #define debug(M, ...) fprintf(stderr, "DEBUG %s:%s:L%d: " M "\n", __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
    #else
    #define debug(M, ...) fprintf(stderr, "DEBUG %s:%s:L%d: " M, __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
    #endif
#else
    //dummy defines
    #define debug(M, ...) ((void)0)
#endif //end main debug block

#ifdef ELOGGI
    #ifdef AUTONL
    #define log_err(M, ...) fprintf(stderr, "[ERROR] (%s:%s:L%d: errno: %s) " M "\n", __FILE__, __FUNCTION__, __LINE__, clean_errno(), ##__VA_ARGS__)
    #define log_info(M, ...) fprintf(stderr, "[INFO] (%s:%s:L%d) " M "\n", __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
    #else
    #define log_err(M, ...) fprintf(stderr, "[ERROR] (%s:%s:L%d: errno: %s) " M, __FILE__, __FUNCTION__, __LINE__, clean_errno(), ##__VA_ARGS__)
    #define log_info(M, ...) fprintf(stderr, "[INFO] (%s:%s:L%d) " M, __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
    #endif
#else
    //dummy defines
    #define log_err(M, ...) ((void)0)
    #define log_info(M, ...) ((void)0)
#endif //end main logging block


#ifdef __cplusplus
};
#endif

#endif
