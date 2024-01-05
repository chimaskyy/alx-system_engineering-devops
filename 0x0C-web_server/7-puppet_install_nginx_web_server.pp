#installs and configures nginx using puppet

# ensure nginx is present
package {'nginx':
    ensure => 'present',
}

#install and update nginx
exec {'install_nginx':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  path     => '/usr/bin',
  require  => Package['nginx'],
}

#create Hello World index.html
file { '/var/www/html/index.html':
  ensure   => file,
  content  => "Hello World!",
  require  => Exec['install_nginx'],
}

# Configure Nginx with 301 redirect
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    server_name _;

    root /var/www/html;
    index index.html;

    location / {
	try_files $uri $uri/ =404;
    }

    location /redirect_me {
	return 301 https://github.com/chimaskyy;
    }
      ",
  require => Exec['install_nginx'],
}

#restart nginx
service  { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
