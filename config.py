# -*- coding: utf-8 -*-
## Filename
EXPORT_FILE_NAME="fail2ban_{{jail}}.prom"

## File output location for node_exporter
EXPORT_LOCATION='/var/lib/node_exporter/textfile_collector'

## Modifying may break it!
parseKeys = {
  'Currently failed:': ('fail2ban_currently_failed', 'Number of failed SSH-connections.'),
  'Total failed:':('fail2ban_total_failed', 'Number of all time failed SSH-Conncetions.'),
  'Currently banned:':('fail2ban_currently_banned', 'Number of banned IP-Addresses in the timeframe'),
  'Total banned:':('fail2ban_total_banned', 'Number of all time banned IP-Addresses')
}