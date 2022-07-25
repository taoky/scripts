#define _GNU_SOURCE
#include <string.h>
#include <dlfcn.h>
#include <stdint.h>
#include <inttypes.h>

char *strstr(const char *haystack, const char *needle) {
	if ((uintptr_t)haystack > (uintptr_t)0xFFFFFFFF00000000) {
		return NULL;
	}

	char* (*p)(const char *haystack, const char *needle) = dlsym(RTLD_NEXT, "strstr");
	return p(haystack, needle);
}
