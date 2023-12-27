# set up client SSH configuration file

#define file content
$file_content = @("EOF")
IdentityFIle ~/.ssh/school
PasswordAuthentication no
EOF

#file path and permission
$file_path = '/etc/ssh/ssh_config'

#manage file
file { $file_path:
  ensure  => present,
  content => $file_content,
}
