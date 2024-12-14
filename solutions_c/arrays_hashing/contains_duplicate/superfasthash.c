/*
Copyright (C) 1999 Free Software Foundation, Inc. <https://fsf.org/>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/

/*
This code originated from the article on SuperFastHash by Paul Hsieh
http://azillionmonkeys.com/qed/hash.html
*/

#include "superfasthash.h"
#include <stdlib.h>

uint32_t SuperFastHash(int value, int capacity)
{
	const char *data = (const char *)&value;
	int len = sizeof(int);
	uint32_t hash = len, tmp;
	int rem;

	if (len <= 0 || data == NULL) {
		return 0;
	}
	rem = len & 3;
	len >>= 2;

	/* Main loop */
	for (; len > 0; len--) {
		hash += *((const uint16_t *)data);
		tmp = (*((const uint16_t *)(data + 2)) << 11) ^ hash;
		hash = (hash << 16) ^ tmp;
		data += 2 * sizeof(uint16_t);
		hash += hash >> 11;
	}

	/* Handle end cases */
	switch (rem) {
	case 3:
		hash += *((const uint16_t *)data);
		hash ^= hash << 16;
		hash ^= ((signed char)data[sizeof(uint16_t)]) << 18;
		hash += hash >> 11;
		break;
	case 2:
		hash += *((const uint16_t *)data);
		hash ^= hash << 11;
		hash += hash >> 17;
		break;
	case 1:
		hash += (signed char)*data;
		hash ^= hash << 10;
		hash += hash >> 1;
	}

	/* Force "avalanching of final 127 bits" */
	hash ^= hash << 3;
	hash += hash >> 5;
	hash ^= hash << 4;
	hash += hash >> 17;
	hash ^= hash << 25;
	hash += hash >> 6;

	return hash % capacity;
}
