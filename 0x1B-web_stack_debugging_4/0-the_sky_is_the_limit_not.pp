# Increase the number of requests to be handled by nginx

# Let's increase ULIMIT of the default.

exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/g" /etc/default/nginx',
  path    => '/usr/local/bin:/bin'
}

# Restart the Nginx server
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d'
}
