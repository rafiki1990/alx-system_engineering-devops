# create a manifest that kills a process named killmenow.

exec { 'kill-killmenow-process':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow'
}
