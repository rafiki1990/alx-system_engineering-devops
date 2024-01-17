# Using strace to diagnose what's wrong with the server. and configure puppet
exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'}
