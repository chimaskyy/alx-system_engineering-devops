#increase the ULIMIT of the default file

exec { 'update_ulimit':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin',  # path to the sed command
  notify  => Exec['nginx-restart'], # Ensure Nginx restarts when the file is updated
}

# Restart Nginx
exec { 'nginx-restart':
  command     => 'service nginx restart',
  path        => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  refreshonly => true,
}
