# set up client SSH configuration file

#define file content
$file_content = @("EOF")
IdentityFIle ~/.ssh/school
PasswordAuthentication no
EOF

#manage file
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => $file_content,
}
