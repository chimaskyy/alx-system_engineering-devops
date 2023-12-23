# Creates a file in /temp

file { '/temp/school':
  mode    => '0744',  
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}

