#!/bin/bash

echo "Content-type: text/html"
echo ""
echo "<html>"
echo "<head>"
echo "<title>System Status</title>"
echo "</head>"
echo "<body>"
echo "<h1>System Status</h1>"

echo "<h2>Uptime:</h2>"
uptime | sed 's/$/<br>/'

echo "<h2>Memory usage:</h2>"
free | sed 's/$/<br>/'

echo "<h2>Disk usage:</h2>"
df | sed 's/$/<br>/'

echo "</body>"
echo "</html>"
