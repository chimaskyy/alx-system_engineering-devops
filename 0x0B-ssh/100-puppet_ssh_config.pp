# client SSH configuration file so that you can connect to a server without typing a password

#define file content
$file_content = @("EOF")
IdentityFIle ~/.ssh/school
PasswordAuthentication no
EOF

#file path and permission
$file_path = '/etc/ssh/ssh_config'
$file_mode = '0644'

#manage file
file { $file_path:
  ensure  => present,
  mode    => $file_mode,
  content => $file_content,
}
