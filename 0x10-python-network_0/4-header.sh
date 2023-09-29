#!/bin/bash
# This script sends a GET request with a custom header to a specified URL
curl -s -H "X-School-User-Id: 98" "$1"
