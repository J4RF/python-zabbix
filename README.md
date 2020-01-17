# python-zabbix
Simple functions for getting values from the Zabbix API using history.get

Example:

```python
token = getToken('zabbix.example.com', 'admin', 'pa$$word')
getItemValues('zabbix.example.com', token, 'server.example.com', 'vfs.fs.size[/,free]', 1578919583, 1578937627)
```
