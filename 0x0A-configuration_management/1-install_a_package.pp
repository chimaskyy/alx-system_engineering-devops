# installs flask from pip3.

# Ensure python3 is installed
package { 'python3':
  ensure => present,
}

# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => present,
}

# Install Flask 2.1.0 using pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  name     => 'flask',
}

# Install Werkzeug 2.1.1 using pip
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
}

