# Adjust user limits.

exec { 'adjust-hard-limits-for-holberton':
  command => "sed -i '/^holberton hard/s/4/50000/g' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin/'
}

exec { 'adjust-soft-limits-for-holberton':
  command => "sed -i '/^holberton soft/s/5/50000/g' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin/'
}
